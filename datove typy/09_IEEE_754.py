import struct
import decimal

#cislo = float(input("číslo:"))
cislo = -0.1

bity = struct.unpack(">Q", struct.pack(">d", cislo))[0]

s = (bity >> 63) & 1
e = (bity >> 52) & ((1 << 11)-1)
m = bity & ((1 << 52)-1)

s_bin = bin(s)[2:]
e_bin = bin(e)[2:].zfill(11)
m_bin = bin(m)[2:].zfill(52)


print("znaménko:", s_bin)
print("exponent:", e_bin, "(", e, ", tj. 2 ^", e-1023, ")" )
print("mantisa:", m_bin)
print("zpětně:", ((-1)**s)*(1+m/2**52)*(2**(e-1023)))
print("přesně:", decimal.Decimal(cislo))
