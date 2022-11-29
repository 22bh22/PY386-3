#Задача №3795. Принадлежит ли точка области
#https://informatics.msk.ru/mod/statements/view3.php?id=3962&chapterid=3795#1
#Проверьте, принадлежит ли точка данной закрашенной области:
#Если точка принадлежит области (область включает границы), выведите слово YES, иначе выведите слово NO.
#Решение должно содержать функцию IsPointInArea(x, y), возвращающую True, если точка принадлежит области и False, если не принадлежит.
#Основная программа должна считать координаты точки, вызвать функцию IsPointInArea и в зависимости от возвращенного значения вывести на экран необходимое сообщение.
#Функция IsPointInArea не должна содержать инструкцию if.
#
#Входные данные
#Вводится два действительных числа.
#
#Выходные данные
#Выведите ответ на задачу.
def IsPointInArea(x,y):
	return (y >=2*x+2)*(y>=-x)*((x+1)**2*(y-1)**2<=4)+(y<=2*x+2)*(y<=-x)*((x+1)**2*(y-1)**2>=4)
x=int(input("Введите координату X точки: "))
y=int(input("Введите координату Y точки: "))
if IsPointInArea(x,y)==1:
	print("YES!")
else:
	print("NO")
input("Для завершения нажмите любую клавишу...")