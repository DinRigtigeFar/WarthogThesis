#!/usr/bin/env Rscript

# Arg 1 is the location of the treemix files. Arg 2 is the popOrder file for residuals.
args = commandArgs(trailingOnly=TRUE)


source('/home/jfl323/pigs/cleanWarts/treemix/plotting_funcs.R')
my_data <- scan(args[1], what='thefuck')

for (i in my_data){
pdf(paste(i,'_and_residuals.pdf',sep=''))
plot_tree(i)
plot_resid(i, args[2])
dev.off()
}

