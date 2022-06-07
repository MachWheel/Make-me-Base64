<p align="center"><img src="https://i.imgur.com/ON7rqYL.png" alt="Simple Sleeper Logo"></p>
<h1 align="center">Make me Base64</h1>
<p align="center"><i>A fast way to convert any image (or a folder full of them) into Base64 bytestrings.</i></p>


# Single mode
![MAIN_DEMO](https://s8.gifyu.com/images/b64-single_CROP.gif)

- Open the app
- Choose an image
- Paste the string


# Batch mode
![MAIN_DEMO2](https://s8.gifyu.com/images/b64-batchmode_CROP.gif)

- Open the app
- Choose a folder
- Check **"__output.py_"** file


# How to install it
There is no installation needed.

Just download the zip file at [Releases](https://github.com/MachWheel/Make-me-Base64/releases), extract it 
and run the **standalone .exe file**.


# Is it "portable"?
**Yes!** In other words, you need just **Make-me-Base64.exe** to run this app. 
To uninstall, just delete it.


# Cloning the repository:

First, open the command-line and check your Python version. This app was made using **Python 3.10.3**:

    py --version


Now, install virtualenv if you don't have it:
    
    py -m pip install virtualenv


Clone the repository and change the directory to it:
    
    git clone https://github.com/MachWheel/Make-me-Base64.git
    cd Make-me-Base64


Create a virtualenv for the project, then activate it:
    
    py -m venv venv
    .\venv\Scripts\activate


Install project dependencies:
    
    py -m pip install -r requirements.txt


Done. Now you can run the app typing:

    py main.py


# How to compile it:

### First: [clone the repository and properly configure its virtualenv (see above)](#cloning-the-repository)
### Second: change to the directory and activate virtualenv if it is not already activated.

    cd Make-me-Base64
    .\venv\Scripts\activate

## Easy way:

### Inside Make-me-Base64 virtualenv, change the directory to compile and run the script:

    cd compile
    .\compile.bat

  - **The folder containing the generated .exe file will be opened automatically**

## Manual way:

Inside Make-me-Base64 virtualenv, change the directory to compile folder and run pyinstaller:

    cd compile
    pyinstaller -w --onefile ..\main.py --name Make-me-Base64 --icon app_icon.ico --splash splashfile.png
    
  - **The generated .exe file will be in .\compile\dist folder.**

## requirements.txt

    PySimpleGUI==4.60.1
    PyInstaller==5.1.0

    
