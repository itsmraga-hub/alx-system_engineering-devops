#!/usr/bin/python3
"""
  Python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
   body = response.read()
   print(body)

