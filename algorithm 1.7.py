# 7. По длинам трех отрезков, введенных пользователем, определить возможность
# существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он
# разносторонним, равнобедренным или равносторонним.
while True:
   a = input('Введите сторону треугольника')
   b = input('Введите сторону треугольника')
   c = input('Введите сторону треугольника')
   if a < b + c and b < a + c and c < b + c:
      print('Существование треугольника возможно')
   else:
      print('Треугольник не может существовать')
      break
   if a == b and b == c:
      print('Треугольник является равносторонним')
   elif a != b and b != c:
      print('Треугольник разносторонний')
   else:
      print('Треугольник равнобедренный')

