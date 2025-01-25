from app import par_ou_impar, classificar_number
from structure_data import Car

def test_par_ou_impar_devolve_par():
    # Arrange / SetUp
    num = 500
    expected_result = 'par'

    # Act / Exercise
    result = par_ou_impar(
        num=num
    )

    # Assert / Verify
    assert result == expected_result

def test_par_ou_impar_devolve_impar():
    # Arrange / SetUp
    num = 501
    expected_result = 'impar'

    # Act / Exercise
    result = par_ou_impar(
        num=num
    )

    # Assert / Verify
    assert result == expected_result

def test_classificar_number_grande():
    # Arrange / SetUp
    num = 150
    expected_result = 'grande'

    # Act / Exercise
    result = classificar_number(
        num=num
    )

    # Assert / Verify
    assert result == expected_result

def test_car_has_all_attributes():
    # Averrage
    model = 'Marea'
    brand = 'Fiat'
    manufacturing_year = 1999

    # Act
    car = Car(
        model=model,
        brand=brand,
        manufacturing_year=manufacturing_year
    )

    # Assert
    car.model = model
    car.brand = brand
    car.manufacturing_year = manufacturing_year