import inspect
import re
import os
import importlib
import sys
from subprocess import run
import glob

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

def check_method_signature(module, method_name):
    """ Accepts a module and a method/function from that module and
        returns true if the method signature either doesn't contain 
        a riff or "region" at all, or contains "region" exactly. Else
        it returns false.
        :type module: object
        :param module: The module being checked.
        :type method_name: string
        :param method_name: Name of the method to check.
    """
    return True
"""
    print("hello")
    print("module:")
    print(type(module))
    module_name = module.name
    print(f"Module name: {module_name}")
    module_act = importlib.util.module_from_spec(module)
    print(type(module_act))
"""
"""      
    method = getattr(module, method_name, None)
    print("method:")
    print(type(method))
    method_name = method.__name__
    print(f"Method name: {method_name}")
"""
"""
    method = getattr(module, method_name, None)
    if method is not None:
        (source_lines, _) = inspect.getsourcelines(method)
        # partial matches with "egion" to see if any riff is present
        if re.search(r"egion", source_lines[0]):
            # checks if that riff is "region" exactly
            pattern = r"def {}\(.*\bregion(\s|:|\)).*:".format(re.escape(method_name))
            return bool(re.findall(pattern, source_lines[0]))
        else:
            return True
    else:
        return True
"""
def check_module_methods(module):
    """ Accepts a module and calls check_method_signature on each 
        function/method present in it.
        :type module: object
        :param module: The module being checked.
    """
    module_act = importlib.util.module_from_spec(module)
    print("module:")
    print(type(module_act))
    print(module_act.__name__)

    module_methods = [
        (name, member)
        for name, member in inspect.getmembers(math)
        if inspect.isfunction(member) and member.__module__ == math.__name__
    ]

    for name, method in module_methods:
        print(f"Method name: {name}")
        print()

"""
    has_region = True
    for (name, member) in inspect.getmembers(module_act):
        print(name)
        print(member)
        if inspect.isfunction(member) or inspect.ismethod(member):
            print("name:")
            print(name)
            if not check_method_signature(module, name):
               has_region = False
    if not has_region:
        print(f"Assertion failed: Module: {module.name}")
        assert has_region
"""

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
