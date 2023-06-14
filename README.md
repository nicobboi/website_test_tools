Tool list to operate tests on a page of a website.

Tests and tool list:
  - Accessibility:
      - [Mauve++](https://mauve.isti.cnr.it/)
  - Performance:
      - [PageSpeed Insight](https://developers.google.com/speed/docs/insights/rest/v5/pagespeedapi/runpagespeed?hl=it) (category PERFORMANCE)
  - Security:
      - [SSLlabs-scan](https://www.ssllabs.com/projects/ssllabs-apis/index.html)
      - [shcheck - Security Headers Check](https://github.com/santoru/shcheck)
  - Validation:
      - [pa-website-validator](https://github.com/italia/pa-website-validator)
  - SEO:
      - ~~[SEOMator tools](https://free-seo-tools.seomator.com/)~~
      - PageSpeed Insight (category SEO)
      - [urllib.robotparser](https://docs.python.org/3/library/urllib.robotparser.html)

Setup python virtual environment:
```
python -m venv .
source bin/activate
pip install -r requirements.txt
```
