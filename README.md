# Databasedoc

This is a small project aiming at providing an easy way to create a database 
documentation from the database schema.

Implemented in python, heavily relying on 
[sphinx](http://www.sphinx-doc.org/en/master/), it should be pretty lightweight
and easy to set up.

__Important__ : this project is still in its early phase ; feedbacks are welcome !

## How to use it

Simply execute :

```console
$ python generate_docs.py
$ cd docs/
$ make html 
```

This should generate all the necessary files in the docs/build/html/ folder. 
The root file is `index.html`.

## Doing

* Implement the tables description generator
* Support MySQL database format
* Tests

## TODO

* Package this code in order to make it installable, rather than having to clone 
the whole repository
* Provide interface for more database types


