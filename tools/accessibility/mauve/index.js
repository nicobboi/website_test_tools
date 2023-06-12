const fs = require("fs");
const path = require("path");
const puppeteer = require("puppeteer");
const waitForDownload = require('puppeteer-utilz').waitForDownload;
const url = process.argv[2];

const tmpPath = path.resolve(__dirname + '/tmp');
const downloadPath = path.resolve('./output');
(async () => {
  const browser = await puppeteer.launch({
    headless: "new",  // "new" or "false"
    defaultViewport: false,
    userDataDir: (__dirname + "/user_data"),
    args:[
      '--start-maximized' // you can also use '--start-fullscreen'
   ],
  });

  const page = await browser.newPage();
  await page.goto('https://mauve.isti.cnr.it/singleValidation.jsp');
  await page.type('#uri', url);
  await page.click('#validate');
  const client = page._client();
  await client.send('Page.setDownloadBehavior', {
    behavior: 'allow',
    downloadPath: tmpPath 
  });

  await page.waitForSelector('a[title="download earl report"]');

  await page.click('a[title="download pdf report"]');
  await waitForDownload(tmpPath);
  fs.readdir(tmpPath, function (err, files) {
    if (err) {
        return console.log('Unable to scan directory: ' + err);
    }
    files.forEach(function (file) {
      fs.rename(tmpPath + '/' + file, downloadPath + '/' + file, (err) => {
        if (err) throw err;
      });
    });
  });

  await page.click('a[title="download earl report"]');
  await waitForDownload(tmpPath);
  fs.readdir(tmpPath, function (err, files) {
    if (err) {
        return console.log('Unable to scan directory: ' + err);
    }
    files.forEach(function (file) {
      fs.rename(tmpPath + '/' + file, downloadPath + '/' + file, (err) => {
        if (err) throw err;
      });
    });
  });

  await browser.close();

  /*fs.readdir(downloadPath, function (err, files) {
    if (err) {
        return console.log('Unable to scan directory: ' + err);
    } 
    files.forEach(function (file) {
        console.log(file); 
    });
  });*/
})();
