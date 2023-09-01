import pytest
from src.problem1 import calculo_salario  

@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (33,1000,33000.0),
        (43,500,22250.0),
        (-40,1000,-1),
        (55,-10000,-1),
        (47,100,5400.0)
    ]
)

def test_calculo_salario(input_x, input_y, expected):
    assert calculo_salario(input_x, input_y) == expected

def test_calculo_salario_argumentos():
    with pytest.raises(TypeError):
        calculo_salario(40)
        calculo_salario()
        calculo_salario(40, 10000, 5000)


if __name__ == "__main__":
    pytest.main()
