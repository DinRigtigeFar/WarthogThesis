#!/bin/bash

realSFS=/programs/albrecht/angsd/misc/realSFS
wart_genome=/home/jfl323/pigs/references/warthog.chr.fa
bams_folder=/steveData/jfl323/pigs/cleanWarts/
pop_list=/home/jfl323/pigs/cleanWarts/pops/allPops.txt
pops_info_folder=/home/jfl323/pigs/cleanWarts/pops
sites_info_folder=/home/jfl323/pigs/cleanWarts/sites_to_keep
out_folder=/home/jfl323/pigs/cleanWarts/heterozygosities/diff_depth_hets

mkdir $out_folder/ind_sfs
mkdir $out_folder/saf_files

cat $pop_list | while read pop; do
	cut -f2 $pops_info_folder/${pop}.info | while read ind; do
		case $ind in

			8922 | 2418 | 7155 | 1257 | 2541 | 8627)
        angsd -i $bams_folder/$ind.bam.rmDupAnd0.bam -anc $wart_genome -GL 2 -doSaf 1 -minQ 20 -minMapQ 30 -doCounts 1 -setMinDepthInd 8 -setMaxDepthInd 30 -nThreads 20 -sites $sites_info_folder/$pop.noSexSites.sites.txt -out $out_folder/saf_files/$ind
				$realSFS $out_folder/saf_files/$ind.saf.idx -P 20 -fold 1 > $out_folder/folded_ind_sfs/$pop/{}.sfs
				;;

			*)
				angsd -i $bams_folder/$ind.bam.rmDupAnd0.bam -anc $wart_genome -GL 2 -doSaf 1 -minQ 20 -minMapQ 30 -doCounts 1 -setMinDepthInd 2 -setMaxDepthInd 12 -nThreads 20 -sites $sites_info_folder/$pop.noSexSites.sites.txt -out $out_folder/saf_files/$ind
        $realSFS $out_folder/saf_files/$ind.saf.idx -P 20 -fold 1 > $out_folder/folded_ind_sfs/$pop/{}.sfs
                    		;;
                esac
        done
done
