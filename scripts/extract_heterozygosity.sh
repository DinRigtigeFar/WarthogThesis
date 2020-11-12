#!/bin/sh

pop_list=/home/jfl323/pigs/cleanWarts/pops/allPops.txt
out_folder=/home/jfl323/pigs/cleanWarts/heterozygosities/diff_depth_hets/folded_ind_sfs
calc_h=/home/jfl323/pigs/cleanWarts/scripts/calc_h.Rscript

cat $pop_list | while read pop; do
	cat $out_folder/$pop/*.sfs > all_sfs_$pop
	Rscript --vanilla $calc_h $pop
	ls $out_folder/$pop/ | cut -f1 -d"." > bam_ids
	paste bam_ids $out_folder/${pop}_het.txt > $out_folder/${pop}_heterozygosities.txt
	rm bam_ids
	rm $out_folder/${pop}_het.txt
	rm all_sfs_$pop
done
