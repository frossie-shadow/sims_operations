# File for holding little utilities
import importlib

__all__ = ["loadClass", "makeIntDict"]

def makeIntDict(ilist):
    """
    This function makes an integer indexed dictionary from a list.

    @param ilist: The list to make the dictionary from.
    @return: An integer indexed dictionary.
    """
    return dict([(i, ilist[i]) for i in range(len(ilist))])

def loadClass(full_class_string):
    """
    Dynamically load a class from a string. Taken from the following blog:
    http://thomassileo.com/blog/2012/12/21/
           dynamically-load-python-modules-or-classes/

    @param full_class_string: A standard import like call.
    @return: An instance of the class.
    """
    class_data = full_class_string.split(".")
    module_path = ".".join(class_data[:-1])
    class_str = class_data[-1]

    module = importlib.import_module(module_path)
    # Finally, we retrieve the Class
    return getattr(module, class_str)
