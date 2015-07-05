print('module.py is being executed')

class ClassDef(object):
    print('ClassDef is being executed')

def function():
    print('function is being executed')
    from . import delay
