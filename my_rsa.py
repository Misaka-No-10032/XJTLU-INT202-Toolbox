from extended_euclidean import extended_euclidean
from prime_factor import prime_factors
from eulers_totient import euler_totient


def validate(n):
    factors = prime_factors(n)
    if n not in factors.keys():
        raise ValueError(f'{n} is not a prime number')


def rsa_generate_key(p, q):
    validate(p)
    validate(q)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 0
    gcd = []
    for i in range(2, phi):
        gcd = extended_euclidean(i, phi)
        if gcd[0] == 1:
            e = i
            break
    d = gcd[2] if gcd[2] > 0 else gcd[2] + phi
    return n, e, d


def rsa_get_private_key(p, q, e):
    validate(p)
    validate(q)
    phi = (p - 1) * (q - 1)
    gcd = extended_euclidean(e, phi)
    if gcd[0] != 1:
        raise ValueError(f'{e} is not coprime to phi(n): {phi}')
    print(f'\nphi = ({p} - 1) * ({q} - 1) = {phi}\nd = {e}^-1 (mod {phi})')
    print(gcd[3])
    d = gcd[2] if gcd[2] > 0 else gcd[2] + phi
    return d


def rsa_encrypt(m, e, n):
    if m < 0:
        raise ValueError(f'Message: {m} must be positive.')
    if m >= n:
        raise OverflowError(f'Message: {m} cannot be larger than or equal to {n}.')
    phi = euler_totient(n)[0]
    if extended_euclidean(e, phi)[0] != 1:
        raise ValueError(f'{e} is not coprime to phi(n): {phi}')

    return pow(m, e, n)


def rsa_decrypt(c, d, n):
    return rsa_encrypt(c, d, n)


def rsa_signature(m, d, e, n):
    print(f'Enctypt the message with private key d: {d}')
    signature = rsa_encrypt(m, d, n)
    print(f'message = {m}\nsignature = {signature}')
    print(
        f'Validate the signature by decrypt the signature with public key (n, e): ({n}, {e})')
    m_dec = rsa_decrypt(signature, e, n)
    print(f"m\' = {m_dec}")
