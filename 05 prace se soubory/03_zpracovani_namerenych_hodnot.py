import numpy as np
import os

def load_measurements(path):
    """vrátí seznam dvojic (time, temperature),"""
    measurements=[]
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip() == "":
                continue
            if "chyba" in line:
                continue
            cleaned = line.strip("\n")
            data = cleaned.split(";")
            measurements.append((data))
    return measurements


def summarize(measurements):
    """vrátí minimum, maximum a průměr,"""
    temperature = []
    for i in range(len(measurements)):
        temperature.append(float(measurements[i][1]))
    mean = float(round(np.mean(temperature), 2))
    minT = min(temperature)
    maxT = max(temperature)

    return minT, maxT, mean


def write_report(path, measurements, summary):
    """uloží textový report."""
    with open(path, "w", encoding="utf-8") as file:
        text = f"naměřené hodnoty: {measurements}\n prumer: {summary[2]}\n minimum: {summary[0]}\n maximum: {summary[1]}"
        file.write(text)

def main():
    os.system('cls||clear')
    path = r"05 prace se soubory\measurements.txt"

    print(load_measurements(path))
    measurements = load_measurements(path)
    print(summarize(measurements))
    summary = summarize(measurements)

    path2 = r"05 prace se soubory\report.txt"
    write_report(path2, measurements, summary)

if __name__ == "__main__":
    main()