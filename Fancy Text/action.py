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
previewString = inputString[:20] + '...'

# -------------------------------------------------------------------------------

option1_compare = '𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ01234567890'
option2_compare = '𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅01234567890'
option3_compare = '𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏𝒜𝐵𝒞𝒟𝐸𝐹𝒢𝐻𝐼𝒥𝒦𝐿𝑀𝒩𝒪𝒫𝒬𝑅𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢'
option4_compare = '𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩01234567890'
option5_compare = '𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘'
option6_compare = 'ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ０１２３４５６７８９０'
option7_compare = 'ꪖ᥇ᥴᦔꫀᠻᧁꫝ꠸꠹ᛕꪶꪑꪀꪮρꪇ᥅ᦓꪻꪊꪜ᭙᥊ꪗƺꪖ᥇ᥴᦔꫀᠻᧁꫝ꠸꠹ᛕꪶꪑꪀꪮρꪇ᥅ᦓꪻꪊꪜ᭙᥊ꪗƺᦲ᧒ᒿᗱᔰƼᦆᒣᲖၦᦲ'
option8_compare = 'ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘQʀꜱᴛᴜᴠᴡxʏᴢᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘQʀꜱᴛᴜᴠᴡxʏᴢ01234567890'
# option9_compare = 'a⃣   b⃣   c⃣   d⃣   e⃣   f⃣   g⃣   h⃣   i⃣   j⃣   k⃣   l⃣   m⃣   n⃣   o⃣   p⃣   q⃣   r⃣   s⃣   t⃣   u⃣   v⃣   w⃣   x⃣   y⃣   z⃣   A⃣   B⃣   C⃣   D⃣   E⃣   F⃣   G⃣   H⃣   I⃣   J⃣   K⃣   L⃣   M⃣   N⃣   O⃣   P⃣   Q⃣   R⃣   S⃣   T⃣   U⃣   V⃣   W⃣   X⃣   Y⃣   Z⃣   0⃣   1⃣   2⃣   3⃣   4⃣   5⃣   6⃣   7⃣   8⃣   9⃣   0⃣'
# option10_compare = 'a⃞    b⃞    c⃞    d⃞    e⃞    f⃞    g⃞    h⃞    i⃞    j⃞    k⃞    l⃞    m⃞    n⃞    o⃞    p⃞    q⃞    r⃞    s⃞    t⃞    u⃞    v⃞    w⃞    x⃞    y⃞    z⃞    A⃞    B⃞    C⃞    D⃞    E⃞    F⃞    G⃞    H⃞    I⃞    J⃞    K⃞    L⃞    M⃞    N⃞    O⃞    P⃞    Q⃞    R⃞    S⃞    T⃞    U⃞    V⃞    W⃞    X⃞    Y⃞    Z⃞    0⃞    1⃞    2⃞    3⃞    4⃞    5⃞    6⃞    7⃞    8⃞    9⃞    0⃞'
option11_compare = '🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉01234567890'
option12_compare = '🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉01234567890'
option13_compare = 'ₐbcdₑfgₕᵢⱼₖₗₘₙₒₚqᵣₛₜᵤᵥwₓyzₐBCDₑFGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥWₓYZ₀₁₂₃₄₅₆₇₈₉₀'
option14_compare = 'ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖqʳˢᵗᵘᵛʷˣʸᶻᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁰'
option15_compare = 'ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ⓪①②③④⑤⑥⑦⑧⑨⓪'
option16_compare = 'ₐbcdₑfgₕᵢⱼₖₗₘₙₒₚqᵣₛₜᵤᵥwₓyzₐBCDₑFGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥWₓYZ₀₁₂₃₄₅₆₇₈₉₀'
option17_compare = '𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝟎'
option18_compare = '𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵𝟬'
option19_compare = '𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡01234567890'
option20_compare = '𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕01234567890'
option21_compare = '𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿𝟶'
option22_compare = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890'
option23_compare = 'ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ０１２３４５６７８９０'

options = [option1_compare, option2_compare, option3_compare, option4_compare, option5_compare, 
option6_compare, option7_compare, option8_compare, # option9_compare, option10_compare, 
option11_compare, option12_compare, option13_compare, option14_compare, option15_compare, 
option16_compare, option17_compare, option18_compare, option19_compare, option20_compare, 
option21_compare, option22_compare, option23_compare]

# -------------------------------------------------------------------------------

def convert_char(char, option_compare):
    base_compare = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890'
    index_track = 0
    for compare_char in base_compare:
        # skip character from base_compare if doesn't match
        if char != compare_char:
            pass
        else:
            return option_compare[index_track]
        index_track += 1
    return char
                
def convert_text(option_compare, inputstring):
    temp_string = ''
    for char in inputstring:
        temp_char = ''
        temp_char = convert_char(char, option_compare)
        temp_string += temp_char
    return temp_string

# -------------------------------------------------------------------------------

import tkinter as tk

class Application(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.title('Fancy Text')
		x_pad = 10
		y_pad = 10


		lbl_1 = tk.Label(self)
		lbl_2 = tk.Label(self)
		lbl_3 = tk.Label(self)
		lbl_4 = tk.Label(self)
		lbl_5 = tk.Label(self)
		lbl_6 = tk.Label(self)
		lbl_7 = tk.Label(self)
		lbl_8 = tk.Label(self)
		# lbl_9 = tk.Label(self)
		# lbl_10 = tk.Label(self)
		lbl_11 = tk.Label(self)
		lbl_12 = tk.Label(self)
		lbl_13 = tk.Label(self)
		lbl_14 = tk.Label(self)
		lbl_15 = tk.Label(self)
		lbl_16 = tk.Label(self)
		lbl_17 = tk.Label(self)
		lbl_18 = tk.Label(self)
		lbl_19 = tk.Label(self)
		lbl_20 = tk.Label(self)
		lbl_21 = tk.Label(self)
		lbl_22 = tk.Label(self)
		lbl_23 = tk.Label(self)

		labels = [lbl_1, lbl_2, lbl_3, lbl_4, lbl_5, lbl_6, lbl_7, lbl_8, # lbl_9, lbl_10, 
		lbl_11, lbl_12, 
		lbl_13, lbl_14, lbl_15, lbl_16, lbl_17, lbl_18, lbl_19, lbl_20, lbl_21, lbl_22, lbl_23]

		for label in labels:
			label.config(text=convert_text(options[labels.index(label)], previewString), font=("Arial",12))
			label.grid(column=1, row=labels.index(label), padx=x_pad, pady=(0, y_pad))

		lbl_1.grid(pady=y_pad)


		btn_1 = tk.Button(self, command=lambda : clicked(options[0], inputString))
		btn_2 = tk.Button(self, command=lambda : clicked(options[1], inputString))
		btn_3 = tk.Button(self, command=lambda : clicked(options[2], inputString))
		btn_4 = tk.Button(self, command=lambda : clicked(options[3], inputString))
		btn_5 = tk.Button(self, command=lambda : clicked(options[4], inputString))
		btn_6 = tk.Button(self, command=lambda : clicked(options[5], inputString))
		btn_7 = tk.Button(self, command=lambda : clicked(options[6], inputString))
		btn_8 = tk.Button(self, command=lambda : clicked(options[7], inputString))
		# btn_9 = tk.Button(self, command=lambda : clicked(options[0], inputString))
		# btn_10 = tk.Button(self, command=lambda : clicked(options[0], inputString))
		btn_11 = tk.Button(self, command=lambda : clicked(options[8], inputString))
		btn_12 = tk.Button(self, command=lambda : clicked(options[9], inputString))
		btn_13 = tk.Button(self, command=lambda : clicked(options[10], inputString))
		btn_14 = tk.Button(self, command=lambda : clicked(options[11], inputString))
		btn_15 = tk.Button(self, command=lambda : clicked(options[12], inputString))
		btn_16 = tk.Button(self, command=lambda : clicked(options[13], inputString))
		btn_17 = tk.Button(self, command=lambda : clicked(options[14], inputString))
		btn_18 = tk.Button(self, command=lambda : clicked(options[15], inputString))
		btn_19 = tk.Button(self, command=lambda : clicked(options[16], inputString))
		btn_20 = tk.Button(self, command=lambda : clicked(options[17], inputString))
		btn_21 = tk.Button(self, command=lambda : clicked(options[18], inputString))
		btn_22 = tk.Button(self, command=lambda : clicked(options[19], inputString))
		btn_23 = tk.Button(self, command=lambda : clicked(options[20], inputString))

		buttons = [btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, # btn_9, btn_10, 
		btn_11, btn_12, 
		btn_13, btn_14, btn_15, btn_16, btn_17, btn_18, btn_19, btn_20, btn_21, btn_22, btn_23]

		def clicked(option_compare, inputStr):
			outputString = convert_text(option_compare, inputStr)
			print(outputString)
			quit()

		for button in buttons:
			button.config(text="Use", font=("Arial",12))
			button.grid(column=2, row=buttons.index(button), padx=x_pad, pady=(0, y_pad))

		btn_1.grid(pady=y_pad)


app = Application()
app.mainloop()
