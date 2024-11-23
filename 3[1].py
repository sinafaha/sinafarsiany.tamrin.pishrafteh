import turtle
import turtle as t
n = int(input("Enter n:"))
x_axis = 0
y_axis = 0
if n%4 in (0,1):
    x_axis = -1
else:
    x_axis = 1
if n%4 in (0,3):
    y_axis = 1
else:
    y_axis = -1
if n%4 in (0,1):
    x_axis *= n//4
else:
    x_axis = n//4 + 1
if n%4 in (0,3):
    y_axis = round(n/4)
else:
    y_axis *= n//4