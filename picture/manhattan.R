# clear the environment
  rm(list = ls())

# 如果有这两个包，省略此步骤
# install.packages("qqman")
# install.packages("Caio")

# load the packages
  library(qqman)
  library(Cairo)
  library(dplyr)

# set as working directory & read data
  setwd("F:/IAS_CAAS/Project/芯片/SNP位点选择/5组选择信号top1%位点注释与富集结果")
  data <- read.csv("F:/IAS_CAAS/Project/芯片/SNP位点选择/5组选择信号top1%位点注释与富集结果/5组选择信号top1%位点注释与富集结果/FZ/3.选择信号分析结果/3-6.候选目标位点/signifSNP_FZ_0.01.csv",header = T)

# extrat data as a data frame
  data.frame <- data[, c("SNP", "CHROM", "POS", "FST")]
  data.frame <- data.frame[data.frame$FST >= 0, ]
  
# install.packages("CMplot")
  library(CMplot)
  x <- data.frame
  head(x)  
  
# CMplot 绘图
  # SNP密度图
  CMplot(x, 
         plot.type = "d",
         col = c("blue","red","yellow"), 
         file.output = F
         )

  # 曼哈顿图
  CMplot(x,plot.type = "m", 
         threshold = c(0.01,0.05)/nrow(x), 
         amplify = T, 
         signal.cex = c(1,1), 
         signal.pch = c(20,20),
         signal.col = c("red","blue"), 
         multracks = F,
         file.output = T
         )
  # 多性状环形曼哈顿图
  CMplot(x, 
         plot.type = "c", 
         r=0.5, 
         threshold = c(1e6,1e6),
         cex = 1, 
         threshold.col = c("red","blue"),
         cir.chr.h = 2, 
         signal.cex = c(2,2), 
         signal.col = c("red","green"), 
         file.output = T
         )
  # 多层圈图
  CMplot(x, 
         plot.type = "c", 
         r=0.4, 
         col = c("grey30","grey60"), 
         chr.labels = paste("", c(1:25),sep = ""), 
         threshold = c(1e-6,1e-4), 
         cir.chr.h = 1.5, 
         amplify = TRUE, 
         threshold.lty = c(1,2), 
         threshold.col = c("red","blue"), 
         signal.line = 1, 
         signal.col = c("red","green"), 
         chr.den.col = c("darkgreen","yellow","red"), 
         bin.size = 1e6, 
         outward = FALSE, 
         file = "jpg",
         dpi = 300, 
         file.output = TRUE, 
         verbose = TRUE
         )
  # 曼哈顿图
  CMplot(
    x, 
    plot.type = "m", 
    col=c("grey30","grey60"), 
    LOG10=TRUE, 
    ylim=c(2,8), #y轴数值调整
    threshold=c(1e-6,1e-4),#显著位点筛选
    threshold.lty=c(1,2), 
    threshold.lwd=c(1,1), 
    threshold.col=c("black","grey"), 
    amplify=TRUE,
    chr.den.col=NULL, 
    signal.col=c("red","green"), 
    signal.cex=c(1,1), 
    signal.pch=c(19,19),
    file="jpg",
    dpi=300,
    file.output=TRUE,
    verbose=TRUE
  )
  # 曼哈顿图+条形图
  CMplot(
    x, 
    plot.type="m", 
    LOG10=TRUE, 
    ylim=NULL, 
    threshold=c(1e-6,1e-4), 
    threshold.lty=c(1,2),
    threshold.lwd=c(1,1), 
    threshold.col=c("black","grey"), 
    amplify=TRUE,
    bin.size=1e6,
    chr.den.col=c("darkgreen", "yellow", "red"),
    signal.col=c("red","green"),
    signal.cex=c(1,1),
    signal.pch=c(19,19),
    file="jpg",
    dpi=300,
    file.output=TRUE,
    verbose=TRUE
  )
  # 分染色体曼哈顿图
  CMplot(
    x, 
    plot.type="m", 
    multracks=TRUE, 
    threshold=c(1e-6,1e-4),
    threshold.lty=c(1,2), 
    threshold.lwd=c(1,1), 
    threshold.col=c("black","grey"), 
    amplify=TRUE,
    bin.size=1e6,
    chr.den.col=c("darkgreen", "yellow", "red"), 
    signal.col=c("red","green"),
    signal.cex=c(1,1),
    file="jpg",
    dpi=300,
    file.output=TRUE,
    verbose=TRUE
  )
  # 单性状QQ图
  CMplot(
    x,
    plot.type="q",
    conf.int.col=NULL,
    box=TRUE,
    file="jpg",
    dpi=300,
    file.output=TRUE,
    verbose=TRUE
  )
  # 多性状QQ图
  CMplot(
    x,
    plot.type="q",
    col=c("dodgerblue1", "olivedrab3", "darkgoldenrod1"),
    threshold=1e6,
    signal.pch=19,
    signal.cex=1.5,
    signal.col="red",
    conf.int.col="grey",
    box=FALSE,
    multracks=TRUE,
    file="jpg",
    dpi=300,
    file.output=TRUE,
    verbose=TRUE
  )
  
