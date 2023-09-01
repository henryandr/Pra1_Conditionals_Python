import pytest
from src.problem3 import verificar_avion
# Casos de prueba utilizando @pytest.mark.parametrize

@pytest.mark.parametrize("temp_aceite, presion_aceite, gases_escape, bomba_vacio, instrumentos_motor, expected_output", [
    (200, 60, 800, 6, "Sí", "¡La aeronave está lista para despegar!"),  # Todas las variables dentro de límites
    (120, 60, 800, 6, "Sí", "¡Atención! problemas:\nTemperatura de aceite fuera de límites.\n"),  # Temperatura fuera de límites
    (200, 90, 800, 6, "Sí", "¡Atención! problemas:\nPresión de aceite fuera de límites.\n"),  # Presión fuera de límites
    (200, 60, 1100, 6, "Sí", "¡Atención! problemas:\nGases de escape fuera de límites.\n"),  # Gases de escape fuera de límites
    (200, 60, 800, 3, "Sí", "¡Atención! problemas:\nBomba de vacío no genera suficiente vacío.\n"),  # Bomba de vacío insuficiente
    (200, 60, 800, 6, "No", "¡Atención! problemas:\nInstrumentos del motor no operativos.\n"),  # Instrumentos no operativos
])
def test_verificar_avion(temp_aceite, presion_aceite, gases_escape, bomba_vacio, instrumentos_motor, expected_output):
    assert verificar_avion(temp_aceite, presion_aceite, gases_escape, bomba_vacio, instrumentos_motor) == expected_output

# Ejecutar las pruebas
if __name__ == "__main__":
    pytest.main()






