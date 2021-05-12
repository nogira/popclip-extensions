# -------------------------------------------------------------------------------
#
# MIT License
#
# Copyright (c) 2021 nogira
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# -------------------------------------------------------------------------------
#
# credit to https://github.com/tinytamb/popclip-sqlparse for how to
# retrieve the selected text to process
#
# https://stackoverflow.com/questions/4302027/how-to-open-a-url-in-python#4302041
# https://stackoverflow.com/questions/24153519/how-to-read-html-from-a-url-in-python-3
# https://www.tutorialspoint.com/python_text_processing/python_extract_url_from_text.htm
#
# -------------------------------------------------------------------------------

import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(str(current_dir) + '/lib')
inputString = os.environ.get('POPCLIP_TEXT', '')

import urllib.request
html = urllib.request.urlopen("https://sci-hub-links.com").read().decode("utf8")

import re
urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', html)

scihuburls = []
for link in urls:
	if 'sci-hub' in link:
		scihuburls.append(link)

import random as rand
scihuburl = scihuburls[rand.randint(0,len(scihuburls))]

import webbrowser  
webbrowser.open(scihuburl + "/" + inputString, new=0, autoraise=True)