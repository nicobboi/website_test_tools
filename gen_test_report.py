import tools.accessibility.accessibilitytest as accessibilityt
import tools.performance.performancetest as performancet
import tools.security.securitytest as securityt
import tools.seo.seotest as seot
import tools.validation.validationtest as validationt
import click
import json
from time import time

# Script for generating a report (JSON) for the tools's outputs

@click.command()
@click.argument("uri")
def main(uri):
    print("Starting tests.\n")
    t_start = int(time())

    output = {
        "tested_url": uri,
        "time": None,
        "accessibility": accessibilityt.run_test(uri),
        "performance": performancet.run_test(uri),
        "security": securityt.run_test(uri),
        "seo": seot.run_test(uri),
        "validation": validationt.run_test(uri)
    }

    output["time"] = int(time()) - t_start

    with open("./reports/report.json", "w") as f:
        json.dump(output, f, indent=2)

    print("Test ended with report generated.\n")


if __name__ == "__main__":
    main()