a = input(' Введите несколько строк, разделённых пробелом')
st_spli = a.split()
n = 0
cut_a = 0
for text in range(len(st_spli)):
    n += 1
    cut_a = st_spli[text]
    print(f' {n} -ое слово: {cut_a[0:10]}')

