from time import time
import click

# Script to test tools's outputs and to print them

@click.command()
@click.argument("uri")
@click.argument("test")
def main(uri, test):
    print("Testing \'" + uri + "\'.\nMode: " + test + ".\n")

    tests = [
        securityTest,
        performanceTest,
        accessibilityTest,
        SEOTest,
        validationTest
    ]

    t_start = int(time())
    match test:
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
    t_end = int(time())
    t_elapsed = t_end - t_start

    print("Elapsed time: ~" + [str(int((t_elapsed) / 60)) + " min", str(t_elapsed) + "s"][t_elapsed < 60] + ".\n")

# ALL TEST OUTPUT ARE DICT (use keys() to check the tools used for that output)

# Runs the security tests (ssllabs-scan and shcheck) and prints the desired output
def securityTest(uri):
    import tools.security.securitytest as securitytest

    print("Executing SECURITY test... \n")
    
    security_output = securitytest.run_test(uri)
    print(security_output)

    print("\nSecurity test ended.\n")


# Runs the performance test (PageSpeed Insight) and prints the desired output
# OUTPUT:
#   PageSpeed Insight: performance score, number of audits, ... (TODO: add more)
def performanceTest(uri):
    import tools.performance.performancetest as performancetest

    print("Executing PERFORMANCE test...\n")

    performance_output = performancetest.run_test(uri)
    print(performance_output)

    print("\nPerformance test ended.\n")
    

# Runs the accessibility test (Mauve++) and prints the desired output
def accessibilityTest(uri):  
    import tools.accessibility.accessibilitytest as accessibilitytest

    print("Executing ACCESSIBILITY test.\n")

    accessibility_out = accessibilitytest.run_test(uri)
    print(accessibility_out)

    print("\nAccessibility test ended.\n")


# Runs the validation test (pa-website-validator) and prints the desired output
# OUTPUT:
#   pa-website-validator: model compliace score, reccomandations tests score, ... (TODO: add more)
def validationTest(uri):
    import tools.validation.validationtest as validationtest

    print("Executing VALIDATION test...\n")

    validation_out = validationtest.run_test(uri)
    print(validation_out)

    print("\nValidation test ended.\n")


# Runs the SEO tests and prints the output
def SEOTest(uri):
    import tools.seo.seotest as seotest

    print("Executing SEO test...\n")

    # returns a dict with key=test name and value=result of the test
    seo_output = seotest.run_test(uri)
    print(seo_output)

    print("\nSEO test ended.\n")


# Main module
if __name__ == "__main__":
    main()
