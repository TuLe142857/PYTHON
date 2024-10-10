def convert(s):
	return s[0].upper() + s[1:].lower()
breakChar = [".", "?", "!"]

s = ""
while(True):
# for i in range(4):
    try:
        s += (" " + input())
    except EOFError:
        break

word = s.split()
i = 0
sentence = ""
while(i < len(word)):
	sentence = ""
	while(i < len(word) and not((word[i])[-1] in breakChar) ):
		sentence += word[i] + " "
		i += 1
	if(i >= len(word)):
		print(sentence[:-1])
		break
	sentence += (word[i])[:-1] + " "
	sentence = convert(sentence)
	print(sentence[:-1])
	i += 1
	



	
	