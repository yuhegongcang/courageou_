import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin

# ================= 配置区域 =================
# 替换为你想要抓取的小说目录页的完整 URL
TOC_URL = "https://d59897de51877044b88.bqg810.cc/#/book/113680/"
# 保存的文件名
OUTPUT_FILE = "downloaded_novel.txt"
# ==========================================

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9",
}


def get_html(url):
    """通用的请求网页方法，处理了编码问题"""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        # 很多中文小说站使用 GBK 编码，这里让 requests 自动推测或强制处理
        response.encoding = response.apparent_encoding
        return response.text
    except Exception as e:
        print(f"请求失败 {url}: {e}")
        return None


def get_chapter_links(toc_url):
    """从目录页提取所有章节的链接"""
    html = get_html(toc_url)
    if not html:
        return []

    soup = BeautifulSoup(html, "html.parser")
    chapter_links = []

    # 笔趣阁的目录通常在一个 id 为 'list' 的 div 下的 dl 标签内
    # 这里我们寻找包含所有 <a> 标签的区域
    list_div = soup.find("div", id="app")

    if list_div:
        a_tags = list_div.find_all("a")
        for a in a_tags:
            href = a.get("href")
            title = a.get_text(strip=True)
            if href:
                # 拼接成完整的 URL (处理相对路径的情况)
                full_url = urljoin(toc_url, href)
                chapter_links.append((title, full_url))

    return chapter_links


def scrape_chapter_content(chapter_url):
    """抓取单章正文并清洗格式"""
    html = get_html(chapter_url)
    if not html:
        return "【章节内容获取失败】\n"

    soup = BeautifulSoup(html, "html.parser")

    # 笔趣阁的正文通常在 id='content' 的 div 中
    content_div = soup.find("div", id="content")

    if content_div:
        # 处理 <br> 标签，将其替换为换行符，保留小说的段落格式
        for br in content_div.find_all("br"):
            br.replace_with("\n")

        # 提取文本，去掉首尾空格和无用的网站广告词
        text = content_div.get_text(strip=True)
        # 清洗掉一些常见的笔趣阁内嵌广告（可选）
        text = text.replace("请记住本书首发域名：...", "")

        # 将连在一起的换行符稍微整理一下，让排版更好看
        cleaned_text = "\n\n".join([p.strip() for p in text.split("\n") if p.strip()])
        return cleaned_text
    else:
        return "【未匹配到正文内容，请检查网页结构】\n"


def main():
    print("开始获取目录...")
    chapters = get_chapter_links(TOC_URL)

    if not chapters:
        print("未获取到章节目录，请检查 TOC_URL 或目录解析规则 (`div id='list'`)。")
        return

    print(f"成功获取目录，共 {len(chapters)} 章。准备开始下载...")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        # 为了演示，如果你不想一次性下完，可以使用切片 chapters[:5] 只下前 5 章测试
        for index, (title, url) in enumerate(chapters):
            print(f"正在抓取 ({index+1}/{len(chapters)}): {title}")

            content = scrape_chapter_content(url)

            # 写入文件
            f.write(f"\n\n{'='*20} {title} {'='*20}\n\n")
            f.write(content)

            # 【绝对关键的一步】：必须休眠！
            # 笔趣阁等网站会对高频请求进行封 IP 处理。每次请求后停顿 1.5 到 3 秒是基本礼仪和防封策略。
            time.sleep(2)

    print(f"下载完成！文件已保存至: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
