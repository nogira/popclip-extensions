set prevClipboard to (the clipboard)
set inputString to "{popclip text}"

set outputString to do shell script "echo \"" & inputString & "\" | python -c \"
import sys
import random as rand
inputString = sys.stdin.read()
outputString = ''

for char in inputString:
	if rand.randint(0,1) == 0:
		outputString += char
	else:
		outputString += char.upper()

print outputString
\""

set the clipboard to outputString

tell application "System Events"
	keystroke "v" using command down
end tell

set the clipboard to prevClipboard