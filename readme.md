# Python & AI Notes

This repository is where I collect notes and examples as I learn Python and artificial intelligence.

## Repository contents

### `09_OOPS_In_Python/`

This folder contains Python examples and notes on object-oriented programming:

- [`01_SimpleClass.py`](./09_OOPS_In_Python/01_SimpleClass.py) — Defining simple classes, creating objects, and checking an object's type.
- [`02_NameSpace.py`](./09_OOPS_In_Python/02_NameSpace.py) — Class and instance attributes, object namespaces, and adding attributes to objects.
- [`03_AttributeShadowing.py`](./09_OOPS_In_Python/03_AttributeShadowing.py) — Attribute shadowing: overriding a class attribute on an instance and deleting the instance attribute to reveal the class value again.
- [`04_SelfArgs.py`](./09_OOPS_In_Python/04_SelfArgs.py) — Instance methods, the purpose of `self`, and calling a method through an object or class.
- [`05_init_objects.py`](./09_OOPS_In_Python/05_init_objects.py) — The `__init__` constructor and initializing different objects with their own values.
- [`06_inheritance_composition.py`](./09_OOPS_In_Python/06_inheritance_composition.py) — Inheritance and composition, with examples of combining both patterns.
- [`07_BaseClass.py`](./09_OOPS_In_Python/07_BaseClass.py) — Calling a base-class constructor directly or with `super()` to reuse initialization in a subclass.
- [`08_Method_Resolution_Order.py`](./09_OOPS_In_Python/08_Method_Resolution_Order.py) — Method Resolution Order (MRO) and how Python searches parent classes in multiple inheritance.
- [`09_Static_Methods.py`](./09_OOPS_In_Python/09_Static_Methods.py) — Defining and calling static methods that do not rely on instance or class state.
- [`10_Class_Method.py`](./09_OOPS_In_Python/10_Class_Method.py) — Class methods, alternative object constructors, and a static method for validating order data.
- [`11_Property_Decorators.py`](./09_OOPS_In_Python/11_Property_Decorators.py) — The `@property` getter and setter decorators, attribute-style access, and validating values before assignment.

### `10_File_And_Exception_Handling_in_Python/`

This folder contains examples of Python exceptions, error handling, and working with files:

- [`01_Basic.py`](./10_File_And_Exception_Handling_in_Python/01_Basic.py) — Common built-in exceptions, the differences between similar exception types, and the purpose of exception-handling keywords.
- [`02_try_except.py`](./10_File_And_Exception_Handling_in_Python/02_try_except.py) — Handling exceptions with `try` and `except`, plus using `else` and `finally`.
- [`03_Multiple_Exception.py`](./10_File_And_Exception_Handling_in_Python/03_Multiple_Exception.py) — Handling different exceptions, such as missing menu items and invalid quantity types.
- [`04_Custom_Errors.py`](./10_File_And_Exception_Handling_in_Python/04_Custom_Errors.py) — Raising a built-in `ValueError` when a chai flavour is unsupported.
- [`05_Custom_Exceptions.py`](./10_File_And_Exception_Handling_in_Python/05_Custom_Exceptions.py) — Defining and raising a custom exception for missing ingredients.
- [`06_complete_order.py`](./10_File_And_Exception_Handling_in_Python/06_complete_order.py) — Combining custom errors, input checks, exception handling, and cleanup in an order-billing example.
- [`07_File_Handling.py`](./10_File_And_Exception_Handling_in_Python/07_File_Handling.py) — Opening and writing files, and using a `with` statement to close files automatically.

### `11_Threads_Concurrency/`

This folder explores concurrency, threading, multiprocessing, and the Global Interpreter Lock (GIL):

- [`01_threading.py`](./11_Threads_Concurrency/01_threading.py) — Concurrency versus parallelism, thread creation and coordination, and examples of overlapping tasks.
- [`02_multiprocessing.py`](./11_Threads_Concurrency/02_multiprocessing.py) — Running tasks in separate processes, and starting and joining multiple processes.
- [`03_Global_Interpreter_Lock_Threading.py`](./11_Threads_Concurrency/03_Global_Interpreter_Lock_Threading.py) — The GIL's effect on CPU-bound threads and why threads can still help with I/O-bound work.
- [`04_GIL_multiprocessing.py`](./11_Threads_Concurrency/04_GIL_multiprocessing.py) — Using multiprocessing for CPU-bound work, comparing it with threading, and protecting process startup with the main guard.

More notes and examples will be added as I continue learning.
