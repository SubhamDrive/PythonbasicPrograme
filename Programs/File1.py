myfile = open('MyFile.txt','r+')
print('Name:',myfile.name)
text=myfile.read()
print(text)
myfile.close()

