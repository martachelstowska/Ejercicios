nombre=input("Introduce tu nombre:")

edad=input("Edad:")
edad=int(edad)
if edad >=18:
    print("!Hola," +" " +nombre +" " +"¿Como va todo?")
    print("Eres mayor de edad")
else:
    print("!Hola," +nombre +"¿Como va todo?")
    print("Eres menor de edad")
