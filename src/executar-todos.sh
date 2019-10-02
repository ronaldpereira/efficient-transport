#!/bin/bash

rm $1saida_todos_to.txt
for file in $1inputs/*.txt;
do
	echo -n "$file " >> $1saida_todos_to.txt
	time timeout 5 ./efficient_transport.out < $file >> $1saida_todos_to.txt
done

rm $1saida_todos.txt
for file in $1inputs/*.txt;
do
	echo -n "$file " >> $1saida_todos.txt
	time ./efficient_transport.out < $file >> $1saida_todos.txt
done
