from pathlib import Path

for path in Path('hendlers').rglob('*.py'):
    print(path.name)