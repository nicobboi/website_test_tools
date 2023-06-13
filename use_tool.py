import subprocess
import json
import click

@click.command()
@click.argument("uri")
@click.argument("test")
def main(uri, test):
    print("Testing \'" + uri + "\'.\nMode: " + test + ".\n")

    match test:
        case "SECURITY":
            securityTest(uri)
        case "PERFORMANCE":
            performanceTest(uri)
        case "ACCESSIBILITY":
            accessibilityTest(uri)
        case "SEO":
            SEOTest(uri)
        case "VALIDATION":
            validationTest(uri)



# Runs the security tests (ssllabs-scan and shcheck) and prints the desired output
# OUTPUT:
#   shcheck: list of present/missing security headers
#   ssllabs-scan: ssl certificate grade of the website's page
def securityTest(uri):
    shcheck_path = "./tools/security/shcheck/shcheck.py"
    ssllabs_path = "./tools/security/ssllabsscan/ssllabs-scan"
    
    # SHCHECK
    print("Executing \'Security Headers Check\' test... \n")
    with subprocess.Popen([shcheck_path, "-j", uri], stdout=subprocess.PIPE) as proc:
        output = json.loads(proc.stdout.read())
        h_pres = list(output[uri]['present'].keys())
        h_miss = output[uri]['missing']
        print("Headers presenti (" + str(len(h_pres)) + "): " + str(h_pres))
        print("Headers mancanti (" + str(len(h_miss)) + "): " + str(h_miss))
    
    # SSLLABS-SCAN
    print("\nExecuting \'SSL/TLS scan\' test... \n")
    with subprocess.Popen([ssllabs_path, "--verbosity", "error", "--grade", uri], stdout=subprocess.PIPE) as proc:
        output = proc.stdout.read()
        grade = str(output).split(" ")[1][1] #retrieve the grade letter
        print("SSL certificate's grade: " + score_from_grade(grade) + ".\n")

    print("Security test ended.\n")

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


# Runs the performance test (PageSpeed Insight) and prints the desired output
# OUTPUT:
#   PageSpeed Insight: performance score, number of audits, ... (TODO: add more)
def performanceTest(uri):
    import tools.performance.pagespeedinsight.pagespeed as pg

    print("Executing \'PageSpeed Insight\' as performance test...\n")

    # PAGESPEED INSIGHT
    output = pg.test(uri)
    n_audit = len(output['lighthouseResult']['categories']['performance']['auditRefs'])
    score = int(output['lighthouseResult']['categories']['performance']['score'] * 100)
    print("Score: " + str(score) + ".\nTotal number of audits done: " + str(n_audit) + ".\n")
            
    print("Performance test ended.\n")


# Runs the accessibility test (Mauve++) and prints the desired output
# OUTPUT:
#   Mauve++: audits passed compared to total audits + example of an audit
def accessibilityTest(uri):  
    mauve_path = "./tools/accessibility/mauve/index.js"

    print("Executing accessibility test...\n")

    # MAUVE++
    with subprocess.Popen(["node", mauve_path, uri, "./output/mauve_reports"]) as proc:
        proc.wait()

    # example: mauve-earl-reporthttps___www.comune.novellara.re.it
    report_path = "./output/mauve_reports/mauve-earl-report" + [uri, uri.translate(uri.maketrans("://", "___"))]["://" in uri] + ".json"
    # ---------------------------------------------------------------------- #
    # there's an error in the json (",]"), so I manually removed it
    replace_string = ""
    with open(report_path, "r") as f:
        replace_string = f.read()

    replace_string = replace_string.replace(",\n\t]", "\n\t]")
    with open(report_path, "w") as f:
        f.write(replace_string)
    # ---------------------------------------------------------------------- #
    
    with open(report_path, "r") as f:
        output = json.load(f)
        # compute the total number of audit passed compared to total audits
        audits_passed = len([x for x in output['@graph'] if x['earl:result']['dcterms:title'] == "PASS"])
        audits_total = len(output['@graph'])
        audits_passed_perc = int(audits_passed / audits_total * 100)
        print("Total number of audit passed: " + str(audits_passed) + "/" + str(audits_total) + " (" + str(audits_passed_perc) + "%)" + ".\n")

        print("Example audit:")
        print("Test: " + output['@graph'][1]['earl:result']['earl:info'] + ". Status: " + output['@graph'][1]['earl:result']['dcterms:title'] + ".\n")

    print("Accessibility test ended.\n")


# Runs the validation test (pa-website-validator) and prints the desired output
# OUTPUT:
#   pa-website-validator: model compliace score, reccomandations tests score, ... (TODO: add more)
def validationTest(uri):
    pwv_path = "./tools/validation/pa-website-validator/"
    out_fold = "./output/pwv_reports"

    print("Executing validation test...\n")
    with subprocess.Popen(["node", pwv_path + "dist", "--type", "municipality", "--destination", out_fold, "--report", "report", \
                          "--accuracy", "min", "--website", uri], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
        proc.wait()

    with open(out_fold + "/report.json", "r") as f:
        output = json.load(f);
        mc_score = int(output['categories']['modelComplianceInformation']['score'] * 100)
        rt_score = int(output['categories']['reccomandationsAndAdditionalTests']['score'] * 100)
        print("Model compliance score: " + str(mc_score) + ".");
        print("Reccomandations tests score: " + str(rt_score) + ".\n")

    print("Validation test ended.\n")


# Runs the SEO tests (SEOMator tools) and prints the desired output
# OUTPUT:
#   SEOMator tools: ...
def SEOTest(uri):
    import tools.seo.seomator.seomator as seo

    print("Executing SEO test...\n")

    # returns a dict with key=test name and value=result of the test
    output = seo.test(uri)
    for key, val in output.items(): 
        if val != None: 
            print(key + ": " + val + ".")

    print("\nSEO test ended.\n")


# Main module
if __name__ == "__main__":
    main()
