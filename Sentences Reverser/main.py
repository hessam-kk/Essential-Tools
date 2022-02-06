x = ''

fi = ''
fin = open('1.txt', encoding="utf8")

lines = fin.readlines()
fout = open('2.txt', 'a', encoding="utf8")

for line in lines:
    lin = line.split()
    sen = ''
    for i in lin[::-1]:
        print(i)
        sen += i + ' '
    fout.write(sen+'\n')
