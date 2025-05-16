from pathlib import Path

path=Path('./alice.txt')

try:
    contents=path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"sorry,you have not the file {path}")
else:
    word=contents.split()
    new_word=len(word)
    print(f"the file {path} has about {new_word} words" )
