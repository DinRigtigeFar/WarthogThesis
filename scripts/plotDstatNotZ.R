library(data.table)


master <- read.table("../noOutnoOthers.info")
df <- as.data.frame(master)

locIdx <- df$V1
names(locIdx) <- df$V2

dstatdf <- fread(cmd="cat /home/jfl323/pigs/cleanWarts/abbababa/mappedToPig/reapeatMasked/pigMappednoRepeatSubsampleBlockSize5mb.txt",data.table = F, stringsAsFactors = F)[,1:9]


getDstat3pop <- function(dstatdf, poptree){
  # extracts all individual dststs that meet poptree, where poptree is a vector c(H1,H2,H3)
  # returns also those that meet c(H2,H1,H3) with Dstat and Z score multiplied by -1 (IS THIS A CORRECT THING TO DO??)
  # return value is a dataframe with same columns as input plus poptree column specifying the population tree

  indTrees <- matrix(as.character(as.matrix(dstatdf[,1:3])), ncol=3)

  keep1 <- apply(matrix(locIdx[indTrees], ncol=3),  1, function(x) all(x == poptree))
  keep2 <- apply(matrix(locIdx[indTrees], ncol=3),  1, function(x) all(x == poptree[c(2,1,3)]))

  dstat1 <- dstatdf[keep1,]
  dstat2 <- dstatdf[keep2,]

  dstat2[,c("Dstat","jackEst", "Z")] <-  - dstat2[,c("Dstat","jackEst", "Z")]

  dstat <- rbind(dstat1,dstat2)

  dstat$poptree <- paste(poptree, collapse = ".")

  return(dstat)
}


# get all combinations with ghana as ougroup
pairs <- t(combn(c("Ghana", "Kenya", "Tanzania", "Zimbabwe", "Namibia", "Zambia"), m=2))
treesDesertOut <- cbind(pairs, rep("Desert", nrow(pairs)))

dstatsDesertOut <- do.call(rbind,apply(treesDesertOut, 1, getDstat3pop, dstatdf=dstatdf))
dstatsDesertOut$poptree <- as.factor(dstatsDesertOut$poptree)


png("/home/jfl323/pigs/cleanWarts/abbababa/mappedToPig/plots/DstatRepeatMakedPigBoxplotDstatsDesertH3.png",width=800, height = 800)
par(mar=c(5,14,4,4))
boxplot(dstatsDesertOut$Dstat ~ dstatsDesertOut$poptree,
        boxwex=0.5,
        main="All individuals Dstat combinations setting Desert as outroup (H3) and Sus scrofa as H4",
        horizontal=T,las=2,xlab="D stat",cex.axis=1.2,cex.lab=1.5)
abline(v=c(0),lty=2)
dev.off()

my_plot <- boxplot(dstatsDesertOut$Dstat ~ dstatsDesertOut$poptree, plot=FALSE)
outs <- dstatsDesertOut[dstatsDesertOut$Dstat %in% my_plot$out,]
write.table(outs, file="OutliersDstat.txt", sep="\t", row.names=FALSE)
