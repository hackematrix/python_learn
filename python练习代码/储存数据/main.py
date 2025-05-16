from pathlib import Path
import json

# json.dumps转化为json 格式
numbers=json.dumps([1,2,3,4,5,6])

path=Path('number.json').write_text(numbers)
