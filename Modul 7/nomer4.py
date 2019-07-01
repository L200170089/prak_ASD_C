import re

wikipedia = open('KEI.html', 'r', encoding='latin1')

text = wikipedia.read()
wikipedia.close()


search = re.findall(r'([w+]+)atdntd([0-9.]+)tdntd([0-9.]+)tdntd([0-9.]+)tdntd([0-9.]+)tdntd([0-9.]+)tdntd([0-9.]+)td', text)

list = []

for i in search
    b = (i[0],float(i[4]))
    list.append(b)

print(list)