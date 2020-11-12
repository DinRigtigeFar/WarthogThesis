#!/bin/bash

#parallel NGSadmixConv.sh beagle_test.beagle.gz {1} ::: {3..9}

for k in `seq 3 9`
do
	/home/jfl323/pigs/cleanWarts/scripts/NGSadmixConv.sh /home/jfl323/pigs/cleanWarts/subsample_wart_minInd18_35inds.beagle.gz $k
done
