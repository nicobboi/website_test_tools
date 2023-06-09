import requests
import json
import click

@click.command()
@click.argument("uri")
def main(uri):
    url = "https://pagespeedonline.googleapis.com/pagespeedonline/v5/runPagespeed"

    params = {
        "category": "PERFORMANCE",
        "url": uri,
    }

    res = requests.get(url, params=params)
    with open("../../../Output/pagespeed_out.json", "w") as f:
       json.dump(res.json(), f, indent=2)

if __name__== "__main__":
    main()

