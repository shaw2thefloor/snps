from wikitools import wiki, category, page


def snpedia_lookup(snp):

    site = wiki.Wiki("http://bots.snpedia.com/api.php")
    snp = snp['snp']
    pagehandle = page.Page(site, snp)
    snp_page = pagehandle.getWikiText()

    return snp_page