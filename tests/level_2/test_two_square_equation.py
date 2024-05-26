from functions.level_2.two_square_equation import solve_square_equation


def test__solve_square_equation__negative_discriminant():
    square_coefficient = 1.0
    linear_coefficient = 0.0
    const_coefficient = 1.0

    root_left, root_right = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert root_left is None
    assert root_right is None


def test__solve_square_equation__not_negative_discriminant_and_not_zero_square_coefficient_and_not_zero_linear_coefficient():
    square_coefficient = 2.0
    linear_coefficient = 5.0
    const_coefficient = 2.0

    root_left, root_right = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)
    assert root_left == -2.0
    assert root_right == -0.5


def test__solve_square_equation__not_negative_discriminant_and_not_zero_square_coefficient_and_zero_linear_coefficient():
    square_coefficient = 1.0
    linear_coefficient = 0.0
    const_coefficient = -4.0

    root_left, root_right = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)
    assert root_left == -2.0
    assert root_right == 2.0


def test__solve_square_equation__not_negative_discriminant_and_zero_square_coefficient_and_not_zero_linear_coefficient():
    square_coefficient = 0.0
    linear_coefficient = 2.0
    const_coefficient = 1.0

    root_left, root_right = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert root_left == -0.5
    assert root_right is None


def test__solve_square_equation__not_negative_discriminant_and_zero_square_coefficient_and_zero_linear_coefficient():
    square_coefficient = 0.0
    linear_coefficient = 0.0
    const_coefficient = 1.0

    root_left, root_right = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert root_left is None
    assert root_right is None
