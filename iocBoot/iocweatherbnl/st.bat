set HOSTNAME=localhost
set IOCNAME=weatherbnl
set TOP=../../
set PATH=C:\Python313;C:\Windows
set PYTHONPATH=%TOP%devsupApp\src;%TOP%weatherApp
call dllPath.bat
..\..\bin\windows-x64\softIocPy3.13.exe st.cmd
