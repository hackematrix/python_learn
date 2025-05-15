from pathlib import Path

data=Path('./pi_digits.txt').read_text()

new_data=Path('progamming.txt').write_text('\nI love creating new games')


print(data)
