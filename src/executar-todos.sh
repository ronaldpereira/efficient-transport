#!/bin/bash
rm $1saida_todos.txt
for file in $1*.txt;
do
	echo -n "$file " >> $1saida_todos.txt
	time python efficient_transport.py < $file >> $1saida_todos.txt
done
