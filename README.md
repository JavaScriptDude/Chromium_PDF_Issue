## Chromium PDF Issue
[UPDATE] - This issue has been resolve: https://bugs.chromium.org/p/chromedriver/issues/detail?id=3517

Test Code to Illustrate Issue with `Page.printToPDF` in Chromium


Illustration of issue where Chromium cannot generate PDF calling `Page.printToPDF` with `headless=False`

Test Dependencies:
* Python:
```python3
python3 -m pip install selenium==4.1.3
```
* `chromedriver`:
 Download and place or create symlink to chromedriver  in same directory. See [chromedriver.chromium.org](http://chromedriver.chromium.org/ ).

Note: This issue has been reproduced using Puppeteer, Pyppeteer, Deno Puppeteer and Selenium.

Error returned from inspector when `headless=False`:
```
{"code":-32000, "message": "Printing is not available"}
```
