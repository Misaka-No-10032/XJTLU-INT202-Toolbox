from clear_screen import clean
from eulers_totient import euler_totient
from extended_euclidean import extended_euclidean
from prime_factor import prime_factors
from my_rsa import rsa_generate_key, rsa_get_private_key, rsa_encrypt, rsa_decrypt, rsa_signature, validate
from fractional_knapsack import fractional_knapsack
from zero_one_knapsack import dynamic_selection, trace_back
from prettytable import PrettyTable


def totient():
    print('Euler\'s Totient Function')
    n = int(input("Input n: "))
    totient = euler_totient(n)
    print(totient[1])
    print(totient[2])
    print(f'\nphi(n) = {totient[0]}')


def eucliedan():
    print('Extended Euclidean Algorithm')
    print('gcd(a,b) = s * a + t * b\nmultiplicative inverse of b (mod a)')
    a = int(input("\nInput a: "))
    b = int(input("Input b: "))
    result = extended_euclidean(a, b)
    print(f'\n{result[-1]}')
    print(
        f'\ngcd({a}, {b}) = {result[1]} * {max(a, b)} + {result[2]} * {min(a, b)} = {result[0]}')
    if result[0] == 1:
        print(
            f'multiplicative inverse of {min(a, b)} (mod {max(a, b)}) = {result[2] if result[2] > 0 else result[2] + max(a, b)}\n')
    else:
        print(f'{min(a, b)} has no multiplicative inverse (mod {max(a, b)})\n')


def prime_decomposition():
    print('Prime Factorization')
    n = int(input("Input n: "))
    factors = prime_factors(n)
    equation = ""
    for key, value in factors.items():
        equation += f"{key}^{value} * "
    print(f'\n{n} = {equation[: -3]}\n')


def get_private_key():
    print('RSA Get Private Key')
    p = int(input("Input p: "))
    validate(p)
    q = int(input("Input q: "))
    validate(q)
    e = int(input("Input e: "))
    result = rsa_get_private_key(p, q, e)
    print(f'\nPrivate Key: {result}')


def encrypt():
    print('RSA Encryption')
    n = int(input("Input n: "))
    e = int(input("Input e: "))
    m = int(input("Input m: "))
    c = rsa_encrypt(m, e, n)
    print(f'\nEncrypted message ({m}^{e} (mod {n})): {c}')


def decrypt():
    print('RSA Decryption')
    n = int(input("Input n: "))
    d = int(input("Input d: "))
    c = int(input("Input c: "))
    m = rsa_decrypt(c, d, n)
    print(f'\nDecrypted message ({c}^{d} (mod {n})): {m}')


def signature():
    print('RSA Signature')
    n = int(input('Input n: '))
    d = int(input('Input d: '))
    e = int(input('Input e: '))
    m = int(input('Input m: '))
    print(f'RSA Signature Process:\n')
    rsa_signature(m, d, e, n)


def generate_key():
    print('RSA Generate Key')
    p = int(input("Input p: "))
    validate(p)
    q = int(input("Input q: "))
    validate(q)
    n, e, d = rsa_generate_key(p, q)
    print(f'\nPublic key (n, e): ({n}, {e}), Private key (d): {d}\n')


def zero_one_kp():
    print('0-1 Knapsack')
    W, B = [0], [0]
    ptb = PrettyTable()
    max_weight = int(input("Input the maximum weight of the knapsack: "))
    benefits = input("Input the benefits of the items: ").split()
    weights = input("Input the weights of the items: ").split()
    if len(benefits) != len(weights):
        raise Exception("The number of benefits and weights must be the same!")
    num_items = len(benefits)
    for i in range(num_items):
        B.append(int(benefits[i]))
        W.append(int(weights[i]))
    T = [[0 for j in range(max_weight + 1)] for i in range(num_items + 1)]
    S = [0 for i in range(num_items + 1)]
    dynamic_selection(W, B, T, max_weight, num_items, ptb)
    trace_back(num_items, max_weight, W, B, S, T, ptb)


def fkp():
    print('Fractional Knapsack')
    fractional_knapsack()


def z_star():
    print('Z* of a number')
    n = int(input("Input n: "))
    z = []
    for i in range(1, n):
        if extended_euclidean(i, n)[0] == 1:
            z.append(i)
    print(f'\nZ* of {n} = {z}\n{len(z)} in total.')


def run_func(func):
    try:
        clean()
        func()
    except Exception as e:
        print(e)
    input("\nPress Enter to continue...")


def menu():
    print("""***  INT202 ToolBox  ***
Please select an option:\n
1. 0-1 Knapsack
2. Fractional Knapsack
3. Euler's Totient Function (phi(n))
4. Z* of a number
5. Extended Euclidean Algorithm
6. Prime Factorization (In RSA: n --> p * q)
7. RSA Get Private Key (require: p, q, e)
8. RSA Encryption (require: n, e, m)
9. RSA Decryption (require: n, d, c)
10. RSA Generate Key (require: p, q)
11. RSA Signature Process (require: m, d, e, n)
0. Exit
""")


def main():
    while True:
        clean()
        menu()
        try:
            option = int(input("\nInput option: "))
        except Exception as e:
            option = -1
        if option == 1:
            run_func(zero_one_kp)
        elif option == 2:
            run_func(fkp)
        elif option == 3:
            run_func(totient)
        elif option == 4:
            run_func(z_star)
        elif option == 5:
            run_func(eucliedan)
        elif option == 6:
            run_func(prime_decomposition)
        elif option == 7:
            run_func(get_private_key)
        elif option == 8:
            run_func(encrypt)
        elif option == 9:
            run_func(decrypt)
        elif option == 10:
            run_func(generate_key)
        elif option == 11:
            run_func(signature)
        elif option == 0:
            break
        else:
            clean()
            print("\nInvalid option")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
    clean()
    exit()
