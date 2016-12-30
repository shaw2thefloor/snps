from lib.snps_util import snpedia_lookup
import json


# function to create mock snp data
# TODO - need to liase with PI about the exact format we will recieve
def make_snps_data():
    d = list()
    d.append({'gene': 'ADIPOQ', 'snp': 'rs17300539', 'variant': 'GG'})
    # d.append(('ANKK1', 'rs1800497', 'TT'))
    # d.append(('FTO', 'rs11076022', 'GG'))
    return d


def test_snpedia_lookup():
    data = make_snps_data()
    for t in data:
        output = snpedia_lookup(t)
        assert output != ''
        json_version = json.loads(output)

