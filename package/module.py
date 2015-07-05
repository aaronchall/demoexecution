print('package.module.py is being executed')

class ClassDef(object):
    print('package.module.ClassDef is being executed')
    def __init__(self):
        print('package.module.ClassDef is being initialized')

def function():
    print('package.module.function is being executed')
    from . import delay
