#!/bin/bash

CHR="chr1 chr2 chr3 chr4 chr5 chr6 chr7 chr8 chr9 chr10 chr11 chr12 chr13 chr14 chr15 chr16 chr17 chr18 chrX chrY"

cd /steveData/kristian/DNA/warthog/mapping/results/bam/ && ls *.bam | parallel -j 28 samtools view -M -F 3852 -h -b {} $CHR -o /home/jfl323/pigs/cleanWarts/{}.rmDupAnd0.bam
