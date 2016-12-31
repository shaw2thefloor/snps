from lib.snps_util import snpedia_lookup
import json


# function to create mock snp data
# TODO - need to liase with PI about the exact format we will recieve
def make_snps_data():
    d = list()
    d.append({'gene': 'ADIPOQ', 'snp': 'rs17300539', 'variant': 'GG'})
    d.append({'gene': 'ANKK1', 'snp': 'rs1800497', 'variant':'TT'})
    d.append({'gene': 'FTO', 'snp': 'rs11076022', 'variant': 'GG'})
    return d


def test_snpedia_lookup():
    data = make_snps_data()
    for t in data:
        output = snpedia_lookup(t)
        assert output != ''
        print("output is: " + str(output))
        #json_version = json.loads(output)

