# Setup

## Contents

1. [Virual Environments](#1-virtual-environments)

## 1. Virtual Environments

When starting a new project, it's good practice to create a _virual environment_ specifically for that project. This will essentially create a copy of the Python interpreter which can be modified to the specific needs of the current project.

To create a virtual environment run the following terminal command **inside your project's directory**.

```terminal
python3 -m venv env
```

Let's break down what this command is doing.

|           |                                                                                                                           |
| --------- | ------------------------------------------------------------------------------------------------------------------------- |
| `python3` | Tell the computer we want to do something with Python (try `python` instead of `python3` if your systems throws an error) |
| `-m`      | `-` is used to select options; `m` stands for "modify"                                                                    |
| `venv`    | Create a virtual environment.                                                                                             |
| `env`     | Name the virtual environment. `env` and `venv` are both popular naming choices.                                           |

After creating a virtual environment a new folder should show up in your project (again make sure you ran the command from project's directory).

```
|__ myProject
     |__ env
```

To begin customizing the environment for your project (adding `pandas` for example), you must activate it inside your terminal.

On Windows first run this command to grant the current terminal session script file execution priviledges.

```
Set-ExecutionPolicy Unrestricted -Scope Process
```

Then activate the environment.

```
env/Scripts/activate.bat
```

The terminal should now look something like this.

```terminal
(env) C:\[some_path]\myProject>
```

Now simply install the desired packages

```terminal
pip install pandas
    .
    .
    .
pip install matplotlib
```
