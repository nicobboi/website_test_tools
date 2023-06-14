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
        "seo_score": seo_score,
        "n_audits": n_audits,
        "is_robots_txt_valid": robot_valid,
    }

    print("Test ended\n")

    # ------------------------------------------------------------------------------- #

    # ROBOT PARSER ------------------------------------------------------------------ #    

    print("\'Robot parser\' test started.")
    output["robot_parser"] = rp.test(uri)
    print("Test ended\n")

    # ------------------------------------------------------------------------------- #

    return output
