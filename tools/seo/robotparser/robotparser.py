import requests
import urllib.robotparser

# Checks if the given URI is crawlable (following the robots.txt rules) 
# and if there's at least one sitemap file at the given URI
def test(uri):
    output = {
        "is_crawlable": False,
        "sitemap_present": {
            "present": False,
            "notes": ""
        }
    }

    if uri[-1] != '/':
        uri += '/'

    # robot parser
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(uri + "robots.txt")
    rp.read()

    output['is_url_crawlable'] = rp.can_fetch("*", uri)

    if rp.site_maps() != None:
        output["sitemap_present"]["present"] = True
        output["sitemap_present"]["notes"] = "Sitemap parameter is presents in the robots.txt."
    else:
        output["sitemap_present"]["notes"] = "Sitemap parameter is not presents in the robots.txt!"

        # list of commons sitemap files
        sitemap = [
            "sitemap.xml",
            "sitemap_index.xml",
            "sitemap-index.xml",
            "sitemap.php",
            "sitemap.txt",
            "sitemap.xml.gz",
            "sitemap/",
            "sitemap/sitemap.xml",
            "sitemapindex.xml",
            "sitemap/index.xml",
            "sitemap1.xml",
            "rss/,"
            "rss.xml",
            "atom.xml"
        ]

        for s in sitemap:
            res = requests.get(uri + s)
            if res.status_code == 200:
                output["sitemap_present"]["present"] = True
        
    # TODO: controllare se i siti presenti nella sitemap non sono rotti

    return output    
    
