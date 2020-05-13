import pyperclip
text=pyperclip.paste()
lines=text.split("\n")
for i in range(len(lines)):
    lines[i]='*'+lines[i]
text='\n'.joint(lines)
pyperclip.copy(text)