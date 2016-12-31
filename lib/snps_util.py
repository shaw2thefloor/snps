from scrape import genotype, snp

def snpedia_lookup(snp_data):
    s = snp_data['snp']
    v = snp_data['variant']
    resp = snp(s, v)

    return resp


