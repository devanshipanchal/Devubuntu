#!/bin/bash

cd /home/devanshi/Downloads
DAY=$(date +%F)s

echo "enter file extension:"
    read EXTENSION

echo "Please enter the prifix:(press enter for $DAY)"
   read 

for NAME in *.$EXTENSION
 do
   echo "Renaming $NAME to ${DAY}-${NAME}"
      mv $NAME ${DAY}-${NAME}

done 

