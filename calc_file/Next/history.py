#В файле history.py должна быть описана вся работа со списком истории и загрузкой и выгрузкой их в файл.
def history(a,b,c,d,abs_file_path,my_count):
	import datetime
	now = datetime.datetime.now()										#получить дату и время
	f_log=open(abs_file_path,'a')										#открыть файл log.txt
	s=str(now.strftime("%d.%m.%Y %H:%M:%S"))+" (строка " + str(my_count)+"): число " + str(a)
	if c=="^" or c =="**":
		s = s + " было возведено в степень "
	elif c=="*":
		s = s + " было умножено на "
	elif c=="/":
		s = s + " было разделено на "
	elif c=="+":
		s = s + " было сложено с "
	s = s + str(b) + "; результат: " + str(d)
	if c=="-":
		s=str(now.strftime("%d.%m.%Y %H:%M:%S"))+": число " + str(b) + " было отнято от " + str(a) + "; результат: " + str(d)
	f_log.write(s+chr(10))												#результат обработки добавить к содержимому файла log.txt
	f_log.close()														#закрыть файл log.txt
	return s