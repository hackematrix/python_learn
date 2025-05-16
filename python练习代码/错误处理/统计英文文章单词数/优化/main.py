from  word import count_words
from pathlib import Path

filenames=['alice.txt','litte.txt','moby.txt','hello.txt']

for filename in filenames:
    path=Path(filename)
    count_words(path)
