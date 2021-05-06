This is based on the RSA algorithm. [Read more about it here.](https://simple.wikipedia.org/wiki/RSA_algorithm)  and [here](https://open.oregonstate.education/cryptographyOEfirst/chapter/chapter-13-the-rsa-function/)

Formulae:   
> RSA function: `m = m*(e) % (n)`   
> inverse RSA function:`c = c**(d) % (n)`,     

Where:  
- m: PlainText
- c: ciphertext
- n: modulus of public and private keys,
- `(n = pq)`: where p, q are prime numbers 
- e: Public Key exponent
- d: Private key exponent

To find the totient of n (`ϕ(n)`), we will need to find p and q. We can find it from [this website](factordb.com/).  
After finding p and q,  
`ϕ(n) = (p-1)*(q-1)`  

Next, we need to find the private key exponent d. d is computed by the congruence relation   
`de ≅ 1 (mod ϕ(n))`, which is nothing but  
`d = c**(-1) (mod (ϕ(n))` i.e: d is the multiplicative inverse of `d % ϕ(n)`.

After finding d, we shapp apply the inverse RSA function.  
I used Crypto.Util for inverse and converting long int to bytestring.  

```
from Crypto.Util.number import inverse, long_to_bytes

c = <c>
n = <n>
e = <e>
p = <p>
q = <q>

totient = (p-1)*(q-1)

d = inverse(e, totient)

m = pow(c,d)
m = m % n

print(long_to_bytes(m))
```
