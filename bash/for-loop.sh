#!/bin/bash

# list/array of binarys 
X= (tmux bash vim)


for Y in ${X[@]}
do
	# ForEach bin in $X see if it is installed
	type $Y
done