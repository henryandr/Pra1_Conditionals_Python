# Calculadora de Índice de Masa Corporal (IMC) 
def categorizar_imc(peso, estatura, edad):
    #####   AQUÍ VA SU CÓDIGO   #####
    #Reemplace el comando pass con el código de su solución
    pass



###################################
#De aquí en adelante NO MODIFICAR
###################################
def main():
    peso = float(input("Ingresa tu peso en kilogramos: "))
    estatura = float(input("Ingresa tu estatura en metros: "))
    edad = int(input("Ingresa tu edad: "))

    # Llama a la función 'categorizar_imc' y almacena los valores de retorno en las variables 'imc' y 'clasificacion'.
    imc, clasificacion = categorizar_imc(peso, estatura, edad)

    # Imprime los resultados de IMC y clasificación.
    if imc == -1:
        print("No se calcula para menores de edad.")
    else:
        print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")
        print(f"Clasificación de IMC: {clasificacion}")

if __name__ == '__main__':
    main()
