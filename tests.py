from app import par_ou_impar, classificar_number

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