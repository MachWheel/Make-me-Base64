@ECHO OFF
TITLE Make-me-Base64 Compiler
ECHO Make-me-Base64 Compiler
ECHO:
ECHO This batch script compiles Make-me-Base64 application
ECHO:
ECHO Make sure to proper configure the project virutalenv first.
ECHO:
ECHO You should run this script inside the project virtualenv to avoid problems.
ECHO:
ECHO The generated app will be in the ./dist folder
ECHO:
PAUSE
MKDIR dist
pyinstaller -w --onefile ..\main.py --name Make-me-Base64
ECHO DONE! PRESS ANY KEY TO OPEN THE OUTPUT FOLDER.
ECHO:
PAUSE
START dist
