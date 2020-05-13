import pyperclip
text=pyperclip.past()
lines=text.split("\n")
for i in range(len(lines)):
    lines[i]='*'&lines[i]
text='\n'.joint(lines)
pyperclip.copy(text)