try:
    a= int(input(" "))
    b= int(input(" "))
    c= int(input(" "))
    d= (b**2 - 4*a*c)**0.5
    x1= (b-d) / (2*a)
    x2= (b+d) / (2*a)
    print("Первый корень уравнения:", x1,"Второй корень уравнения:",x2)
except Exception:
    print("Введите число")
