#! /bin/bash
OUTMAIN=/home/jfl323/pigs/cleanWarts/treemix/allsites_2020/runs/41inds_noss

#Run treemix with 0-4 migrations and put output in respective directories

for i in {0..4}
do
	mkdir -p $OUTMAIN/$i/log
	mkdir $OUTMAIN/$i/iter
	seq 150 | parallel -j 20 treemix -i treemix_41inds_400mbp_sites.frq.gz -o $OUTMAIN/$i/iter/41inds_${i}_mig_{}_iter -m $i -root SScrof -noss -bootstrap -k 500 '>' $OUTMAIN/$i/log/41inds_${i}_mig_{}_iter.log
done

mkdir $OUTMAIN/best

#Find the highest likelihood amongst the different iterations
grep -B 3 DONE $OUTMAIN/0/log/*0_mig*log | grep likelihood | sort -nk2 | tail -n 1 > $OUTMAIN/best/0_mig_best.txt

# Wait for remaining jobs to finish?
sleep 5m

for i in {1..4}
do
	grep -B 1 DONE $OUTMAIN/$i/log/* | grep likelihood | tr ":" "\t" | sort -nk2 | tail -n 1 > $OUTMAIN/best/${i}_mig_best.txt
done

cat $OUTMAIN/best/*mig_best.txt | cut -f 1 -d "." > $OUTMAIN/best/all_migs_best.txt

sed -i 's/log/iter/g' $OUTMAIN/best/all_migs_best.txt
sed -i 's/log/iter/g' $OUTMAIN/best/all_migs_best.txt

Rscript plotTreeAndResid.r $OUTMAIN/best/best_locations.txt 41indsPopOrder.txt
