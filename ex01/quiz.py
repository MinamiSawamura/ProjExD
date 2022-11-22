import random

def shutudai(qa_lst):
    qa = random.choice(qa_lst)
    print("問題：" + qa["q"])
    return qa["a"]

def kaitou(ans_lst):
    ans = input("答えを入力してください：")
    if ans in ans_lst:
        print("正解！！！")
    else:
        print("不正解です･･･")

if __name__ == "__main__":
    qa_lst = [
        {"q":"サザエの旦那の名前は？", "a":["マスオ", "ますお"]}, 
        {"q":"カツオの妹の名前は？", "a":["ワカメ", "わかめ"]},
        {"q":"タラオはカツオから見てどんな関係？", "a":["甥", "おい", "甥っ子", "おいっこ"]}
    ]
    ans_lst = shutudai(qa_lst)
    kaitou(ans_lst)