#清除环境变量
rm(list=ls())
#读取数据
data <- read.table("yourfile")
#查看数据结构
head(data)

#install.packages("ggplot2")
library(ggplot2)

ggplot(pca_result, aes(x = PC1, y = PC2, color = IID)) +
  geom_point() +
  labs(x = "PC1", y = "PC2", color = "Sample") +
  geom_hline(yintercept = 0,lty=2,col="red") + 
  geom_vline(xintercept = 0,lty=2,col="blue", lwd =1 ) +
  theme_bw() +
  theme(legend.position = "none") #删除图例
