#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)
# 1 is the popfile
# 2 is the qopt file from NGSadmix
# 3 is the EvalAdmix output
# 4 is the K

# read population labels and estimated admixture proportions
pop<-read.table(args[1],as.is=T)
q<-read.table(args[2])

# order according to population and plot the NGSadmix reults
ord<-order(pop[,1])
barplot(t(q)[,ord],col=2:10,space=0,border=NA,xlab="Individuals",ylab=paste("Admixture proportions for K=", args[4], sep=""))
text(tapply(1:nrow(pop),pop[ord,1],mean),-0.05,unique(pop[ord,1]),xpd=T)
abline(v=cumsum(sapply(unique(pop[ord,1]),function(x){sum(pop[ord,1]==x)})),col=1,lwd=1.2)

r<-read.table(args[3])

# Plot correlation of residuals
source("~/software/evalAdmix/NicePlotCorRes.R")
plotCorRes(cor_mat = r, pop = as.vector(pop[,1]), title=paste("Evaluation of warthog admixture proportions with K=", args[4], sep=""), max_z=0.1, min_z=-0.1, rotatelabpop=90)
