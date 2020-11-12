
with open("/home/jfl323/pigs/noRepeatSscrofa11.1/noRepeatsAutosomesContigsPigMapped.rf", "r") as f:
	# Get the ranges of the no repeat regions
	to_eval = [j.strip().split("-") for idx, j in enumerate([k for i in f.readlines() for k in i.split(":")]) if idx%2!=0]

diffs = 0
for i in to_eval:
	diffs += int(i[1])-int(i[0])

print(diffs)
