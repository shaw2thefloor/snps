from scrape import genotype, snp
from xlrd import open_workbook

'''
Function used xlrd library to load and scrape excel workbooks
'''
def read_snp_excel_file(filename):
    # open book and get first sheet
    wb = open_workbook(filename)
    sheet = wb.sheet_by_index(0)
    # init some lists
    genes = list()
    rs_refs = list()
    samples = list()
    
    # now do a doubly nested loop to scan through the matrix
    for i in range(0, sheet.nrows):
        # each row is either a list of gene names, a list of associated rs_refs or a list of snp variant for a sample
        sample = ()
        # start from 1 as the first column is a label column
        for j in range(1, sheet.ncols):
            # if we are on the first row, we are scanning gene names
            if i == 0:
                genes.append(sheet.cell(i, j).value)
            # if we are on the second row we are scanning rs_refs
            elif i == 1:
                rs_refs.append(sheet.cell(i, j).value)
            # else we are scanning a sample's snp variants
            else:
                sample = sample + (sheet.cell(i, j).value,)
        if i > 1:
            samples.append(sample)

    return {'genes': genes, 'rs_refs': rs_refs, 'samples': samples}

'''
Function to lookup variant in snpedia - from https://github.com/leaena/snp-api
'''
def snpedia_lookup(snp_data):
    s = snp_data['snp']
    v = snp_data['variant']
    resp = snp(s, v)

    return resp
