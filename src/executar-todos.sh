#!/bin/bash
rm $1saida_todos_timeout_$2.txt
for file in $1*.txt;
do
	echo -n "$file " >> $1saida_todos_timeout_$2.txt
	time timeout $2 python efficient_transport.py < $file >> $1saida_todos_timeout_$2.txt
done
