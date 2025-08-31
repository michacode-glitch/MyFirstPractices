import datetime
print("*******************************")
print("**   Bienvenido a la pagina  **")
print("********  de CarRent  *********")
print("*******************************")

print("Ingrese su nombre completo")
nombre = input()
print(f"Bienvenido {nombre}!!")

try:
    print("¿Sos mayor de edad?\nResponda con -si- o -no-")
    edad = input("").lower().strip()

    if edad == "no":
        print("Lo sentimos, necesitas ser mayor de edad")
        exit()
    elif edad == "si":
        print("Perfecto.\nNecesitamos verificar su fecha de nacimiento")
        while True:
            fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd-mm-aaaa): ")
            try:
                # Intenta convertir la fecha, si falla pide de nuevo
                fecha_obj = datetime.datetime.strptime(fecha_nacimiento, "%d-%m-%Y")
                
                # Checkea si realmente tiene 18 o más

                today = datetime.date.today()
                birth_date = fecha_obj.date()
                edad = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

                if edad >= 18:
                    print("Fecha verificada. Puede seguir con la compra\n")
                    break

                else:
                    print("Lo sentimos, tenes que ser mayor de 18 años para continuar.")
                    exit()

            except ValueError:
                print("Formato inválido. Por favor, ingrese la fecha en formato dd-mm-aaaa.")
    else:
        print("Ingrese una respuesta valida (si/no)")
        exit ()

except Exception as e:
    print(f"Error inesperado {e}")
    exit()

print("A continuacion apareceran los tipos autos de renta disponibles en este momento.")
print("Tipos de autos:\n-Tipo sport\n-Tipo comfort")

try:
    print("Ahora eliga que tipo de auto prefiere escribiendo: 1 para tipo sport y 2 para comfort;")
        
    inp = int(input())

    if inp == 1: 

        print("Genial, te gustan los autos rapidos y furiosos... guiño guiño")
        print("A continuacion seleccione que auto quiere alquilar:")
        
        try:

            print("Escriba debajo la letra correspondiente:")
            print("P - Porshe")
            print("L - Lamborghini")
            print("B - Bugatti")
            print("Escriba aqui: ", end="")

            inp2 = input().upper().strip() #convertir a uppercase y remover espacios

            
            
            if inp2 in ("P", "L", "B"):
                car_names = {"P": "Porshe", "L": "Lamborghini", "B": "Bugatti"}
                print(f"Felicitaciones! Ha seleccionado un {car_names[inp2]}")
                print("Gracias por comprar en CarRent!!")
            else:
                print("Ingrese una letra valida(P/L/B)")
                exit ()

        except ValueError:
            print("Ingrese una letra valida.")
            
    elif inp == 2:

        print("Perfecto usted prefiere un auto comodo y espacioso")
        print("A continuacion seleccione que auto quiere alquilar:")
        
        
        try:

            print("Escriba debajo la letra correspondiente:")
            print("A - Amarok")
            print("B - Bronco")
            print("J - Jeep")
            print("Escriba aqui: ", end="")

            inp3 = input().upper().strip()

            if inp3 in ("A", "B", "J"):
                suv_name = {"A": "Amarok", "B": "Bronco", "J": "Jeep"}
                print(f"Felicitaciones usted ha finalizado la compra de su {suv_name[inp3]}")
                print("Gracias por comprar en CarRent!!")
            else:
                print("Ingrese una letra valida(A/B/J)")
                exit ()
        except Exception as e:
            print("De una respuesta valida")
            exit()        

    else:
        print("Eliga un numero valido")

except Exception as e:
        print("Por favor! Seleccione un numero del 1 al 2")



























