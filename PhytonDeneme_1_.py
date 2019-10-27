Vize = int(input('Sınav notunuzu giriniz:'))
Final = int(input('Sınav notunuzu giriniz:'))
notunuz = (Vize + Final) / 2

print(notunuz)

if int(notunuz)>50:
    print('Tebrikler geçtiniz')
else:
    print('Maalesef kaldınız')
