realSFS=~/software/misc/realSFS
wart_genome=/home/jfl323/pigs/references/warthog.chr.fa
pop_list=/home/jfl323/pigs/cleanWarts/pops/allPops.txt
pops_bam_folder=/home/jfl323/pigs/cleanWarts/pops
good_sites=/home/jfl323/pigs/subsampled_whole_genome/warthogGenomeSubsample_Nregions2000_sizePerRegion2e+05.region
out_folder=/home/jfl323/pigs/cleanWarts/fst/Desert_and_Wart/realSFS_folds/pop_safs


cat $pop_list | while read line; do
	mkdir $out_folder/$line
done

cat $pop_list | parallel -j 4 angsd -bam $pops_bam_folder/{}*.txt -anc $wart_genome -GL 2 -doSaf 1 -minQ 20 -minMapQ 30 -nThreads 15 -rf $good_sites -out $out_folder/{}/{}


cat $pop_list | parallel -j 2 $realSFS $out_folder/{}/{}.saf.idx -P 20 '>' $out_folder/{}/{}.sfs
