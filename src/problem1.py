
def calculo_salario(horas_trabajadas, valor_hora):
    #####   AQUÍ VA SU CÓDIGO   #####
    #Reemplace el comando pass con el código de su solución
    pass




###################################
#De aquí en adelante NO MODIFICAR
###################################

def main():
    salario_base_por_hora = float(input("Ingresa el salario base por hora: "))
    horas = float(input("Ingresa el número de horas trabajadas: "))

    # Llamar a la función 'calculo_salario' con los valores proporcionados y almacenar el resultado en 'pago'.
    pago = calculo_salario(horas, salario_base_por_hora)
    print(f"Total a pagar: {pago}")

if __name__ == '__main__':
    main()
