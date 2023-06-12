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
    
    print("Executing \'Security Headers Check\' test... \n")
    with subprocess.Popen([shcheck_path, "-j", uri], stdout=subprocess.PIPE) as proc:
        output = json.loads(proc.stdout.read())
        #print("Headers presenti: " + str(output[uri]['present']))
        print("Headers mancanti: " + str(output[uri]['missing']))
    
    print("\nExecuting \'SSL/TLS scan\' test... \n")
    with subprocess.Popen([ssllabs_path, "--verbosity", "error", "--grade", uri], stdout=subprocess.PIPE) as proc:
        output = proc.stdout.read()
        grade = str(output).split(" ")[1][1:3]
        print("SSL certificate's grade: " + grade + ".\n")

    print("Security test ended.\n")


# Runs the performance test (PageSpeed Insight) and prints the desired output
# OUTPUT:
#   PageSpeed Insight: ...
def performanceTest(uri):
    import tools.performance.pagespeedinsight.pagespeed as pg

    #psi_path = "./Tools/Performance/PageSpeedInsight/pagespeed.py"

    print("Executing \'PageSpeed Insight\' as performance test...\n")
    output = pg.test(uri)
    n_audit = len(output['lighthouseResult']['categories']['performance']['auditRefs'])
    score = output['lighthouseResult']['categories']['performance']['score'] * 100
    print("Score: " + str(score) + ".\nTotal number of audits done: " + str(n_audit) + ".\n")
    '''
    # per test più veloce
    with open("./Output/psi_output.json", "r") as f:
            output = json.load(f)
            #print(str(output['lighthouseResult']['audits']['speed-index']) + "\n")
            print(str(output['lighthouseResult']['categories']['performance']['score']) + "\n")
    '''
            
    print("Performance test ended.\n")



def accessibilityTest(uri):
    print("Test " + uri)



def validationTest(uri):
    print("Test " + uri)

def SEOTest(uri):
    print("Test " + uri)

if __name__ == "__main__":
    main()
