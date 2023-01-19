persona = int(input("Digite su edad: "))

if persona >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

def libros(a):
    if a == 'Laura':
        print("Hola Laura")
    else:
        print("No eres Laura")
    if a == 'Santiago':
        print("Hola Santiago")
    else:
        print("No eres Santiago")
    return

libros(a='jose')