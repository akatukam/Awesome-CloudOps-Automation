import os

for root, dirs, files in os.walk('.'):
    for file in files:
        if file == '__init__.py':
            file_path = os.path.join(root, file)
            with open(file_path, 'r+') as f:
                content = f.read()
                if '# pytype: skip-file' not in content:
                    f.seek(0, 0)
                    f.write('# pytype: skip-file\n' + content)
