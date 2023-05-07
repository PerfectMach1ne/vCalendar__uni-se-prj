#!/bin/bash

# Works, but not with wsl and bash. Only git's bash is able of rendering the entire Tcl script functional.
# Why? I don't know!
# WSL is a lovely disaster, I guess!
# Launch "c:\Program Files\Git\bin\bash.exe"
# or "# Launch "c:\Program Files\Git\git-bash.exe"
get_script_dir () {
     SOURCE="${BASH_SOURCE[0]}"
     # While $SOURCE is a symlink, resolve it
     while [ -h "$SOURCE" ]; do
          DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
          SOURCE="$( readlink "$SOURCE" )"
          # If $SOURCE was a relative symlink (so no "/" as prefix, need to resolve it relative to the symlink base directory
          [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE"
     done
     DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
     echo "$DIR"
}
cd "$(get_script_dir)/vCalendar-backend/venv/Scripts"
. ./activate
cd ../../../
tclsh "./run-stuff.tcl"