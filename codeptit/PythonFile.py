s = input()
size = len(s)
ext = s[size-3] + s[size-2] + s[size-1]
ext = ext.lower()
if(ext == ".py"):
	print("yes")
else:
	print("no")