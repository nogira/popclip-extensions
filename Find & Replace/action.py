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
# -------------------------------------------------------------------------------

import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(str(current_dir) + '/lib')
inputString = os.environ.get('POPCLIP_TEXT', '')

import tkinter as tk

class Application(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.title('Find & Replace')
		x_pad = 10
		y_pad = 10

		the_font = ("Arial",12)

		find_lbl = tk.Label(self)
		find_lbl.config(text="Find", font=the_font)
		find_lbl.grid(column=1, row=1, padx=(x_pad, 0), pady=y_pad)

		find_textbox = tk.Entry(self)
		find_textbox.grid(column=2, row=1, padx=x_pad, pady=y_pad)
		

		replace_lbl = tk.Label(self)
		replace_lbl.config(text="Replace", font=the_font)
		replace_lbl.grid(column=1, row=2, padx=(x_pad, 0), pady=0)

		replace_textbox = tk.Entry(self)
		replace_textbox.config()
		replace_textbox.grid(column=2, row=2, padx=x_pad, pady=0)


		find_lbl.grid(pady=y_pad)


		def clicked():
			
			find = find_textbox.get()\
						.replace("\\t", "\t")\
						.replace("\\n", "\n")
			replace = replace_textbox.get()\
						.replace("\\t", "\t")\
						.replace("\\n", "\n")

			# modify input by replacing find term with replace term
			output = inputString.replace(find, replace)

			# using print adds a new line after pasting, and this cannot be 
			# fixed with end='', but using copy/paste works
			import subprocess
			subprocess.run("pbcopy", text=True, input=output)
			subprocess.run("pbpaste")
			
			quit()

		done_btn = tk.Button(self, command=clicked)
		done_btn.config(text="Replace All", font=the_font)
		done_btn.grid(column=2, row=3, padx=x_pad, pady=y_pad)


app = Application()
app.mainloop()