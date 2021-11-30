# ------------------------------------------------------------------------------
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
# ------------------------------------------------------------------------------
#
# credit to https://github.com/tinytamb/popclip-sqlparse for how to
# retrieve the selected text to process
#
# ------------------------------------------------------------------------------

# import sys
# # get absolute path of folder this file is in
# # current_dir = os.path.dirname(os.path.abspath(__file__))
# # sys.path.append(str(current_dir) + '/lib')
# # HMMMMMM actually i think i can just get the first entry in sys.path and its 
# # the same
# # append path to sys.path so able to access the python module within the lib 
# # folder
# sys.path.append(sys.path[0] + '/lib')

import os, random

# get 'POPCLIP_TEXT' value from os.environ dict, else return empty string
input_string = os.environ.get('POPCLIP_TEXT', '').lower()

output_string = ''
# track number of consecutive same case to prevent > 3 in a row same case
num_consecutive_lower = 0
num_consecutive_upper = 0

def add_char(case):
    global output_string
    global num_consecutive_lower
    global num_consecutive_upper
    if case == 'upper':
        output_string += char.upper()
        num_consecutive_upper += 1
        num_consecutive_lower = 0
    else:
        output_string += char
        num_consecutive_lower += 1
        num_consecutive_upper = 0

for char in input_string:
    if num_consecutive_upper == 3:
        add_char('lower')
    elif num_consecutive_lower == 3:
        add_char('upper')
    else:
        if random.randint(0,1) == 0:
            add_char('lower')
        else:
            add_char('upper')

# using print adds new line after paste. cannot be fixed with end=''
# copy and paste works instead
import subprocess
subprocess.run('pbcopy', text=True, input=output_string)
subprocess.run('pbpaste')