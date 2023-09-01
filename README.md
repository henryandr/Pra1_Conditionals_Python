# Instrucciones
1. Clone el repositorio en su computador.
2. Busque dentro de la carpeta `src` los archivos `problem1.py`, `problem2.py` y `problem3.py`.
3. Usando un editor de texto para ingresar su código en el lugar indicado.
4. Realice los cambios y haga los _commits_ cada vez que haga una modificación al código. El control de versión es muy importante.
5. Cuando realice `git push`, la autoevaluación de su trabajo se realizará en github.

---

# Problema 1: Calculadora de salario para empleados
---
## Descripción del problema
---
Diseña el código para una función que calcula el salario total de un empleado en función del valor de la hora trabajada y el número de horas trabajadas. La función debe considerar las siguientes condiciones:

- Si las horas trabajadas exceden 50 horas, la función debe retornar un valor -1 para indicar un error.
- Si se ingresa cualquie valor negativo, la función debe retornar -1.
- Si las horas trabajadas están entre 41 y 45, cada hora extra trabajada se paga un 50% más que la tarifa base por hora.
- Si las horas trabajadas son 46 o más, cada hora extra trabajada se paga al doble de la tarifa base por hora.
- Calcular el salario total sumando el salario base y el bono de horas extra correspondiente, si aplica.

## Entrada

La función debe recibir los siguientes argumentos:
- `valor_hora`: el valor de la hora trabajada (un número de punto flotante).
- `horas_trabajadas`: el número de horas trabajadas (un número entero).

## Salida

La función debe retornar un valor decimal que representa el salario total a pagar, o -1 en caso de que los datos ingresados no sean válidos.

---
# Problema 2: Calculadora de Índice de Masa Corporal (IMC)
---
## Descripción del Problema

Escribe el código para una función llamada **`clasifica_imc()`** que solicita el peso, la estatura y la edad de una persona. Luego, calcula el Índice de Masa Corporal (**IMC**) de la persona y la categorización de su estado de peso. 

Las categorías de peso basadas en el IMC son las siguientes:

| IMC           | Categoría             |
|---------------|-----------------------|
| < 18.5        | Bajo peso             |
| 18.5 - 24.9   | Peso normal           |
| 25 - 29.9     | Sobrepeso             |
| 30 - 34.9     | Obesidad grado I      |
| 35 - 39.9     | Obesidad grado II     |
| >= 40         | Obesidad grado III    |

## Verificación de datos
- Si la persona es menor de 18 años, el programa debe retornar el mensaje: **`"Cálculo válido solo para adultos"`** y retornar el valor de **`IMC = -1`**.
- Si se ingresa cualquier dato negativo, el programa debe retornar el mensaje **`"No se aceptan valores negativos"`** y retornar el valor de **`IMC = -1`**.

## Entrada
El programa debe solicitar los siguientes datos al usuario:
- Peso en kilogramos.
- Estatura en metros.
- Edad.

## Salida

La función retorna el IMC y un mensaje en una cadena de caracteres según la columna **Categoría** de la tabla anteior.

---
# Problema 3: Verificación de variables del motor antes del despegue

Un piloto y su equipo de mecánicos están realizando la verificación minuciosa de las variables del motor de una aeronave antes de proceder con el despegue. Asegurarse de que todas las variables estén dentro de los límites adecuados es esencial para garantizar un vuelo seguro. Se han establecido límites hipotéticos para las variables del motor que deben ser comprobados.

A continuación se presentan las variables que deben ser verificadas y sus límites:

| Variable            | Límites                 |
|--------------------|-------------------------|
| Temperatura de Aceite | 150°F - 250°F |
| Presión de Aceite | 40 psi - 80 psi |
| Gases de Escape   | 500°F - 1000°F |
| Bomba de Vacío    | Mínimo 5 pulgadas de Hg |
| Instrumentos del Motor | Deben estar operativos |

Diseña el código de una función llamada `verificar_avion()` que tome como argumentos las mediciones de estas variables y devuelva un mensaje indicando si la aeronave está lista para despegar o si alguna de las variables está fuera de los límites establecidos.

## Entradas:

- `temp_aceite`: Temperatura del aceite en grados Fahrenheit.
- `presion_aceite`: Presión del aceite en psi.
- `gases_escape`: Temperatura de los gases de escape en grados Fahrenheit.
- `bomba_vacio`: Medición de la bomba de vacío en pulgadas de mercurio (Hg).
- `instrumentos_motor`: Respuesta "Sí" o "No" sobre si los instrumentos del motor están operativos.

## Salida Esperada:

- Si todas las variables están dentro de los límites y los instrumentos del motor están operativos, la función debe retornar exactamente el mensaje: `"¡La aeronave está lista para despegar!"`.
- Si alguna de las variables está fuera de los límites o los instrumentos del motor no están operativos, la función debe retornar un mensaje detallando todos los problemas, por ejemplo: La línea 1 se imprime siempre, las demás líneas (_el texto exacto, incluido el punto_) dependiendo del cumplimiento de los condicionales.
1. `¡Atención! problemas:`
2. `Temperatura de aceite fuera de límites.`
3. `Presión de aceite fuera de límites.`
4. `Gases de escape fuera de límites.`
5. `Bomba de vacío no genera suficiente vacío.`
6. `Instrumentos del motor no operativos.`