# demoexecution
Demo the Python execution model.

A package is a directory with an `__init__.py` file. When you import a package, the `__init__.py` is executed:

```
~/demoexecution$ python - << END
import package
> END
package.__init__ is being executed
PackageClass is being executed
package_function var foo being executed
```

When you import a subpackage or (in this case) a submodule, the package `__init__.py` is executed first, 
then the module is executed.

You can delay the execution of a module by putting the import in a function. 

```
~/demoexecution$ python - << END
> import package.module
> print('---')
> package.module.function()
> END
package.__init__ is being executed
PackageClass is being executed
package_function var foo being executed
module.py is being executed
ClassDef is being executed
---
function is being executed
delay.py is being executed

```
