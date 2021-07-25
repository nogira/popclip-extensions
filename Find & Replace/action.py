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

import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(str(current_dir) + '/lib')
inputString = os.environ.get('POPCLIP_TEXT', '')


import tkinter as tk

class Application(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.title('Fancy Text')
		x_pad = 10
		y_pad = 10


		lbl_1 = tk.Label(self)
		lbl_1.config(text="Find", font=("Arial",12))
		lbl_1.grid(column=1, row=1, padx=(x_pad, 0), pady=y_pad)

		text_box1 = tk.Entry(self)
		text_box1.config()
		text_box1.grid(column=2, row=1, padx=x_pad, pady=y_pad)
		

		lbl_2 = tk.Label(self)
		lbl_2.config(text="Replace", font=("Arial",12))
		lbl_2.grid(column=1, row=2, padx=(x_pad, 0), pady=0)

		text_box2 = tk.Entry(self)
		text_box2.config()
		text_box2.grid(column=2, row=2, padx=x_pad, pady=0)


		lbl_1.grid(pady=y_pad)


		def clicked():
			
			find = text_box1.get()\
				.replace("\\t", "\t")\
				.replace("\\n", "\n")
			replace = text_box2.get()\
				.replace("\\t", "\t")\
				.replace("\\n", "\n")

			# using print adds a new line after pasting, and this cannot be fixed with end='', but this works
			import subprocess
			subprocess.run("pbcopy", text=True, input=inputString.replace(find, replace))
			subprocess.run("pbpaste")
			
			quit()

		btn_1 = tk.Button(self, command=lambda : clicked())
		btn_1.config(text="Replace All", font=("Arial",12))
		btn_1.grid(column=2, row=3, padx=x_pad, pady=(0, y_pad))




		btn_1.grid(pady=y_pad)


app = Application()
app.mainloop()