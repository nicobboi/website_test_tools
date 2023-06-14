from subprocess import Popen, PIPE
import json
import os
import inspect

# Runs all SECURITY tool tests and return a dict with all the desired output
def run_test(uri):
    output = {
        "sh-check": None,
        "ssllabs-scan": None
    }

    script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 
    
    # SHCHECK -------------------------------------------------------------------- #

    shcheck_path = script_dir + "/shcheck/shcheck.py"

    print("\'Security headers check\' test started.")
    with Popen([shcheck_path, "-j", uri], stdout=PIPE) as proc:
        shcheck_out = json.loads(proc.stdout.read())
        output["sh-check"] = {
            "h_pres": list(shcheck_out[uri]['present'].keys()),
            "h_miss": shcheck_out[uri]['missing']
        }
    
    print("Test ended.\n")

    # ---------------------------------------------------------------------------- #
    
    # SSLLABS-SCAN --------------------------------------------------------------- #

    ssllabs_path = script_dir + "/ssllabsscan/ssllabs-scan"

    print("\'SSLlabs-scan\' test started.")
    with Popen([ssllabs_path, "--verbosity", "error", "--grade", uri], stdout=PIPE) as proc:
        ssllabs_scan_out = proc.stdout.read()
        output["ssllabs-scan"] = {
            "grade": score_from_grade(str(ssllabs_scan_out).split(" ")[1][1]) #retrieve the grade letter
        }

    print("Test ended.\n")
    # ----------------------------------------------------------------------------- #

    return output

# returns the correspondig score from the given grade
def score_from_grade(grade):
    score = "0"
    match grade:
        case 'A':
            score = "A, score >= 80"
        case 'B':
            score = "B, score >= 65"
        case 'C':
            score = "C, score >= 50"
        case 'D':
            score = "D, score >= 35"
        case 'E':
            score = "E, score >= 20"
        case 'F':
            score = "F, score < 20"
            
    return score
