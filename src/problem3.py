# Definición de la función verificar_avion que realiza la verificación de variables del motor.
def verificar_avion(temp_aceite, presion_aceite, gases_escape, bomba_vacio, instrumentos_motor):
    #####   AQUÍ VA SU CÓDIGO   #####
    #Reemplace el comando pass con el código de su solución
    pass


###################################
#De aquí en adelante NO MODIFICAR
###################################

def main():
    # Solicitar datos al usuario para las variables del motor.
    temp_aceite = float(input("Ingrese la temperatura de aceite (°F): "))
    presion_aceite = float(input("Ingrese la presión de aceite (psi): "))
    gases_escape = float(input("Ingrese los gases de escape (°F): "))
    bomba_vacio = float(input("Ingrese la bomba de vacío (pulgadas de Hg): "))
    instrumentos_motor = input("¿Todos los instrumentos del motor están operativos? (Sí/No): ")

    # Llamar a la función verificar_avion con los datos ingresados y mostrar el mensaje resultante.
    mensaje = verificar_avion(temp_aceite, presion_aceite, gases_escape, bomba_vacio, instrumentos_motor)
    print(mensaje)

if __name__ == '__main__':
    main()
