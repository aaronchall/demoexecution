from __future__ import print_function

print('package.__init__ is being executed')

class PackageClass(object):
    print('package.PackageClass is being executed')

def package_function(foo=print('package.package_function var foo being executed')):
    print('package.package_function is being executed')


