#!/bin/bash
args=("$@")

for arg in ${args[@]}; do
	system "CALL PGM($(cat ~/.clle_path)) PARM($arg)"
	mv /QSYS.LIB/QGPL.LIB/$(echo $arg).FILE ~
done
