import inspect
import re
import os
import importlib
import sys
from subprocess import run
import glob
import types

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

def check_method_signature(param, method_name):
    if re.search(r"egion", param):
        # checks if that riff is "region" exactly
        pattern = r"(?<![^\s(])region(?=\s|:|\))"
        return bool(re.findall(pattern, param+")"))
    else:
        return True

def check_module_methods(module):
    has_region = True
    module_act = importlib.util.module_from_spec(module)
    module_source = inspect.getsource(module_act)
    method_matches = re.findall(r"def (.*?)\)", module_source, flags=re.DOTALL)
    for method_match in method_matches:
        method_name = re.findall(r"(\w+)\s*\(", method_match)
        if not check_method_signature(method_match, method_name[0]):
            has_region = False
    assert(has_region)

if __name__ == '__main__':   
    """  
    entries = os.listdir('/home/runner/work/Awesome-CloudOps-Automation/Awesome-CloudOps-Automation/Datadog/legos/datadog_search_monitors')
    for entry in entries:
        print(entry)
    """
    module = importlib.util.spec_from_file_location("datadog_search_monitors","/home/runner/work/Awesome-CloudOps-Automation/Awesome-CloudOps-Automation/Datadog/legos/datadog_search_monitors/datadog_search_monitors.py")
    check_module_methods(module)
    print(f"TESTChecked module")
    
    """     
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                print(f"File path: {file_path}")
                module_name = os.path.splitext(file)[0]
                try:
                    module = importlib.util.spec_from_file_location(module_name,file_path)
                    check_module_methods(module)
                    print(f"Checked module: {module_name}")
                except Exception as e:
                    print(f"Error importing module {module_name}: {str(e)}")
    """
    assert True
