from prime_factor import prime_factors


def euler_totient(n):
    factors = prime_factors(n)
    result = n
    equation = ''
    euler_function = str(n) + ' * '
    for key, value in factors.items():
        result *= (1 - 1 / key)
        equation += f'{key}^{value} * '
        euler_function += f'(1 - 1/{key}) * '
    factor = f'\n{n} = {equation[:-3]}'
    function = f'\nEuler totient function: {euler_function[:-3]}'
    return [int(result), factor, function]
