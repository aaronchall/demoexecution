from __future__ import print_function

print('package.__init__ is being executed')

class PackageClass(object):
    print('PackageClass is being executed')

def package_function(foo=print('package_function var foo being executed')):
    print('package_function is being executed')


