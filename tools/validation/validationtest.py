from subprocess import Popen, PIPE
import json
import os
import inspect

def run_test(uri):
    output = {
        "pa-website-validator": None
    }

    script_dir = os.path.dirname(__file__) 

    # PA-WEBSITE-VALIDATOR ------------------------------------------------------- #

    pwv_path = script_dir + "/pa-website-validator/"
    out_fold = script_dir + "/pa-website-validator/reports/"

    print("\'pa-website-validator\' test started.")

    with Popen(["node", pwv_path + "dist", "--type", "municipality", "--destination", out_fold, "--report", "report", \
                          "--accuracy", "min", "--website", uri], stdout=PIPE, stderr=PIPE) as proc:
        proc.wait()

    with open(out_fold + "report.json", "r") as f:
        pwt_out = json.load(f)

        mc_score = int(pwt_out['categories']['modelComplianceInformation']['score'] * 100)
        rt_score = int(pwt_out['categories']['reccomandationsAndAdditionalTests']['score'] * 100)
        score = int((mc_score*9 + rt_score*1) / 10) # media pesata
        output["pa-website-validator"] = {
            "stats": {
                "score": score,
                "mc_score": mc_score,
                "rt_score": rt_score
            },
            "notes": None,
            "documents": {
                "json_report": out_fold + "report.json",
                "html_report": out_fold + "report.html"
            }
        }

    print("Test ended.\n")

    # ---------------------------------------------------------------------------- #

    return output