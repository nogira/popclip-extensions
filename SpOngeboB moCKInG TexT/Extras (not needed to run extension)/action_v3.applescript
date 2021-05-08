set prevClipboard to (the clipboard)
set inputString to "{popclip text}"
set inputArray to characters of inputString
set outputString to ""

tell application "System Events"
	
	repeat with char in inputArray
		
		if (random number from 0 to 1) = 1 then
			set outputString to outputString & char
		else
			set outputString to outputString & (do shell script ("echo " & char & " | tr a-z A-Z;"))
		end if
		
	end repeat
	
	set the clipboard to outputString
	keystroke "v" using command down
	set the clipboard to prevClipboard
	
end tell
