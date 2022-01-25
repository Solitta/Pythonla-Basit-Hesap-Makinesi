num1 = int(input('Birinci sayıyı giriniz: '))
num2 =int(input('İkinci sayıyı giriniz: '))
 
op = input('Bir işlem seçiniz(+, -, *, /): ')

if op == '+':
  print(num1 + num2)

if op == '*':
  print(num1 * num2)

if op == '-':
  print(num1 - num2)

if op == '/':
  print(num1 / num2)
else:
  print('Programımızda böyle bir işlem yok kardeşim')