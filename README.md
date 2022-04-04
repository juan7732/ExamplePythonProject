# ExamplePythonProject
This should serve as a solid example for creating a python project, leveraging good practices, as well as using package imports.


# Getting started

1. Create the virtual environment

In a terminal enter the following command to create the virtual environment:

`python -m venv ./.venv`

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

`pip install -r requirements.txt`

4. To test your code simply run the main.py file

`python ./src/main.py`