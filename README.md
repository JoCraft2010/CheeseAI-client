# CheeseAI client

## 1. General information

CheeseAI is a client for pretrained models from [Huggingface](https://huggingface.co/models), supporting text-generation (transformers) and text-to-image (diffusers) so far.

All files and newer Versions are available on [GitHub](https://github.com/JoCraft2010/CheeseAI-client).

## 2. Installation

### 2.1. Windows

#### 2.1.1. Installing Python

Download and install the [newest version of Python](https://www.python.org/downloads/windows/), if you haven't already.

You can check, if your installation was successful, by opening PowerShell and typing
```commandline
py --version
```
and pressing enter.

#### 2.1.2. Creating a venv

If you already know how to create a venv, you can skip this section.

1. Go to the folder, where you want to install the CheeseAI client. **Warning:** The folder must be empty!

2. Open PowerShell by pressing ```Shift+Right mouse button->Open PowerShell in this location``` in your open folder.

3. Type
```commandline
py -m venv venv
cd venv
Scripts\activate
cd ..
```
to create and enter a venv called ```venv```. **Warning:** When you are finished with your installation, leave the venv, by typing
```commandline
deactivate
```

#### 2.1.3. Installing CheeseAI client

Copy All cheeseAI client files to your project folder. **Warning:** Copy them directly to your installation folder, so your file system will look like this:
```
(Project folder)
|- dependencies_setup
|  |- [...]
|- [...]
|- venv
|  |- Lib
|  |  |- [...]
|  |- Scripts
|  |  |- [...]
|  |- share
|  |  |- [...]
|  |- .gitignore
|  |- pyvenv.cfg
|- webui
|  |- [...]
|- config.ini
|- [...]
|- main.py
|- [...]
|- prepare_setup.py
|- README.md
|- [...]
|- setup.py
|- [...]
```

#### 2.1.4. Setting up all dependencies

Go back to PowerShell and make sure, that you are inside the venv, you created.
You are inside a venv, when PowerShell looks something like ```(venv) PS C:\Path\to\your\folder>```.
Also make sure, that you are directly in your installation folder.
When, these requirements are met, run the command
```commandline
py prepare_setup.py
```
and answer all questions provided by the program. The program will provide a command that should look something like
```commandline
py setup.py processortype --some_kind_of_flag
```
Execute the given command in PowerShell while making sure, you are still directly in your installation folder.
You will be given another command, you have to execute that will look something like
```powershell
./dependencies_setup/install_this.ps1
```
This command will set up all dependencies for you.

## 3. Usage

### 3.1. Windows

1. Open PowerShell, as described in 2.1.2.2.

2. Enter your previously created venv using
```commandline
cd venv
Scripts\activate
cd ..
```

3. Run the program by executing
```commandline
py main.py
```
inside the venv or running main.py using the IDE of your choice.

4. After a few seconds, a console and an instance of your default browser with the UI should open.
