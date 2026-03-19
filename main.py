if __name__ == "__main__":
    from operacionesMatematicas import OperacionesMatematicas
    from holamundo import Mensaje
    from persona import Persona

    print("Hola, esta es la interfaz principal del programa:")
    print("Seleccione una opcion:")        
    print("1. Operaciones Matematicas")
    print("2.Mostrar mensaje")
    print("3.calcular la edad de una persona")
    print("4.calcular area y perimetro de figuras geometricas")
    opcion =int(input("ingresa el numero de la opcion: "))

    if opcion == 1:
        operaciones = OperacionesMatematicas()
        
        a= float(input("Ingresa el primer número: "))
        b= float(input("Ingresa el segundo número: "))
        print("Suma:", operaciones.sumar(a, b))
        print("Resta:", operaciones.restar(a, b))
        print("Multiplicación:", operaciones.multiplicar(a, b))
        try:
            print("División:", operaciones.dividir(a, b))
        except ValueError as e:
            print("Error:", e)
    elif opcion == 2:
        mensaje = Mensaje("Hola Mundo programacion en clase")
        print(mensaje)
   
    elif opcion == 3:
        print("ingresa tu nombre:")
        nombre = input()
        print("ingresa tu año de nacimiento:")
        anio_nacimiento = int(input())
        persona = Persona(nombre, anio_nacimiento, 0) 
        anio_actual = 2026
        edad = persona.calcular_edad(anio_actual)
        print("tu edad es:", persona.calcular_edad(anio_actual))

    elif opcion == 4:    
        print("que figura geometrica deseas calcular?")
        print("1. Cuadrado")
        print("2. Rectangulo") 
        print("3. Triangulo")
        figura = int(input("ingresa el numero de la figura: "))

        if figura == 1:
            from cuadrado import Cuadrado
            print("ingresa el lado del cuadrado:")
            lado = float(input())
            cuadrado = Cuadrado(lado)
            print("area del cuadrado:", cuadrado.area())
            print("perimetro del cuadrado:", cuadrado.perimetro())
        elif figura == 2:
            from rectangulo import Rectangulo
            print("ingresa la base del rectangulo:")
            base = float(input())
            print("ingresa la altura del rectangulo:")
            altura = float(input())
            rectangulo = Rectangulo(base, altura)
            print("area del rectangulo:", rectangulo.area())
            print("perimetro del rectangulo:", rectangulo.perimetro())
        elif figura == 3:
            from triangulo import Triangulo
            print("ingresa la base del triangulo:")
            base = float(input())
            print("ingresa la altura del triangulo:")
            altura = float(input())
            triangulo = Triangulo(base, altura)
            print("area del triangulo:", triangulo.area())
            print("perimetro del triangulo:", triangulo.perimetro())

    else:
        print("Opción no válida. Por                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    favor, elige 1, 2 o 3")