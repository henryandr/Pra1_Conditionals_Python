import pytest
from src.problem2 import categorizar_imc  

@pytest.mark.parametrize("peso, estatura, edad, expected_imc, expected_clasificacion", [
    (70, 1.75, 25, 22.86, "Peso normal"),
    (55, 1.60, 16, -1, "Cálculo válido para mayores de edad"),  # Edad < 18, retorna -1 (error)
    (90, 1.80, 40, 27.78, "Sobrepeso"),
    (110, 1.70, 50, 38.06, "Obesidad grado II"),
    (60, 1.75, 30, 19.59, "Peso normal"),
    (112, 1.6, 30, 43.75, "Obesidad grado III"),
    (112, -1.6, 30, -1, "No se aceptan valores negativos"),
    (-12, 1.6, 30, -1, "No se aceptan valores negativos"),
    (12, 1.6, -30, -1, "No se aceptan valores negativos"),
    
])
def test_categorizar_imc(peso, estatura, edad, expected_imc, expected_clasificacion):
    imc, clasificacion = categorizar_imc(peso, estatura, edad)
    assert imc == pytest.approx(expected_imc, rel=1e-2)  # Aproximación con tolerancia de 0.01
    assert clasificacion == expected_clasificacion

if __name__ == "__main__":
    pytest.main()
