f = open('iban_lenght.txt')
a = {}
for s in f:
    s = s.split()
    a.update({s[0]: s[1]})
print(a)