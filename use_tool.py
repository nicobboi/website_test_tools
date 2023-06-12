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
#   PageSpeed Insight: performance score, number of audits, ... (TODO)
def performanceTest(uri):
    import tools.performance.pagespeedinsight.pagespeed as pg

    print("Executing \'PageSpeed Insight\' as performance test...\n")

    # PAGESPEED INSIGHT
    output = pg.test(uri)
    n_audit = len(output['lighthouseResult']['categories']['performance']['auditRefs'])
    score = output['lighthouseResult']['categories']['performance']['score'] * 100
    print("Score: " + str(score) + ".\nTotal number of audits done: " + str(n_audit) + ".\n")
            
    print("Performance test ended.\n")


# Runs the accessibility test (Mauve++) and prints the desired output
# OUTPUT:
#   Mauve++: ...
def accessibilityTest(uri):
    import os
    mauve_path = "./tools/accessibility/mauve/index.js"
    mauve_json = "mauve-earl-reporthttps___www.comune.novellara.re.it_.json"

    #with subprocess.Popen(["node", mauve_path, uri]) as proc:
     #   proc.wait()

    with open("./output/" + mauve_json, "r+") as f:
        res = f.read()
        #print(res[-6])
        f_size = os.stat("/home/nico/Scrivania/website_test_tools/output/mauve-earl-reporthttps___www.comune.novellara.re.it_.json").st_size
        f.seek(f_size - 6)
        print(f.read())
        #f.write(f_size - 6)
        # TODO: eliminare quella virgola :(

    #with open("./output/mauve-earl-reporthttps___www.comune.novellara.re.it_.json", "r") as f:
     #   output= json.load(f)

def validationTest(uri):
    print("Test " + uri)

def SEOTest(uri):
    print("Test " + uri)


# Main module
if __name__ == "__main__":
    main()
