# Módulos externos a importar

# Este comentario indica que el código no importará ningún módulo externo,
# lo que significa que el código es independiente y no depende de bibliotecas adicionales.

def calculo_salario(horas_trabajadas, valor_hora):
    # Esta es la definición de una función llamada 'calculo_salario' que toma dos parámetros:
    # 'horas_trabajadas' (horas trabajadas) y 'valor_hora' (salario por hora).

    if horas_trabajadas > 50:
        print("Error: El empleado no puede trabajar más de 50 horas a la semana.")
        # Si las horas trabajadas son más de 50, el código imprime un mensaje de error.
        
    elif horas_trabajadas > 40:
        # Si las horas trabajadas son más de 40 pero no más de 50, se ejecutan los siguientes pasos.

        salario_base = valor_hora * 40
        # Calcular el salario base multiplicando el salario por hora por 40 horas.

        if horas_trabajadas >= 45:
            bono = (valor_hora * 2) * (horas_trabajadas - 40)
            # Si las horas trabajadas son 45 o más, calcular un bono multiplicando el salario por hora por 2
            # y luego multiplicándolo por la diferencia entre las horas trabajadas y 40.

        else:
            bono = (valor_hora * 1.5) * (horas_trabajadas - 40)
            # Si las horas trabajadas son más de 40 pero menos de 45, calcular un bono multiplicando el salario por hora por 1.5
            # y luego multiplicándolo por la diferencia entre las horas trabajadas y 40.

        salario_total = salario_base + bono
        # Calcular el salario total sumando el salario base y el bono calculado.

    return salario_total
    # Devolver el salario total calculado desde la función.

# Definición de la función principal
def main():
    salario_base_por_hora = float(input("Ingresa el salario base por hora: "))
    # Solicitar al usuario que ingrese el salario por hora y almacenarlo en la variable 'salario_base_por_hora'.

    horas = float(input("Ingresa el número de horas trabajadas: "))
    # Solicitar al usuario que ingrese el número de horas trabajadas y almacenarlo en la variable 'horas'.

    pago = calculo_salario(horas, salario_base_por_hora)
    # Llamar a la función 'calculo_salario' con los valores proporcionados y almacenar el resultado en 'pago'.

    print(f"Total a pagar: {pago}")
    # Imprimir el total calculado a pagar utilizando un f-string.

# Función principal
if __name__ == '__main__':
    main()
    # Este bloque de código verifica si el script se está ejecutando como programa principal (no importado como módulo)
    # y luego llama a la función 'main', que inicia la ejecución del programa.
