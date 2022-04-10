/* -----------------------------------------------------------------------------
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
----------------------------------------------------------------------------- */

// get 'POPCLIP_FULL_TEXT' value from environment vars obj
const inputString = Deno.env.get("POPCLIP_FULL_TEXT").toLowerCase();

const output = {
    text: "",
    currentChar: "",
    // track number of consecutive same case to prevent > 3 in a row same case
    numConsecutiveLower: 0,
    numConsecutiveUpper: 0,
    addChar(charCase) {
        if (charCase == 'upper') {
            this.text += this.currentChar.toUpperCase();
            this.numConsecutiveUpper += 1
            this.numConsecutiveLower = 0
        } else {
            this.text += this.currentChar
            this.numConsecutiveLower += 1
            this.numConsecutiveUpper = 0
        }
    },
}

for (const char of inputString) {
    output.currentChar = char;
    if (char == 'i') {
        output.addChar('lower')
    } else if (char == 'l') {
        output.addChar('upper')
    } else if (output.numConsecutiveUpper == 3) {
        output.addChar('lower')
    } else if (output.numConsecutiveLower == 3) {
        output.addChar('upper')
    } else {
        const randomTrueOrFalse = Math.random() >= 0.5;
        if (randomTrueOrFalse) {
            output.addChar('lower')
        } else {
            output.addChar('upper')
        }
    }
}

// using console.log() adds \n after paste. so must write to stdout instead
import { writeAll } from "https://deno.land/std/streams/conversion.ts";
const text = new TextEncoder().encode(output.text);
await writeAll(Deno.stdout, text);