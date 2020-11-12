#!/bin/bash

pops=/home/jfl323/pigs/cleanWarts/pops/allPops.txt

cat $pops | while read pop; do
	grep -v "chrY\|chrX" sites_to_keep_$pop.txt > $pop.noSexSites.sites.txt
done
