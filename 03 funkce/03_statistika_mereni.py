def mean(values):
    prumer = soucet(values) / len(values)
    return prumer

def median(values):
    data = sorted(values)
    stred = int(len(data)/2) - 1
    if len(data)%2 != 0:
        return data[stred]
    else:
        median = (data[stred] + data[stred + 1])/2
        return median
def std_dev(values):
    prumer = mean(values) 
    rozptyl = 0
    for i in range(len(values)):
        rozptyl += (values[i] - prumer)**2
    odchylka = (rozptyl/len(values))**(1/2)
    return odchylka
#(√(součet (x − průměr)² / n)),
def min_max(values):
    min = values[0]
    max = values[0]
    for i in range(1, len(values)):
        if values[i] > max:
            max = values[i]
        elif values[i] < min:
            min = values[i]
    return min, max


#— vrátí dvojici (nejmenší, největší) bez použití min() a max(),

def soucet(values):
    celkove = 0
    for i in range(len(values)):
        celkove += values[i]
    return celkove

def summary(values):
    min, max = min_max(values)
    return {"mean": mean(values), "median":median(values), "std_dev":std_dev(values), "min":min, "max":max}

data = [2, 4, 4, 4, 5, 5, 7, 9]
print(summary(data))
# {'mean': 5.0, 'median': 4.5, 'std_dev': 2.0, 'min': 2, 'max': 9}