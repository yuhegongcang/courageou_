import random


def number_game():
    numb = random.randrange(1, 11)
    guess = 0
    while guess != numb:
        guess = int(input("请输入一个1-10的数字："))
        if guess < numb:
            print("太小了")
        elif guess > numb:
            print("太大了")
    else:
        print("中！")


if __name__ == "__main__":
    number_game()
