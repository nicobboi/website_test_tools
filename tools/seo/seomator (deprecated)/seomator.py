import requests
import html_to_json
from bs4 import BeautifulSoup

def test(uri):
    # tests on robots.txt, sitemap, DA, PA (TODO: verificare con test su sito rotto questi tool per effettiva utilita')
    # tool_ids = ["robots-txt", "sitemap", "crawlability", "domain-authority", "page-authority", "headers", "extract-meta-tags", "link-analysis"]

    output = {
        "crawlability": None,
        "authority_values": None
    }

    # Request for all tools
    # robotstxt(uri) -> TODO: utile se controlla robots.txt malfunzionanti(non presenti)
    # sitemap(uri)  -> TODO: come robots.txt ma per sitemap
    output["crawlability"] = crawlability(uri)
    output["authority_values"] = authority_values(uri)

    return output

    
# function to handle crawlability tool's output
# checks if a site is crawlable and/or indexable following the robots.txt rules
# TODO: fare piu' test su come definire se il sito e' crawlable o meno 
def crawlability(uri):
    tool_id = "crawlability"
    url = "https://free-seo-tools.seomator.com/tool.php?id=" + tool_id + "&site=" + uri

    # GET request verso il tool
    res = requests.get(url)
    # Converto l'html in JSON
    out_json = html_to_json.convert_tables(res.text)

    return ["Not crawlable", "Crawlable"][not "cannot crawl" in out_json[0][0]['Info']]

# function to handle domain authority and page authority output
# checks the DA and PA of the site and returns their value
def authority_values(uri):
    tool_id_DA = "domain-authority"
    tool_id_PA = "page-authority"
    url_DA = "https://free-seo-tools.seomator.com/tool.php?id=" + tool_id_DA + "&site=" + uri
    url_PA = "https://free-seo-tools.seomator.com/tool.php?id=" + tool_id_PA + "&site=" + uri

    output = ""

    # DOMAIN AUTHORITY
    res = requests.get(url_DA)
    res_soup = BeautifulSoup(res.text, "html.parser")
    output += "DA: " + res_soup.h3.string + "\t"

    # PAGE AUTHORITY
    res = requests.get(url_PA)
    res_soup = BeautifulSoup(res.text, "html.parser")
    output += "PA: " + res_soup.h3.string

    return output