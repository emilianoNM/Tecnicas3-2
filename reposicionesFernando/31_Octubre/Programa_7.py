#Este te muestra el calendario y ademas te da la fecha numerica

import datetime
import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))
Hoy = datetime.datetime.now()
print ("La Fecha y Hora del dia de hoy es: ")
print (Hoy.strftime("%Y-%m-%d %H:%M:%S"))