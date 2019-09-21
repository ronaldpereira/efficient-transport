#!/bin/bash
rm $1saida-todos.txt
for file in $1*.txt;
do
	echo -n "$file " >> $1saida-todos.txt
	time timeout 5 python efficient_transport.py < $file >> $1saida-todos.txt
done
