mycolpal=c("#E41A1C", "#377EB8", "#984EA3", "#4DAF4A", "#FF7F00", "#F0C000", "#A65628")

#arg 1 is pop list, 2 is cov matrix, 3 is name of pdf, 4 is the PC on x axis, 5 is the PC on the y axis and 6 is description of data
args = commandArgs(trailingOnly=TRUE)
dim1 <- as.numeric(args[4])
dim2 <- as.numeric(args[5])
what <- c(dim1,dim2)
ax1 <- dim1
ax2 <- dim2

pop<-read.table(args[1])

C <- as.matrix(read.table(args[2]))
e <- eigen(C)
pdf(paste(args[3],".pdf",sep = ""))
pcs <- c(round(e$values[ax1]/sum(e$values) * 100, digits=2), round(e$values[ax2]/sum(e$values) * 100, digits=2))

ord <- unique(sort(pop[,1]))

plot(e$vectors[,what], col=mycolpal[factor(pop[,1])], xlab=paste("PC", ax1," ", pcs[1], "%", sep=""),
     ylab=paste("PC", ax2, " ", pcs[2], "%", sep = ""),
     pch=as.numeric(factor(pop[,1])), main=paste("PC", ax1, " and ", "PC", ax2, " of ", args[6], sep=""))
abline(h=0, v=0, col="gray", lty=3, lwd=2)
#text(e$vectors[,what], row.names(pop), cex=0.6, pos=3, col="blue")
legend("topleft", legend=ord, col=mycolpal[factor(ord)], pch=factor(ord))
dev.off()
