vim extract.py

import multiprocessing
import pandas as pd

def extract_columns(df, columns):
    extracted_data = df[columns]
    return extracted_data

if __name__ == '__main__':
    # Read file
    df = pd.read_csv('output.vcf', delimiter='\t', skiprows=2692)

    # Define the columns to extract
    columns_to_extract = ['#CHROM', 'POS', 'ID', 'REF', 'QUAL', 'FILTER', 'INFO', 'FORMAT']

    # Define the additional columns
    #有角9
    alt_columns = [col for col in df.columns if 'ALT' in col]
    ...
    btb_columns = [col for col in df.columns if 'BTB' in col]
    #无角19
    auw_columns = [col for col in df.columns if 'AUW' in col]
    ...
    wag_columns = [col for col in df.columns if 'WAG' in col]

    # Combine all columns
    columns_to_extract += alt_columns + byb_columns + meh_columns + oul_columns + ssf_columns + sth_columns + sno_columns + thf_columns + btb_columns + auw_columns + wad_columns + tec_columns + efd_columns + bam_columns + dop_columns + dor_columns + dul_columns + fin_columns + got_columns + hus_columns + lpb_columns + mep_columns + rom_columns + sol_columns + suk_columns + suw_columns + txl_columns + wag_columns

    # Split the columns into chunks for parallel processing
    num_processes = multiprocessing.cpu_count()
    chunk_size = len(columns_to_extract) // num_processes
    column_chunks = [columns_to_extract[i:i+chunk_size] for i in range(0, len(columns_to_extract), chunk_size)]

    # Create a pool of processes
    pool = multiprocessing.Pool(processes=num_processes)

    # Apply the extract_columns function to each chunk of columns
    results = []
    for chunk in column_chunks:
        result = pool.apply_async(extract_columns, args=(df, chunk))
        results.append(result)

    # Get the extracted data from the results
    extracted_data = [result.get() for result in results]

    # Merge the extracted data from different processes
    merged_data = pd.concat(extracted_data, axis=1)

    # Write the merged data into a new file
    merged_data.to_csv('mul_extracted.vcf', sep='\t', index=False)

    print("The data has been successfully written into horned_polled_extracted.vcf")
