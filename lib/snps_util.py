from scrape import genotype, snp
from xlrd import open_workbook


def read_snp_excel_file(filename):
    wb = open_workbook(filename)
    sheet = wb.sheet_by_index(0)

    genes = list()
    rs_refs = list()
    samples = list()

    for i in range(0, sheet.nrows):
        sample = ()
        for j in range(1, sheet.ncols):
            # check for gene names
            if i == 0:
                genes.append(sheet.cell(i, j).value)
            # check for rs_ref
            elif i == 1:
                rs_refs.append(sheet.cell(i, j).value)
            else:
                sample = sample + (sheet.cell(i, j).value,)
        if i > 1:
            samples.append(sample)

    return {'genes': genes, 'rs_refs': rs_refs, 'samples': samples}


def snpedia_lookup(snp_data):
    s = snp_data['snp']
    v = snp_data['variant']
    resp = snp(s, v)

    return resp
