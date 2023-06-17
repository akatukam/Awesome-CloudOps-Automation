import os

def git_top_dir() -> str:
    """git_top_dir returns the output of git rev-parse --show-toplevel 

    :rtype: string, the output of the git rev-parse --show-toplevel command
    """
    run_output = run(["git", "rev-parse", "--show-toplevel"], capture_output=True)
    top_dir = run_output.stdout.strip()
    top_dir = top_dir.decode('utf-8')
    return top_dir

# Get the top-level directory of the Git repository
folder_path = git_top_dir()

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file == '__init__.py':
            file_path = os.path.join(root, file)
            with open(file_path, 'r+') as f:
                content = f.read()
                if '# pytype: skip-file' not in content:
                    f.seek(0, 0)
                    f.write('# pytype: skip-file\n' + content)

print("Adding skip-file was successful")
