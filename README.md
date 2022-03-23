## Chromium PDF Issue
Test Code to Illustrate Issue with Page.printToPDF in Chromium


Illustration of issue where Chromium cannot generate PDF using Page.printToPDF `when headless=False`

Install dependencies:
```python3
python3 -m pip install selenium==4.1.3
```

Download and place or create symlink to chromedriver  in same directory. See [chromedriver.chromium.org](http://chromedriver.chromium.org/ ).

Note: This issue has been reproduced using Puppeteer, Pyppeteer, Deno Puppeteer and Selenium.
