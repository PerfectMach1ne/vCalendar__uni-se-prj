:: %~dp0 is Win Batch's insane way of getting current directory.
@echo off
:: Beloved Tcl's only limitation - cooperation with venv's activate scripts.
:: Without the line directly below, the "standalone script" just won't work.
:: venv needs to be activated "from the outside".
call "%~dp0\vCalendar-backend\venv\Scripts\activate.bat"
tclsh "%~dp0run-stuff.tcl"
