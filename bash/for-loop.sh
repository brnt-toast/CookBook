#!/bin/bash

# list/array of binaries 
X= (tmux bash vim)


for Y in ${X[@]}
do
	# ForEach bin in $X see if it is installed
	type $Y
done
