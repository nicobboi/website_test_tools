from time import time
import sys
import click

# Script to test tools's outputs and to print them

@click.command()
@click.argument("uri")
@click.argument("test_type")
@click.argument("test_name")
def main(uri, test_type, test_name):
    print("Testing \'" + uri + "\'.\nMode: " + test_type + ".\n")

    tests = [
        securityTest,
        performanceTest,
        accessibilityTest,
        SEOTest,
        validationTest
    ]

    t_start = int(time())
    match test_type:
        case "SECURITY":
            tests[0](uri, test_name)
        case "PERFORMANCE":
            tests[1](uri, test_name)
        case "ACCESSIBILITY":
            tests[2](uri, test_name)
        case "SEO":
            tests[3](uri, test_name)
        case "VALIDATION":
            tests[4](uri, test_name)
        case "ALL":
            for test in tests:
                test(uri, test_name)
        case _:
            return print("Test type not valid.")
    t_end = int(time())
    t_elapsed = t_end - t_start

    print("Elapsed time: ~" + [str(int((t_elapsed) / 60)) + " min", str(t_elapsed) + "s"][t_elapsed < 60] + ".\n")

# ALL TEST OUTPUT ARE DICT (use keys() to check the tools used for that output)

# Runs the security tests (ssllabs-scan and shcheck) and prints the desired output
def securityTest(uri, test_name):
    import tools.security.securitytest as securitytest

    print("Executing SECURITY test... \n")
    
    security_output = securitytest.run_test(uri)
    #print(security_output)

    pushToDB(test_name, uri, "security", security_output)

    print("Security test ended.\n")


# Runs the performance test (PageSpeed Insight) and prints the desired output
# OUTPUT:
#   PageSpeed Insight: performance score, number of audits, ... (TODO: add more)
def performanceTest(uri, test_name):
    import tools.performance.performancetest as performancetest

    print("Executing PERFORMANCE test...\n")

    performance_output = performancetest.run_test(uri)
    #print(performance_output)

    pushToDB(test_name, uri, "performance", performance_output)

    print("Performance test ended.\n")
    

# Runs the accessibility test (Mauve++) and prints the desired output
def accessibilityTest(uri, test_name):  
    import tools.accessibility.accessibilitytest as accessibilitytest

    print("Executing ACCESSIBILITY test.\n")

    accessibility_out = accessibilitytest.run_test(uri)
    #print(accessibility_out)

    pushToDB(test_name, uri, "accessibility", accessibility_out)

    print("Accessibility test ended.\n")


# Runs the validation test (pa-website-validator) and prints the desired output
# OUTPUT:
#   pa-website-validator: model compliace score, reccomandations tests score, ... (TODO: add more)
def validationTest(uri, test_name):
    import tools.validation.validationtest as validationtest

    print("Executing VALIDATION test...\n")

    validation_out = validationtest.run_test(uri)
    #print(validation_out)

    pushToDB(test_name, uri, "validation", validation_out)

    print("Validation test ended.\n")


# Runs the SEO tests and prints the output
def SEOTest(uri, test_name):
    import tools.seo.seotest as seotest

    print("Executing SEO test...\n")

    # returns a dict with key=test name and value=result of the test
    seo_output = seotest.run_test(uri)
    #print(seo_output)

    pushToDB(test_name, uri, "seo", seo_output)

    print("SEO test ended.\n")


# Push a test result into the database using the custom API
def pushToDB(name, url, type, output):
    import requests

    for tool in output:
        out = output[tool]
        payload = {
            "name": name,
            "url": url,
            "type": type,
            "tool": tool,
            "stats": out['stats'],
            "notes": out['notes'],
            "documents": out['documents']
        }

        try:
            # api request to send report's data into the database
            res = requests.post("http://localhost:8000/saveReport", json=payload)
        except requests.exceptions.ConnectionError:
            print("Connection error.\nShutting down...")
            sys.exit(1)

        

# Main module
if __name__ == "__main__":
    main()
