SSL Labs APIs expose the complete SSL/TLS server testing functionality in a programmatic fashion, allowing for scheduled and bulk assessment.
This tool is a command-line client for the SSL Labs APIs.

Usage: `ssllabs-scan [options] <URI>` 

Example for JSON output with only grade: `./ssllabs-scan --grade --json-flat <URI> > ../../../Output/sslabs-scan_out.json`

Check the below github page for full option list.

[SSL Labs site](https://www.ssllabs.com/projects/ssllabs-apis/index.html)
[CLI Github](https://github.com/ssllabs/ssllabs-scan/)