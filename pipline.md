#提取信息

vim extrat.awk
```shell
#!/usr/bin/env awk

BEGIN {
    FS = "\t"
    OFS = "\t"
    header_row = 2692
    output_file = "/mnt/huangchang/huangchang/04_sheep/01_horned_polled/horned_polled_extracted.vcf"
    print "The data has been successfully written into " output_file > "/dev/stderr"
}

NR <= header_row {
    next
}

{
    print $1, $2, $3, $4, $5, $6, $7, $8, $9, $20, $21, $22, $23, $24, $25, $26, $27, $28, $29, $30, $31, $32, $136, $137, $138, $139, $140, $141, $142, $143, $144, $145, $146, $147, $148, $149, $326, $327, $328, $329, $330, $331, $332, $333, $334, $335, $336, $360, $361, $362, $363, $364, $365, $366, $367, $368, $369, $370, $420, $421, $422, $423, $424, $425, $426, $427, $428, $429, $430, $431, $432, $433, $434, $435, $436, $437, $438, $439, $440, $441, $442, $443, $444, $445, $402, $403, $404, $405, $406, $407, $408, $409, $498, $499, $500, $501, $502, $117, $118, $119, $120, $121, $122, $123, $124, $125, $126, $127, $128, $129, $130, $131, $132, $133, $134, $135, $53, $54, $55, $56, $57, $58, $59, $60, $61, $62, $63, $64, $65, $66, $67, $539, $540, $541, $542, $543, $544, $545, $546, $547, $548, $549, $550, $551, $484, $485, $486, $487, $488, $489, $490, $491, $492, $493, $494, $495, $496, $497, $222, $223, $224, $225, $226, $227, $228, $229, $230, $231, $68, $69, $70, $71, $72, $73, $74, $75, $76, $77, $187, $188, $189, $190, $191, $192, $193, $194, $195, $196, $197, $198, $199, $200, $201, $202, $203, $204, $205, $206, $212, $213, $214, $215, $216, $217, $218, $219, $220, $221, $232, $233, $234, $235, $236, $237, $238, $239, $240, $241, $242, $243, $248, $249, $250, $251, $252, $253, $254, $255, $256, $257, $271, $272, $273, $274, $275, $276, $277, $278, $279, $280, $281, $282, $283, $284, $285, $337, $338, $339, $340, $341, $342, $343, $344, $345, $346, $347, $348, $349, $389, $390, $391, $392, $393, $394, $410, $411, $412, $413, $414, $415, $416, $417, $418, $419, $446, $447, $448, $449, $450, $451, $452, $453, $454, $455, $461, $462, $463, $464, $465, $466, $467, $468, $469, $470, $509, $510, $511, $512, $513, $514, $515, $516, $552, $553, $554, $555, $556, $557, $558, $559, $560, $561 > output_file
}
```
awk -f extract.awk DP3miss0.2.recode.vcf

#将vcf文件转换为plink的ped和map格式 
```shell
plink --vcf hp_extracted.vcf --recode --out hp_e --const-fid --allow-extra-chr
```

#将ped和map转换为bed、bim、fam格式
```shell
plink --allow-extra-chr --file hp_e --noweb --make-bed --out hp_e  
```

#进行PCA计算
```shell
plink --allow-extra-chr --threads 20 -bfile hp_e --pca 20 --out hp_e
```
```R
    install.packages("FactoMineR")
    install.packages("factoextra")
    library(FactoMineR)
    library(factoextra)
    library(ggplot2)
    data <- read.csv("C:/Users/Admin/Desktop/待办/sheep analysis/PCA.csv",header = T)
    setwd("C:/Users/Admin/Desktop/待办/sheep analysis/")
    data3 <- data[,-1]
    data2 <- as.data.frame(data3)
    pdf("SNP_test_pca.pdf",width = 30, height = 30)
    ggplot(data2, aes(x=data$PC1, y=data$PC2, color=data$IID)) + 
      geom_point(shape=19, size=2) + 
      scale_shape_manual(values=c(1:8)) + 
      labs(title="PCA", x="PC1", y="PC2") + 
      theme(plot.title = element_text(hjust = 0.5)) 
    dev.off()

    #add labels to everyone plot
    adata <- read.csv("C:/Users/Admin/Desktop/待办/sheep analysis/PCA_geti.csv",header = T)
    adata3 <- adata[,-1]
    adata2 <- as.data.frame(adata3)
    pdf("SNP_test_pca_test.pdf", width = 50, height = 50)
    ggplot(data2, aes(x=adata$PC1, y=adata$PC2, color=adata$IID)) +
      geom_point(shape=19, size=2) +
      scale_shape_manual(values=c(1:8)) +
      geom_text(aes(label=adata$IID), hjust=-0.2, vjust=0.2, size=3) +  # 添加标签
      labs(title="PCA", x="PC1", y="PC2") +
      theme(plot.title = element_text(hjust = 0.5))
    dev.off()
```
#admixture analysis
    #染色体必须是整数
    ```shell
     less hp_extracted.vcf | grep -v "#" |awk '{print $1}' |sort -u |awk '{print $1"\tChr"NR}' > chr_name_change.txt

                less your.vcf|grep -v "#" |awk '{print $1}' |sort -u |awk '{print $1"\tChr"NR}' >chr_name_change.txt #生成染色体名称转化表,我的原本染色体名称类似：Chr01A,在这里只改成了Chr1
                vim chr_name_change.txt #我希望把Chr1改成Chr01，但是不知道怎么写代码，只好手动添加
                 
                bcftools annotate --rename-chrs chr_name_change.txt your.vcf > chrname_change.vcf #admixture要求染色体名称只能为整数，而plink在处理形如CHR01的染色体时会自动替换为1，但有些染色体格式如CHR01A则不能转化，因此先使用bcftools进行格式转换。
                 
                plink --vcf chrname_change.vcf  --make-bed --out snp_indel  --allow-extra-chr --keep-allele-order --set-missing-var-ids @:# --chr-set 70 #plink转化为bed格式
                 
                seq 2 6 | awk '{print "admixture --cv -j2 snp_indel.bed "$1" 1>admix."$1".log 2>&1"}' > admixture.sh 
                 
                #在vi编辑器下输入
                %s/^/nohup /
                %s/$/ \&/
                 
                sh admixture.sh 
                ps -aux |grep admixture
                https://blog.csdn.net/weixin_52269481/article/details/130351775

for K in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20; do admixture --cv hp_e.bed $K | tee log${K}.out; done

  
grep -h CV log*.out
        ```
```R
tbl=read.table("hapmap3.3.Q")

pdf("/USER/XXX/Project/xj/reseq/result/11.admixture/Q7.pdf")

barplot(t(as.matrix(tbl)), col=rainbow(3),xlab="Individual #", ylab="Ancestry", border=NA) 

dev.off()
```


#Use phylip software plot NJ tree
```shell
step1
  download tassel software
step2 
  #vcf转换为phylip格式
      run_pipeline.pl -Xms1G -Xmx1024G  \
    -importGuess  hp_extracted.vcf  \
    -ExportPlugin \
    -saveAs sequences.phy \
    -format Phylip_Inter
step3
 #生成dnadist需要的配置文件
      echo -e "sequences.phy\nY" > dnadist.cfg

#运行dnadist生成距离矩阵文件
      dnadist < dnadist.cfg  >dnadist.log

#生成neighbor程序需要的配置文件
    mv outfile infile.dist
    echo -e "infile.dist\nY"  > neighbor.cfg

#构建nj树
    neighbor  <  neighbor.cfg  >nj.log

#整理结果格式
    less infile.dist | tr '\n' '|'| sed 's/| / /g' | tr '|' '\n' >infile.dist.table
    less outtree | tr '\n' ' '|sed 's/ //g' > outtree.nwk
#整理结果格式
less infile.dist | tr '\n' '|'| sed 's/| / /g' | tr '|' '\n' >infile.dist.table
less outtree | tr '\n' ' '|sed 's/ //g' > outtree.nwk
```
链接：https://zhuanlan.zhihu.com/p/574616718

