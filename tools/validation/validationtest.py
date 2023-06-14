from subprocess import Popen, PIPE
import json
import os
import inspect

def run_test(uri):
    output = {
        "pa-website-validator": None
    }

    script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 

    # PA-WEBSITE-VALIDATOR ------------------------------------------------------- #

    pwv_path = script_dir + "/pa-website-validator/"
    out_fold = script_dir + "/pa-website-validator/reports/"

    print("\'pa-website-validator\' test started.")

    with Popen(["node", pwv_path + "dist", "--type", "municipality", "--destination", out_fold, "--report", "report", \
                          "--accuracy", "min", "--website", uri], stdout=PIPE, stderr=PIPE) as proc:
        proc.wait()

    with open(out_fold + "report.json", "r") as f:
        pwt_out = json.load(f)
        output["pa-website-validator"] = {
            "mc_score": int(pwt_out['categories']['modelComplianceInformation']['score'] * 100),
            "rt_score": int(pwt_out['categories']['reccomandationsAndAdditionalTests']['score'] * 100)
        }

    print("Test ended.\n")

    # ---------------------------------------------------------------------------- #

    return output