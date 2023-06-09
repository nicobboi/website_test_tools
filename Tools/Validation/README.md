Desktop app that test the overall quality of institutional websites of Schools/Municipalities and if 
they are following the 'PNRR Esperienza del cittadino nei servizi pubblici digitali' policies.
[Criteria list](https://docs.italia.it/italia/designers-italia/app-valutazione-modelli-docs/it/versione-attuale/index.html)

### Local installation
```
clone the repo (SSH: git@github.com:italia/pa-website-validator.git)
npm install
```

Usage: `node dist [options] --type <type> --destination <folder> --report <name> --website <URI>`

Example: `node dist --type municipality --destination ../../../Output/pa-website-validator_out --report pa-website-validator_out --accuracy min --website https://www.comune.novellara.re.it/`

Check the below github page for full option list.

[Full doc](https://github.com/italia/pa-website-validator)