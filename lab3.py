#Problem 1
def gcd(x, y):
    #Return gcd(x, y) using the recursive Euclidean algorithm.
    if x == 0 and y == 0:
        return None
    if y == 0:
        return x
    return gcd(y, x % y)


#Problem 2
#This took like 2 hours straight of debugging :D
def mod_inv(x, y):
    #Return the multiplicative inverse of x mod y, uses the extended euclidean algorithm.
    #Inverse exists only if gcd(x, y) == 1
    if gcd(x, y) != 1:
        return None
    #Extended euclidean algorithm
    r0, r1 = x, y
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    #Loop until remainder = 0
    while r1 != 0:
        q = r0 // r1
        #Update remainders
        r0, r1 = r1, r0 % r1
        #Update bezout coefficients
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    #Inverse of x mod y is s0 mod y
    return s0 % y

#Problem 3
def mod_exp(x, y, n):
    #Compute x^y mod n using fast modular exponentiation
    #I pretty much just completely copied this from zybook
    base = x % n
    exponent = y
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % n
        base = (base * base) % n
        exponent //= 2
    return result

#Problem 4
def generate_RSA_keys(p, q):
    #Generate RSA public and private keys from primes p and q.
    n = p * q
    phi = (p - 1) * (q - 1)
    #Find e by starting at 3 and increading by 2 til gcd(e, phi) === 1
    e = 3
    while e < phi and gcd(e, phi) != 1:
        e += 2
    d = mod_inv(e, phi)
    public_key = [n, e]
    private_key = d
    return [public_key, private_key]

#Problem 5
if __name__ == '__main__':
    #Get input
    p = int(input("Enter prime p: "))
    q = int(input("Enter prime q: "))
    M = int(input("Enter plaintext integer M: "))
    #Get keys
    public_key, private_key = generate_RSA_keys(p, q)
    n, e = public_key
    d = private_key
    print(f"Public key (n, e): ({n}, {e})")
    print(f"Private key d: {d}")
    #Encrypt
    C = mod_exp(M, e, n)
    print(f"Ciphertext C: {C}")
    #Decrypt
    decrypted_M = mod_exp(C, d, n)
    print(f"Decrypted message: {decrypted_M}")