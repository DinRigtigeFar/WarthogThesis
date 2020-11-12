# Adapted from script made by Kristian for leoaprd in /home/leopard/users/krishang/bed_region/get_nonrepeatmask.sh

ref=/davidData/genis/references/pig/SusScrofa11.1.fasta.gz
bed=/home/jfl323/pigs/noRepeatSscrofa11.1/pigMappedNonRepeat.bed

/home/krishang/software/vir_python36/bin/python /home/leopard/users/krishang/bed_region/scripts/get_upper.py $ref  |  /home/krishang/software/bedops/bin/bedops -m - > $bed
