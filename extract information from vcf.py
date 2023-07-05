#!/usr/bin/env python

import pandas as pd

# 读取文件
df = pd.read_csv('output.vcf', delimiter='\t', skiprows=2692)

# 提取所需的列
columns_to_extract = ['#CHROM', 'POS', 'ID', 'REF', 'QUAL', 'FILTER', 'INFO', 'FORMAT']

alt_columns = [col for col in df.columns if 'ALT' in col]
byb_columns = [col for col in df.columns if 'BYB' in col]

columns_to_extract += alt_columns + byb_columns

extracted_data = df[columns_to_extract]

# 将提取的数据写入新文件
extracted_data.to_csv('3result.vcf', sep='\t', index=False)

print("数据已成功写入 3result.vcf 文件。")

