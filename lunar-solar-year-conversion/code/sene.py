def lunar_to_solar(x):
    return round((x*354)/365)

def solar_to_lunar(x):
    return round((x*365)/354)
    
print('Ay takviminden güneş takvimine sene dönüşümü için 1')
print('Güneş takviminden ay takvimine sene dönüşümü için 2')
secim = int(input('Seçiminizi giriniz: '))
sene = int(input('Kaç sene? '))
if (secim == 1):
    print('%i ay senesi = %i güneş senesi' %(sene, lunar_to_solar(sene)))
elif (secim == 2):
    print('%i güneş senesi = %i ay senesi' %(sene, solar_to_lunar(sene)))
