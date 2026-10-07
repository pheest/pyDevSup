@echo off
REM requires the pymetar module installed.
set OLD_PATH=%PATH%
call ..\env_vars.bat
call dllPath.bat
%TOP%\bin\windows-x64\softIocPy%PY_VER%.exe st.cmd
set PATH=%OLD_PATH%

