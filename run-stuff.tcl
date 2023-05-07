#! /usr/bin/env tclsh
puts "Tcl web app runner"
puts "q - quit terminal"
puts "f - run frontend"
flush stdout ;# prevent gets stdin from behaving weirdly with the output
set c [gets stdin] ;# read 1 character from stdin channel

proc run_npm {} {
  exec >&@stdout npm run dev ;# >&@stdout is shorthand for showing exec output instead of capturing it
}

while {[string tolower $c] != "q"} {
  if {[string tolower $c] == "f"} {
    puts "Running frontend . . ."
    cd D:/Programming/uni-se-prj/vCalendar-frontend
    run_npm
    break
  } else {
    puts "Invalid input"
  }
  flush stdout
  set c [gets stdin]
}
