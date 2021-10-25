skor = [0.0, 0.0, 0.0, 0.0] # initialize ediyoruz
agirlik = [0.4, 0.6]
skor[0] = float(input('Ara sınav notunuzu giriniz: '))
skor[1] = float(input('Final sınavı notunu giriniz: '))
skor[2] = agirlik[0]*skor[0] + agirlik[1]*skor[1]
skor[3] = round(skor[2])
print('Dönem sonu ağırlıklı notunuz %.2f' %skor[2])
print('Yuvarlandıktan sonra %i' %int(skor[3]))
harfNotu = ['AA', 'BA', 'BB', 'CB', 'CC', 'DC', 'DD', 'FD', 'FF']
notGecis = [81, 76, 70, 60, 50, 45, 40, 30]
if skor[3] >= notGecis[0]:
    print('Bu dersten %s aldınız.' %harfNotu[0])
elif skor[3] >= notGecis[1]:
    print('Bu dersten %s aldınız.' %harfNotu[1])
elif skor[3] >= notGecis[2]:
    print('Bu dersten %s aldınız.' %harfNotu[2])
elif skor[3] >= notGecis[3]:
    print('Bu dersten %s aldınız.' %harfNotu[3])
elif skor[3] >= notGecis[4]:
    print('Bu dersten %s aldınız.' %harfNotu[4])
elif skor[3] >= notGecis[5]:
    print('Bu dersten %s aldınız.' %harfNotu[5])
elif skor[3] >= notGecis[6]:
    print('Bu dersten %s aldınız.' %harfNotu[6])
elif skor[3] >= notGecis[7]:
    print('Bu dersten %s aldınız.' %harfNotu[7])
else:
    print('Bu dersten %s aldınız.' %harfNotu[8])
