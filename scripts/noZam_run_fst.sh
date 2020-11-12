realsfs=/home/jfl323/software/misc/realSFS
out_folder=/home/jfl323/pigs/cleanWarts/fst/Desert_and_Wart/realSFS_folds/
saf_folder=$out_folder/pop_safs
sfs_folder=$out_folder/2dsfs
fst_folder=$out_folder/fst
fst_bin=$fst_folder/binary
final=$out_folder/final_fst

# Do 2dSFS from saf files
$realsfs $saf_folder/Ghana/Ghana.saf.idx $saf_folder/Kenya/Kenya.saf.idx -P 20 -fold 1 > $sfs_folder/Ghana.Kenya.ml
$realsfs $saf_folder/Ghana/Ghana.saf.idx $saf_folder/Namibia/Namibia.saf.idx -P 20 -fold 1 > $sfs_folder/Ghana.Namibia.ml
$realsfs $saf_folder/Ghana/Ghana.saf.idx $saf_folder/Tanzania/Tanzania.saf.idx -P 20 -fold 1 > $sfs_folder/Ghana.Tanzania.ml
$realsfs $saf_folder/Ghana/Ghana.saf.idx $saf_folder/Zimbabwe/Zimbabwe.saf.idx -P 20 -fold 1 > $sfs_folder/Ghana.Zimbabwe.ml
$realsfs $saf_folder/Kenya/Kenya.saf.idx $saf_folder/Namibia/Namibia.saf.idx -P 20 -fold 1 > $sfs_folder/Kenya.Namibia.ml
$realsfs $saf_folder/Kenya/Kenya.saf.idx $saf_folder/Tanzania/Tanzania.saf.idx -P 20 -fold 1 > $sfs_folder/Kenya.Tanzania.ml
$realsfs $saf_folder/Kenya/Kenya.saf.idx $saf_folder/Zimbabwe/Zimbabwe.saf.idx -P 20 -fold 1 > $sfs_folder/Kenya.Zimbabwe.ml
$realsfs $saf_folder/Namibia/Namibia.saf.idx $saf_folder/Tanzania/Tanzania.saf.idx -P 20 -fold 1 > $sfs_folder/Namibia.Tanzania.ml
$realsfs $saf_folder/Namibia/Namibia.saf.idx $saf_folder/Zimbabwe/Zimbabwe.saf.idx -P 20 -fold 1 > $sfs_folder/Namibia.Zimbabwe.ml
$realsfs $saf_folder/Tanzania/Tanzania.saf.idx $saf_folder/Zimbabwe/Zimbabwe.saf.idx -P 20 -fold 1 > $sfs_folder/Tanzania.Zimbabwe.ml
$realsfs $saf_folder/Ghana/Ghana.saf.idx $saf_folder/Desert/Desert.saf.idx -P 20 -fold 1 > $sfs_folder/Ghana.Desert.ml
$realsfs $saf_folder/Kenya/Kenya.saf.idx $saf_folder/Desert/Desert.saf.idx -P 20 -fold 1 > $sfs_folder/Kenya.Desert.ml
$realsfs $saf_folder/Namibia/Namibia.saf.idx $saf_folder/Desert/Desert.saf.idx -P 20 -fold 1 > $sfs_folder/Namibia.Desert.ml
$realsfs $saf_folder/Tanzania/Tanzania.saf.idx $saf_folder/Desert/Desert.saf.idx -P 20 -fold 1 > $sfs_folder/Tanzania.Desert.ml
$realsfs $saf_folder/Zimbabwe/Zimbabwe.saf.idx $saf_folder/Desert/Desert.saf.idx -P 20 -fold 1 > $sfs_folder/Zimbabwe.Desert.ml

# Prepare for easy window analyses
$realsfs fst index $saf_folder/Ghana/Ghana.saf.idx $saf_folder/Kenya/Kenya.saf.idx -sfs $sfs_folder/Ghana.Kenya.ml -fstout $fst_bin/Ghana.Kenya -whichFst 1
$realsfs fst index $saf_folder/Ghana/Ghana.saf.idx $saf_folder/Namibia/Namibia.saf.idx -sfs $sfs_folder/Ghana.Namibia.ml -fstout $fst_bin/Ghana.Namibia -whichFst 1
$realsfs fst index $saf_folder/Ghana/Ghana.saf.idx $saf_folder/Tanzania/Tanzania.saf.idx -sfs $sfs_folder/Ghana.Tanzania.ml -fstout $fst_bin/Ghana.Tanzania -whichFst 1
$realsfs fst index $saf_folder/Ghana/Ghana.saf.idx $saf_folder/Zimbabwe/Zimbabwe.saf.idx -sfs $sfs_folder/Ghana.Zimbabwe.ml -fstout $fst_bin/Ghana.Zimbabwe -whichFst 1
$realsfs fst index $saf_folder/Kenya/Kenya.saf.idx $saf_folder/Namibia/Namibia.saf.idx -sfs $sfs_folder/Kenya.Namibia.ml -fstout $fst_bin/Kenya.Namibia -whichFst 1
$realsfs fst index $saf_folder/Kenya/Kenya.saf.idx $saf_folder/Tanzania/Tanzania.saf.idx -sfs $sfs_folder/Kenya.Tanzania.ml -fstout $fst_bin/Kenya.Tanzania -whichFst 1
$realsfs fst index $saf_folder/Kenya/Kenya.saf.idx $saf_folder/Zimbabwe/Zimbabwe.saf.idx -sfs $sfs_folder/Kenya.Zimbabwe.ml -fstout $fst_bin/Kenya.Zimbabwe -whichFst 1
$realsfs fst index $saf_folder/Namibia/Namibia.saf.idx $saf_folder/Tanzania/Tanzania.saf.idx -sfs $sfs_folder/Namibia.Tanzania.ml -fstout $fst_bin/Namibia.Tanzania -whichFst 1
$realsfs fst index $saf_folder/Namibia/Namibia.saf.idx $saf_folder/Zimbabwe/Zimbabwe.saf.idx -sfs $sfs_folder/Namibia.Zimbabwe.ml -fstout $fst_bin/Namibia.Zimbabwe -whichFst 1
$realsfs fst index $saf_folder/Tanzania/Tanzania.saf.idx $saf_folder/Zimbabwe/Zimbabwe.saf.idx -sfs $sfs_folder/Tanzania.Zimbabwe.ml -fstout $fst_bin/Tanzania.Zimbabwe -whichFst 1
$realsfs fst index $saf_folder/Ghana/Ghana.saf.idx $saf_folder/Desert/Desert.saf.idx -sfs $sfs_folder/Ghana.Desert.ml -fstout $fst_bin/Ghana.Desert -whichFst 1
$realsfs fst index $saf_folder/Kenya/Kenya.saf.idx $saf_folder/Desert/Desert.saf.idx -sfs $sfs_folder/Kenya.Desert.ml -fstout $fst_bin/Kenya.Desert -whichFst 1
$realsfs fst index $saf_folder/Namibia/Namibia.saf.idx $saf_folder/Desert/Desert.saf.idx -sfs $sfs_folder/Namibia.Desert.ml -fstout $fst_bin/Namibia.Desert -whichFst 1
$realsfs fst index $saf_folder/Tanzania/Tanzania.saf.idx $saf_folder/Desert/Desert.saf.idx -sfs $sfs_folder/Tanzania.Desert.ml -fstout $fst_bin/Tanzania.Desert -whichFst 1
$realsfs fst index $saf_folder/Zimbabwe/Zimbabwe.saf.idx $saf_folder/Desert/Desert.saf.idx -sfs $sfs_folder/Zimbabwe.Desert.ml -fstout $fst_bin/Zimbabwe.Desert -whichFst 1

#Final step
$realsfs fst stats $fst_bin/Ghana.Kenya.fst.idx > $final/Ghana.Kenya.txt
$realsfs fst stats $fst_bin/Ghana.Namibia.fst.idx > $final/Ghana.Namibia.txt
$realsfs fst stats $fst_bin/Ghana.Tanzania.fst.idx > $final/Ghana.Tanzania.txt
$realsfs fst stats $fst_bin/Ghana.Zimbabwe.fst.idx > $final/Ghana.Zimbabwe.txt
$realsfs fst stats $fst_bin/Kenya.Namibia.fst.idx > $final/Kenya.Namibia.txt
$realsfs fst stats $fst_bin/Kenya.Tanzania.fst.idx > $final/Kenya.Tanzania.txt
$realsfs fst stats $fst_bin/Kenya.Zimbabwe.fst.idx > $final/Kenya.Zimbabwe.txt
$realsfs fst stats $fst_bin/Namibia.Tanzania.fst.idx > $final/Namibia.Tanzania.txt
$realsfs fst stats $fst_bin/Namibia.Zimbabwe.fst.idx > $final/Namibia.Zimbabwe.txt
$realsfs fst stats $fst_bin/Tanzania.Zimbabwe.fst.idx > $final/Tanzania.Zimbabwe.txt
$realsfs fst stats $fst_bin/Ghana.Desert.fst.idx > $final/Ghana.Desert.txt
$realsfs fst stats $fst_bin/Kenya.Desert.fst.idx > $final/Kenya.Desert.txt
$realsfs fst stats $fst_bin/Namibia.Desert.fst.idx > $final/Namibia.Desert.txt
$realsfs fst stats $fst_bin/Tanzania.Desert.fst.idx > $final/Tanzania.Desert.txt
$realsfs fst stats $fst_bin/Zimbabwe.Desert.fst.idx > $final/Zimbabwe.Desert.txt
