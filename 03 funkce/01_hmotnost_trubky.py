import math

def circle_area(d):
    area = math.pi * (d/2)**2
    return area
    
def tube_cross_section(d_out, d_in):
    cross_section = float(circle_area(d_out)) - float(circle_area(d_in))
    return cross_section

def tube_mass(d_out, d_in, length, density=7850):
    mass = float(tube_cross_section(d_out, d_in) * length * density)
    return mass

print(tube_mass(0.060, 0.050, 6))                # ocelová trubka: ≈ 40.69 kg
print(tube_mass(0.060, 0.050, 6, density=2700))  # hliníková: ≈ 14.00 kg