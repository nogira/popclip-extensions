set inputString to "{popclip text}"
set inputArray to my theSplit(inputString, "")

on theSplit(theString, theDelimiter)
	-- save delimiters to restore old settings
	set oldDelimiters to AppleScript's text item delimiters
	-- set delimiters to delimiter to be used
	set AppleScript's text item delimiters to theDelimiter
	-- create the array
	set theArray to every text item of theString
	-- restore the old setting
	set AppleScript's text item delimiters to oldDelimiters
	-- return the result
	return theArray
end theSplit


tell application "System Events"
	repeat with char in inputArray
		if char = " " then
			keystroke char
		else if (random number from 0 to 1) = 1 then
			keystroke char
		else
			keystroke char using shift down
		end if
	end repeat
end tell
