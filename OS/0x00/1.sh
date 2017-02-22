#!/bin/bash

echo "ogi cuo za fish od oca"

MY_VAR = $(ls)

#kolekcijska for petlja
for f in $(ls)
do
	file $f
done

#argumentima pristupamo sa $1 $2...
# -eq -ne -- equal i not equal
if [[ $# -ne 1 ]]
then 
	echo "Usage: .prva.sh num"
	exit 1
fi

for ((i=1; i<=$1, i++))
do
	touch $i.txt
done
