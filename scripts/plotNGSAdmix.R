#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

# Get ID and pop info for each individual
pop<-read.table(args[1])

# Read inferred admixture proportions file
q<-read.table(args[2])

# Plot them (ordered by population)
ord = order(pop[1])
par(mar=c(7,4,1,1))
# Change the values in col so the length matches K
barplot(t(q)[,ord],col=c(1,2,3,5,4),names=paste(pop[,1][ord], pop[,2][ord]),las=2,ylab="Demo1 Admixture proportions",cex.names=0.75)
