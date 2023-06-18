import inspect
import re
import os
from subprocess import run

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

def check_module_methods(module):
    """ Accepts a module and calls check_method_signature on each 
        function/method present in it.
        :type module: object
        :param module: The module being checked.
    """
    has_region = True
    for (name, member) in inspect.getmembers(module):
        if inspect.isfunction(member) or inspect.ismethod(member):
            if not check_method_signature(module, name):
               has_region = False
    assert has_region
