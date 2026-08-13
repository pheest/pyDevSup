@echo off
REM requires the pymetar module installed.
REM set HOSTNAME=localhost
REM set IOCNAME=weatherbnl
set TOP=..\..
set CONFIG_PY=%TOP%\configure\os\CONFIG_PY.Common.windows-x64
REM https://stackoverflow.com/questions/232747/read-environment-variables-from-file-in-windows-batch-cmd-exe
setlocal EnableDelayedExpansion
for /F "tokens=1,2 delims==" %%i in ('type %CONFIG_PY%') do (
    set rawtoken=%%i
    REM rawtoken still ends with the " :" of the " := " text.
    set token=!rawtoken:~0,-2%!
    set rawvalue=%%j
    REM rawvalue still begins with the " " of the " := " text.
    set value=!rawvalue:~1%!
    if "!token!"=="PY_VER" (
        set PY_VER="!value!"
    )
    if "!token!"=="PY_LIBDIRS" (
        REM remove the "\libs" from the end of the string
        set PYTHON=!value:~0,-5%!
    )
)
set PATH=%PYTHON%;C:\Windows
REM set PYTHONPATH=%TOP%\devsupApp\src
call dllPath.bat
%TOP%\bin\windows-x64\softIocPy%PY_VER%.exe st.cmd
endlocal
