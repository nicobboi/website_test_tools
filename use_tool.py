from time import time
import sys
import click

# Script to test tools's outputs and to print them

# global list to stores all reports which will be sent to db 
run_reports = []

@click.command()
@click.argument("uri")
@click.argument("test_type")
def main(uri, test_type):
    print("Testing \'" + uri + "\'.\nMode: " + test_type + ".\n")

    tests = [
        securityTest,
        performanceTest,
        accessibilityTest,
        SEOTest,
        validationTest,
    ]

    t_start = int(time())
    match test_type:
        case "SECURITY":
            tests[0](uri)
        case "PERFORMANCE":
            tests[1](uri)
        case "ACCESSIBILITY":
            tests[2](uri)
        case "SEO":
            tests[3](uri)
        case "VALIDATION":
            tests[4](uri)
        case "ALL":
            for test in tests:
                test(uri)
        case "TEST":
            Test(uri)
        case _:
            return print("Test type not valid.")
    t_end = int(time())
    t_elapsed = t_end - t_start

    pushToDB(uri)

    print("Elapsed time: ~" + [str(int((t_elapsed) / 60)) + " min", str(t_elapsed) + "s"][t_elapsed < 60] + ".\n")

# ALL TEST OUTPUT ARE DICT (use keys() to check the tools used for that output)

# Runs the security tests (ssllabs-scan and shcheck) and prints the desired output
def securityTest(uri):
    import tools.security.securitytest as securitytest

    print("Executing SECURITY test... \n")
    
    security_output = securitytest.run_test(uri)
    #print(security_output)

    addToReport("security", security_output)

    print("Security test ended.\n")


# Runs the performance test (PageSpeed Insight) and prints the desired output
# OUTPUT:
#   PageSpeed Insight: performance score, number of audits, ... (TODO: add more)
def performanceTest(uri):
    import tools.performance.performancetest as performancetest

    print("Executing PERFORMANCE test...\n")

    performance_output = performancetest.run_test(uri)
    #print(performance_output)

    addToReport("performance", performance_output)

    print("Performance test ended.\n")
    

# Runs the accessibility test (Mauve++) and prints the desired output
def accessibilityTest(uri):  
    import tools.accessibility.accessibilitytest as accessibilitytest

    print("Executing ACCESSIBILITY test.\n")

    accessibility_out = accessibilitytest.run_test(uri)
    #print(accessibility_out)

    addToReport("accessibility", accessibility_out)

    print("Accessibility test ended.\n")


# Runs the validation test (pa-website-validator) and prints the desired output
# OUTPUT:
#   pa-website-validator: model compliace score, reccomandations tests score, ... (TODO: add more)
def validationTest(uri):
    import tools.validation.validationtest as validationtest

    print("Executing VALIDATION test...\n")

    validation_out = validationtest.run_test(uri)
    #print(validation_out)

    addToReport("validation", validation_out)

    print("Validation test ended.\n")


# Runs the SEO tests and prints the output
def SEOTest(uri):
    import tools.seo.seotest as seotest

    print("Executing SEO test...\n")

    # returns a dict with key=test name and value=result of the test
    seo_output = seotest.run_test(uri)
    #print(seo_output)

    addToReport("seo", seo_output)

    print("SEO test ended.\n")


# TEST FUNCTION to send data into the db 
def Test(uri):
    print("Test API!")

    output = {
        "test_tool6": {
            'scores': {
                'score_1': 89,
                'score_2': 13
            },
            'notes': "Stringhe con note.",
            'json_report': None
        } 
    }

    addToReport("test_type", output)



# add the report in the global list of reports
def addToReport(type, output):
    for tool in output:
        out = output[tool]

        run_reports.append({
            'type': type,
            'tool': tool,
            'scores': out['scores'],
            'notes': out['notes'],
            'json_report': out['json_report']
        })

# Push a test result into the database using the custom API
def pushToDB(url):
    import requests

    payload = {
        'url': url,
        'reports': run_reports
    }

    try:
        # api request to send report's data into the database
        res = requests.post("http://localhost:8000/saveReport", json=payload)
    except requests.exceptions.ConnectionError:
        print("Connection error.\nShutting down...")
        sys.exit(1)
    finally:
        run_reports.clear()



# Main module
if __name__ == "__main__":
    main()
