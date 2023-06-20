from .pagespeedinsightperformance import pagespeedperf as psp

def run_test(uri):
    output = {
        "pagespeed_performance": None
    }

    # PAGESPEED INSIGHT PERFOMANCE ----------------------------------------------- #

    print("\'PageSpeed Insight PERFORMANCE\' test started.")

    psp_out, psp_report_path = psp.test(uri)

    try:
        output['pagespeed_performance'] = {
            "stats": {
                "score": int(psp_out['lighthouseResult']['categories']['performance']['score'] * 100),
                "n_audits": len(psp_out['lighthouseResult']['categories']['performance']['auditRefs'])
            },
            "notes": {
                "overall_loading_speed": psp_out['loadingExperience']['overall_category'],
            },
            "documents": {
                "json_report": psp_report_path
            }
        }
    except KeyError:
        print("Error on \'PageSpeed Insight (PERFORMANCE)\' test.\n")
        output['pagespeed_performance'] = {
            "stats": None,
            "notes": {
                "info": "An error occured while testing this tool..."
            },
            "documents": None
        }
            
    print("Test ended.\n")

    # ---------------------------------------------------------------------------- #

    return output