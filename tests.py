from app import par_ou_impar

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