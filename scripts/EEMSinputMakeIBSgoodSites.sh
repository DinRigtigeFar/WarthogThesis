dir=/home/jfl323/pigs/cleanWarts/eems
ibs=$dir/wartAndDesIBSforEEMS
whitelist=/home/jfl323/pigs/cleanWarts/treemix/sub_noBadHW.sites
bams=$dir/42inds_sorted.filelist



angsd -GL 2 -out $ibs -nThreads 5 -doMajorMinor 1 -doMaf 1 -minMinor 2 -setMinDepthInd 1 -setMaxDepthInd 60 -maxMis 20 -bam $bams -minmapQ 30 -minQ 20 -sites $whitelist -doCounts 1 -doIBS 1 -output01 1 -makeMatrix 1 -doCov 1
