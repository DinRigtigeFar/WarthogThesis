setwd(".")

library(ggplot2)

pops <- c("Desert", "Ghana", "Kenya","Tanzania","Zambia","Zimbabwe","Namibia")
new_pops <- pops

hets <- data.frame(Population = character(0), 
                   Individual = character(0), 
                   Heterozygosity = numeric(0))

for(i in (1:length(pops))){
  pop_hets <- read.table(paste("/home/jfl323/pigs/cleanWarts/heterozygosities/diff_depth_hets/folded_ind_sfs/",pops[i],"_heterozygosities.txt",sep=""))
  colnames(pop_hets) <- c("Population", "Individual", "Heterozygosity")
  
  hets <- rbind(hets, pop_hets)
}

pop<- hets$Population
ord<-c(which(pop=="Desert"), which(pop=="Ghana"), which(pop=="Kenya"), 
       which(pop=="Tanzania"),
       which(pop=="Zambia"),which(pop=="Zimbabwe"),which(pop=="Namibia"))
order<-pops
pop<-as.vector(pop[ord])
hets <- hets[ord,]
hets$Population <- factor(x=pop,levels = order)
colnames(hets)
mycolpal <- c("#A65628", "#E41A1C", "#377EB8", "#984EA3", "#4DAF4A", "#FF7F00", "#F0C000")


ggplot(hets)+geom_boxplot(aes(x=Population,
                              y=Heterozygosity,
                              fill=Population))+
  geom_jitter(aes(x=Population,
                  y=Heterozygosity), col="blue")+
  ggtitle("Desert- and common warthog heterozygosity \ndistribution by population") +
  theme_minimal() + theme(axis.text.x=element_text(size=10),
                          plot.title = element_text(size=16,hjust=0.5),
                          axis.title=element_text(size=12),
                          legend.position = "none")+
  scale_fill_manual(values=mycolpal)+
  ggsave("/home/jfl323/pigs/cleanWarts/heterozygosities/diff_depth_hets/folded_ind_sfs/JitterhetsWartAndDesert.pdf")
