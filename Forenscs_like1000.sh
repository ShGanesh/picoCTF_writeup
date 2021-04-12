#!/bin/bash

for i in {999..0..-1}         # {initial..final..increment}
do
	tar -xvf *.tar              # Using regex... tar -x(extract)v(verbose)f(file) *(all_characters).tar.
                              # *.tar means: all files present in working directory that end with ".tar".
	rm $(( $i+1 )).tar          # Remove file (i+1).tar
                              # If loop is currently in i==228, 229.tar is removed.
	rm filler.txt               #removing filler.txt

done
