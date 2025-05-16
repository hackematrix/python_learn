from pathlib import Path

def count_words(path):
    """计算一个文件大致包含多少个单词"""

    try:
        data=path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"sorry,the file {path} does not exist")
    else:
        word=data.split()
        new_word=len(data)
        print(f"the file {path} has about {new_word} words")
