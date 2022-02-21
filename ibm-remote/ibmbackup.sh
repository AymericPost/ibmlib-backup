#!/bin/bash
args=("$@")

for arg in ${args[@]}; do
	system "CALL PGM(AS06005/QSHLIBBKUP) PARM($arg)"
	mv /QSYS.LIB/QGPL.LIB/$(echo $arg).FILE ~
done
