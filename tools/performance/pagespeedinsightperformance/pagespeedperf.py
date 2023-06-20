import requests, os, json
from datetime import datetime

def test(uri):
    # API's url for the GET request
    url = "https://pagespeedonline.googleapis.com/pagespeedonline/v5/runPagespeed"

    # params to send with the GET request
    params = {
        "category": "PERFORMANCE",
        "url": uri,
    }

    # request to PageSpeed Insight and returns a JSON
    res = requests.get(url, params=params)
    output = res.json()

    reports_dir = os.path.dirname(__file__) + "/reports"

    # if not exists, creates the output folder for reports
    if not os.path.exists(reports_dir):
        os.mkdir(reports_dir)

    # saves the report in a JSON
    output_file = reports_dir + "/report__" + datetime.now().strftime("%d%m%Y_%H%M%S") + "__.json"
    with open(output_file, "w") as f:
        json.dump(output, f, indent=4)

    # return directly the content of the JSON and the path of the report file
    return output, output_file

