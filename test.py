# test.py - Illustration of issue where Chromium cannot generate PDF using Page.printToPDF
#           when headless=False
# python3 -m pip install selenium==4.1.3
# Download and place or create symlink to chromedriver in same directory
#    See: http://chromedriver.chromium.org/ 
# Author: Timothy.c.quinn@gmail.com (https://github.com/JavaScriptDude)
# License: MIT
import sys
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json, base64

def main(args):
  url = 'https://www.google.com'
  out = f'z_test_{datetime.now().strftime("%y%m%d-%H%M%S.%f")}.pdf'

  wd_opts = Options()
  # Uncomment this line to avoid error:
  # wd_opts.add_argument('--headless')
  wd_opts.add_argument('--disable-gpu')
  with webdriver.Chrome('./chromedriver', options=wd_opts) as driver:
    driver.get(url)
    result = send_cmd(driver, "Page.printToPDF", params={})
  
  with open(out, 'wb') as file:
    file.write(base64.b64decode(result['data']))

  if not os.path.isfile(f'./{out}'):
    raise Exception(f"PDF WAS NOT GENERATED: ./{out}")

  print(f"PDF Generated - ./{out}")


def send_cmd(driver, cmd, params={}):
  response = driver.command_executor._request(
     'POST'
    ,f"{driver.command_executor._url}/session/{driver.session_id}/chromium/send_command_and_get_result"
    ,json.dumps({'cmd': cmd, 'params': params}))
  if response.get('status'): raise Exception(response.get('value'))
  return response.get('value')


if __name__ == '__main__':
    main(sys.argv[1:])
