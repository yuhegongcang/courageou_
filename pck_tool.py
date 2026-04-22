import struct
import os


def unpack_pck(pck_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(pck_path, "rb") as f:
        # 1. 验证是不是 PCK 文件 (读取前 4 个字节，必须是 GDPC)
        magic = f.read(4)
        if magic != b"GDPC":
            print("错误：这不是一个标准的 Godot PCK 文件！")
            return

        # 2. 读取版本信息
        # Godot 的数据是小端序 (Little-Endian)，用 '<I' 表示无符号 32 位整数
        pack_format = struct.unpack("<I", f.read(4))[0]
        major, minor, patch = struct.unpack("<III", f.read(12))
        print(f"解析成功！引擎版本: Godot {major}.{minor}.{patch}")

        # 跳过一些保留的标识位和填充字节
        # 标志位(4) + 基础偏移(8) + 预留空白(64) = 76 个字节
        f.seek(76, 1)  # 从当前位置向后跳 76 个字节

        # 3. 获取文件总数
        file_count = struct.unpack("<I", f.read(4))[0]
        print(f"包内共有 {file_count} 个文件\n")
        print("-" * 30)

        # 4. 读取目录表（索引）
        files_info = []
        for _ in range(file_count):
            # 读取路径长度
            path_len = struct.unpack("<I", f.read(4))[0]
            # 读取路径字符串并解码
            file_path = (
                f.read(path_len).decode("utf-8").rstrip("\x00")
            )  # 去除末尾的空字符
            # 读取该文件的起始位置(8字节)和大小(8字节)
            offset, size = struct.unpack("<QQ", f.read(16))
            # 跳过该文件的 MD5(16字节) 和 标志位(4字节)
            f.seek(20, 1)

            files_info.append({"path": file_path, "offset": offset, "size": size})

            # 如果是你想找的储君卡面，可以打印出来看看
            if "Radiate_portrait" in file_path or "regent" in file_path:
                print(f"找到目标: {file_path}")
                print(f"  起始位置: {offset}, 大小: {size} 字节")

        # 5. 提取你想替换的图片（举例提取所有文件，你也可以加 if 限制）
        print("-" * 30)
        print("开始提取文件...")
        for file_info in files_info:
            # 去除 Godot 默认的 'res://' 前缀，构建本地保存路径
            local_path = file_info["path"].replace("res://", "")
            full_save_path = os.path.join(output_dir, local_path)

            # 创建子文件夹
            os.makedirs(os.path.dirname(full_save_path), exist_ok=True)

            # 指针跳到文件数据的真实位置
            f.seek(file_info["offset"])
            # 抓取数据并保存
            file_data = f.read(file_info["size"])

            with open(full_save_path, "wb") as img_file:
                img_file.write(file_data)

        print(f"\n全部提取完成！文件已保存在 {output_dir}")


# 运行测试
# 把你的 pck 文件放在同目录下，把名字填在下面
unpack_pck("RegentCardsAnimeRework.pck", "./extracted_mod")
