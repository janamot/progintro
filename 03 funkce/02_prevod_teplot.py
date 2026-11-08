def convert_temperature(value, from_unit, to_unit):
    if from_unit == "K":
        value = value - 273.15
    elif from_unit == "F":
        value = 5/9 * (value - 32)
    elif from_unit == "C":
        value = value
    else:
        return
    
    if to_unit == "C":
        return value
    elif to_unit == "F":
        value = 9/5 * value + 32
        return value
    elif to_unit == "K":
        value = value + 273.15
        return value
    else:
        return
    


print(convert_temperature(100, "C", "F"))   # 212.0
print(convert_temperature(0, "K", "C"))     # -273.15
print(convert_temperature(-40, "C", "F"))   # -40.0
print(convert_temperature(20, "C", "X"))    # None

for i in range(-40, 101, 20):
    print(f"{i}°C --> {convert_temperature(i, "C", "F")}°F --> {convert_temperature(i, "C", "K")}")