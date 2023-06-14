from .pagespeedinsightperformance import pagespeedperf as psp

def run_test(uri):
    output = {
        "pagespeedinsightperf": None
    }

    # PAGESPEED INSIGHT PERFOMANCE ----------------------------------------------- #

    print("\'PageSpeed Insight PERFORMANCE\' test started.")

    psp_out = psp.test(uri)
    output['pagespeedinsightperf'] = {
        "score": int(psp_out['lighthouseResult']['categories']['performance']['score'] * 100),
        "n_audits": len(psp_out['lighthouseResult']['categories']['performance']['auditRefs'])
    }
            
    print("Test ended.\n")

    # ---------------------------------------------------------------------------- #

    return output