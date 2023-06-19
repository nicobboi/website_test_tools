from .pagespeedinsightseo import pagespeedseo as pss
from .robotparser import robotparser as rp 

# Runs all SEO tool tests and return a dict with all the desired output
def run_test(uri):
    # tools's output returned
    output = {
        "pagespeed_seo": None,
        "robot_parser": None
    }

    # PAGESPEED INSIGHT SEO --------------------------------------------------------- #

    print("\'PageSpeed Insight SEO\' test started.")

    # runs pagespeed insight seo test
    pss_out = pss.test(uri)
    
    # organizing pss output 
    seo_score = int(pss_out["lighthouseResult"]["categories"]["seo"]["score"] * 100)
    n_audits = len(pss_out["lighthouseResult"]["categories"]["seo"]["auditRefs"])
    robot_valid = bool(pss_out["lighthouseResult"]["audits"]["robots-txt"]["score"])

    output["pagespeed_seo"] = {
        "stats": {
            "seo_score": seo_score,
            "n_audits": n_audits
        },
        "notes": {
            "is_robots_txt_valid": robot_valid
        },
        "documents": None
    }

    print("Test ended\n")

    # ------------------------------------------------------------------------------- #

    # ROBOT PARSER ------------------------------------------------------------------ #    

    output["robot_parser"] = {
        "stats": None,
        "notes": None,
        "documents": None
    }

    print("\'Robot parser\' test started.")
    if output["pagespeed_seo"]["notes"]["is_robots_txt_valid"]:
        output["robot_parser"]["notes"] = rp.test(uri)
    else:
        output["robot_parser"]["notes"] = "Test not started because robots.txt is not valid!"
    print("Test ended\n")

    # ------------------------------------------------------------------------------- #

    return output
