# ExamplePythonProject
This should serve as a solid example for creating a python project, leveraging good practices, as well as using package imports.


# Getting started

1. Create the virtual environment

In a terminal enter the following command to create the virtual environment:

```sh
python -m venv ./.venv
```

This command will create the required directories and place a pyvenv.cfg file in it.

2. Activate your virtual env by running the following command replacing `<venv>` with your path containing the virtual environment (./.venv)

(Depends on Platform)
| Platform | Shell      | Command                               |
| -------- | ---------- | ------------------------------------- |
| POSIX    | bash/zsh   | `$ source <venv>/bin/activate`        |
|          | pscore     | `$ <venv>/bin/Activate.ps1`           | 
| Windows  | cmd        | `C:\> <venv>\Scripts\activate.bat`    |
|          | PowerShell | `PS C:\> <venv>\Scripts\Activate.ps1` |

3. Install required python packages by using the requirements file in the root directory, this is accomplished by running the below command:

```sh
pip install -r requirements.txt
```

4. To test your code simply run the main.py file

```sh
python ./src/main.py
```

## Wrapping up

When you are finished with your virtual environment, simply type `deactivate` and it will deactivate the environment.

# Why the structure (Using Regular Packages)
From [The Python 3 docs](https://docs.python.org/3/reference/import.html#packages)

In python you can modularize your code by adding a special file to your directories. This file `__init__.py` indicates that you want what is known as a "Regular Package" which comes from Python 3.2 and earlier. This allows you to have a file `__init__.py` be implicitly executed. You can add import logic if needed, or leave empty and allow for you to import them as modules in other parts of your code.

## Namespace Packages
For Namespace Packages refernce [the Python Packaging Docs](https://packaging.python.org/en/latest/guides/packaging-namespace-packages/)

These packages are slightly different as they are more intended to be separately installed, used, and versioned. Similar to a package created for NPM.

## Same Directory Imports

Finally, you can also just create a file at the same root directory and import as such: 
```python
from <filename> import *
```