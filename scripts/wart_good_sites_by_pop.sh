#!/bin/sh


pops=/home/jfl323/pigs/cleanWarts/pops/allPops.txt
blacklist=/home/jfl323/pigs/cleanWarts/pca/hwe_filtered_sites.txt
bams_folder=/home/jfl323/pigs/cleanWarts/pops

cat $pops | while read pop; do
	angsd -b $bams_folder/${pop}_pop.txt -nThreads 20 -doMajorMinor 1 -doMaf 1 -GL 2 -out $pop
	zcat $pop.mafs.gz | sed '1d' | cut -f1,2 | sed 's/\t/ /g' > all_sites_$pop.txt
	grep -Fvxf $blacklist all_sites_$pop.txt > sites_to_keep_$pop.txt
	angsd sites index sites_to_keep_$pop.txt
done
