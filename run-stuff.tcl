#! /usr/bin/env tclsh

# Needs to be ran in a "wrapper script" due to issues with venv's activation and 
# lack of straightforward support for Tcl scripts.
catch {console show}

puts "Tcl web app runner"
puts "q - quit terminal"
puts "f - run frontend"
puts "b - run backend"
puts "s - run SQLite CLI (Win)"
flush stdout ;# prevent gets stdin from behaving weirdly with the output
set c [string tolower [gets stdin]] ;# read 1 character from stdin channel

proc run_npm {} {
  exec >&@stdout npm run dev ;# >&@stdout is shorthand for showing exec output instead of capturing it
}

proc run_uvicorn {dir} {
  # exec >&@stdout $dir/venv/Scripts/activate ;# Activate venv
  catch {exec >&@stdout cmd /c $dir/venv/Scripts/activate.bat} err
  exec >&@stdout uvicorn app.main:app --reload ;# >&@stdout is shorthand for showing exec output instead of capturing it
}

while {$c != "q"} {
  if {$c == "f"} {
    puts "Running frontend . . ."
    # https://stackoverflow.com/questions/23285360/how-to-get-path-of-current-script
    # This 'frees' the Tcl script from being bound to project's absolute paths
    # "it works on my machine!!" begone.
    cd "[file dirname [file normalize [info script]]]/vCalendar-frontend"
    run_npm
    break
  } elseif {$c == "b"} {
    puts "Running backend . . ."
    set backend_dir "[file dirname [file normalize [info script]]]/vCalendar-backend"
    cd $backend_dir
    run_uvicorn $backend_dir
    break
  } elseif {$c == "s"} {
    puts "Command to open the database in the CLI:"
    puts "./vCalendar-backend/database/maindb.db"
    # This smoothbrainedly assumes that SQLite CLI is installed in this directory and that you're using Windows
    exec >&@stdout {c:\sqlite\sqlite3.exe}
  } else {    
    puts stderr "Invalid input"
  }
  flush stdout
  set c [string tolower [gets stdin]]
}
