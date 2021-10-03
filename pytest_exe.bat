set CUR_YYYY=%date:~6,4%
set CUR_MM=%date:~3,2%
set CUR_DD=%date:~0,2%
set CUR_HH=%time:~0,2%
if %CUR_HH% lss 10 (set CUR_HH=0%time:~1,1%)

set CUR_NN=%time:~3,2%
set CUR_SS=%time:~6,2%
set CUR_MS=%time:~9,2%

set DATM=%CUR_DD%.%CUR_MM%.%CUR_YYYY%-%CUR_HH%-%CUR_NN%-%CUR_SS%
set FOLD=%CUR_DD%.%CUR_MM%.%CUR_YYYY%
cd \
cd "C:\Private folder\Testscripts\Democases"
py.test test_exe.py --html=.\report\%FOLD%\Test_Report_%DATM%.html --html-report=.\report\%FOLD%\Test_Report_dashboard_%FOLD%.html
start chrome "file:///C:/Private folder/Testscripts/Democases"/report/%FOLD%/Test_Report_%DATM%.html"