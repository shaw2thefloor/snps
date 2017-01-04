'''
This is a pytest file. Make sure the dependencies are installed, navigate to this directory in a terminal and type 'pytest test_sample.py'
PyTest will automatically discover and run functions prefixed with 'test_'
'''

from lib.snps_util import snpedia_lookup, read_snp_excel_file

# function to create mock snp data
def make_snps_data():
    d = list()
    d.append({'gene': 'ADIPOQ', 'snp': 'rs17300539', 'variant': 'GG'})
    d.append({'gene': 'ANKK1', 'snp': 'rs1800497', 'variant': 'TT'})
    d.append({'gene': 'FTO', 'snp': 'rs11076022', 'variant': 'GG'})
    return d


def test_excel_file_load():
    d = read_snp_excel_file('test_data/ExampleSNPTable_vsmall.xlsx')
    assert 'genes' in d
    assert 'rs_refs' in d
    assert 'samples' in d

# main test of util functions
def test_snpedia_lookup():
    
    data = read_snp_excel_file('test_data/ExampleSNPTable_vsmall.xlsx')

    for sample in data['samples']:
        print(sample)
        for idx in range(0, len(sample)):
            d = {'gene': data['genes'][idx], 'snp': data['rs_refs'][idx], 'variant': sample[idx]}

            output = snpedia_lookup(d)
            print("output is: " + str(output))
            assert type(output) == type(dict())
            assert len(output) > 0
            
