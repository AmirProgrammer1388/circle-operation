import math
import turtle as t
t.shape('turtle')
t.hideturtle()
t.speed('slow')
r = int(t.textinput('Circumference and area of circle','Write the radius'))
A = 2*(math.pi)*r
print("The area of the circle is "+str(math.floor(A)))
S = (math.pi) * (r ** 2)
print("The circumference of the circle is "+str(math.floor(S)))