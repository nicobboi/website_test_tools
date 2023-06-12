import requests
import html_to_json
import json
import click

@click.command()
@click.argument("uri")
@click.argument("tool_id")
def main(uri, tool_id):
    # Costruisco url con id tool e sito da controllare
    url = "https://free-seo-tools.seomator.com/tool.php?id=" + tool_id + "&site=" + uri

    # GET request verso il tool
    res = requests.get(url)
    # Converto l'html in JSON
    out_json = html_to_json.convert(res.text, capture_element_attributes=False)
    
    # Stampo output
    with open("../../../Output/SEOMATOR/" + tool_id + "_out.json", "w") as f:
        json.dump(out_json, f, indent=2)

if __name__ == "__main__":
    main()