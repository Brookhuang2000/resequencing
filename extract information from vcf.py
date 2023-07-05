#!/usr/bin/env python

import pandas as pd

# Read file
df = pd.read_csv('output.vcf', delimiter='\t', skiprows=2692)

# Extract the required columns.
columns_to_extract = ['#CHROM', 'POS', 'ID', 'REF', 'QUAL', 'FILTER', 'INFO', 'FORMAT']

#有角9
alt_columns = [col for col in df.columns if 'ALT' in col]
byb_columns = [col for col in df.columns if 'BYB' in col]
meh_columns = [col for col in df.columns if 'MEH' in col]
oul_columns = [col for col in df.columns if 'OUL' in col]
ssf_columns = [col for col in df.columns if 'SSF' in col]
sth_columns = [col for col in df.columns if 'STH' in col]
sno_columns = [col for col in df.columns if 'SNO' in col]
thf_columns = [col for col in df.columns if 'THF' in col]
btb_columns = [col for col in df.columns if 'BTB' in col]
#无角19
auw_columns = [col for col in df.columns if 'AUW' in col]
wad_columns = [col for col in df.columns if 'WAD' in col]
tec_columns = [col for col in df.columns if 'TEC' in col]
efd_columns = [col for col in df.columns if 'EFD' in col]
bam_columns = [col for col in df.columns if 'BAM' in col]
dop_columns = [col for col in df.columns if 'DOP' in col]
dor_columns = [col for col in df.columns if 'DOR' in col]
dul_columns = [col for col in df.columns if 'DUL' in col]
fin_columns = [col for col in df.columns if 'FIN' in col]
got_columns = [col for col in df.columns if 'GOT' in col]
hus_columns = [col for col in df.columns if 'HUS' in col]
lpb_columns = [col for col in df.columns if 'LPB' in col]
mep_columns = [col for col in df.columns if 'MEP' in col]
rom_columns = [col for col in df.columns if 'ROM' in col]
sol_columns = [col for col in df.columns if 'SOL' in col]
suk_columns = [col for col in df.columns if 'SUK' in col]
suw_columns = [col for col in df.columns if 'SUW' in col]
txl_columns = [col for col in df.columns if 'TXL' in col]
wag_columns = [col for col in df.columns if 'WAG' in col]

columns_to_extract += alt_columns + byb_columns + meh_columns + oul_columns + ssf_columns + sth_columns + sno_columns + thf_columns + btb_columns + auw_columns + wad_columns + tec_columns + efd_columns + bam_columns + dop_columns + dor_columns + dul_columns + fin_columns + got_columns + hus_columns + lpb_columns + mep_columns + rom_columns + sol_columns + suk_columns + suw_columns + txl_columns + wag_columns

extracted_data = df[columns_to_extract]

# Write the extracted data into a new file.
extracted_data.to_csv('3result.vcf', sep='\t', index=False)

print("数据已成功写入 3result.vcf 文件。")

