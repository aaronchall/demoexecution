# demoexecution
Demo the Python execution model.

A package is a directory with an `__init__.py` file. When you import a package, the `__init__.py` is executed:

```
~/demoexecution$ python - << END
> import package
> END
package.__init__ is being executed
package.PackageClass is being executed
package.package_function var foo being executed
```

When you import a subpackage or (in this case) a submodule, the package `__init__.py` is executed first, 
then the module is executed.

You can delay the execution of a module by putting the import in a function. 

```
~/demoexecution$ python - << END
> import package.module
> defined_class = package.module.ClassDef()
> print('---')
> package.module.function()
> END
package.__init__ is being executed
package.PackageClass is being executed
package.package_function var foo being executed
package.module.py is being executed
package.module.ClassDef is being executed
package.module.ClassDef is being initialized
---
package.module.function is being executed
package.delay.py is being executed
```

