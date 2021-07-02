@ECHO OFF
:: Check for Python Installation
python --version 2>NUL
if errorlevel 1 goto errorNoPython

:: Reaching here means Python is installed.

ECHO Downloading Python Installer
curl https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe -O python-3.9.6-amd64.exe
pip install -r requirements.txt
ECHO Setup Complete!
pause

:: Once done, exit the batch file -- skips executing the errorNoPython section
pause
goto:eof

:errorNoPython
echo.
echo Error^: Python not installed
curl https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe -O python-3.9.6-amd64.exe
python-3.9.6-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0