#!/bin/bash

NGSA=/home/jfl323/software/NGSadmix

file=$1 # Input file
nfile=admix_result
num=1000  # Maximum number of iterations
P=30 #numer of threds/cores used

K=$2 #number of populations. Max ligger på antal lokaliteter, men 2-8 må være passende
out=$K #output  directory (no /)

rm $out/$nfile.$K.likes

mkdir $out

for f in `seq $num`
do
    echo -n -e $f"\t"
    echo $file
    echo $K
    $NGSA -likes $file -seed $f -K $K -P $P -o $out/$nfile.$K.$f
    grep "like=" $out/$nfile.$K.$f.log | cut -f2 -d " " | cut -f2 -d "=" >> $out/$nfile.$K.likes
    CONV=`Rscript -e "r<-read.table('$out/$nfile.$K.likes');r<-r[order(-r[,1]),];cat(sum(r[1]-r<3),'\n')"` #Check for convergence. ¿3,5...?

    if [ $CONV -gt 2 ]  #-gt 2 = greater than 2
    then
	cp $out/$nfile.$K.$f.qopt $out/$nfile.$K.$f.qopt_conv
	cp $out/$nfile.$K.$f.fopt.gz $out/$nfile.$K.$f.fopt_conv.gz
	cp $out/$nfile.$K.$f.log $out/$nfile.$K.$f.log_conv
	break
    fi

done
