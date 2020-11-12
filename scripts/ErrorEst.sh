#!/bin/bash

output="/home/jfl323/pigs/cleanWarts/errorEst/pigMapped/out"
anc1="/home/jfl323/pigs/cleanWarts/errorEst/pigMapped/1003.errorReady.fa.gz"
anc2="/home/jfl323/pigs/cleanWarts/errorEst/pigMapped/W18.errorReady.fa.gz"
bamlist="/home/jfl323/pigs/cleanWarts/errorEst/pigMapped/mapToSus.filelist"

cat refs.txt | parallel -j 2 angsd -doAncError 2 -anc $anc2 -ref {}.errorReady.fa.gz -nThreads 20 -bam $bamlist \
-uniqueOnly 1 -remove_bads 1 -only_proper_pairs 1 -minMapQ 30 -minQ 20 -rf /home/jfl323/pigs/cleanWarts/noSexChroms.rf -out $output/{}/W18/errorRate_55Warthogs_{}_ref_ancW18

cat refs.txt | parallel -j 2 Rscript /programs/albrecht/angsd/R/estError.R file=/home/jfl323/pigs/cleanWarts/errorEst/pigMapped/out/{}/W18/errorRate_55Warthogs_{}_ref_ancW18 out=/home/jfl323/pigs/cleanWarts/errorEst/pigMapped/out/{}/W18/error{}_W18out indNames=1002,1105,1130,1257,1259,1261,1262,1264,2418,2541,2660,3223,3224,3809,4466,5221,5222,5706,5707,5708,5709,5710,579,580,581,6272,6273,6274,6280,6436,7144,7146,7147,7151,7152,7155,7156,7160,7161,7162,7163,7966,8622,8623,8627,8628,8922,8928,8929,8931,8932,8943,8950,9124,931  main="Error rate using Potamochoerus porcus as outgroup and {} as a high quality genome"
