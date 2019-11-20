set filename ./datafile.txt
set fileId [open ./$filename r]
gets $fileId line
set fields [split [lindex [split $line "\""] 1] ":"]
set portId [lindex $fields end]
puts "Info: portId = $portId"

