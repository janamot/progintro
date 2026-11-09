from statistics import mean

def load_file(path):
    """Načte platná měření a chyby z jednoho souboru."""
    with open(path, "r", encoding="utf-8") as file:
        txt = []
        for line in file:
            txt.append(line)
    return txt    

def merge_measurements(paths):
    """Spojí a seřadí měření ze zadaných souborů."""
    sloucene = []
    errors = []
    for path in paths:
        seznam = load_file(path)
        for j in seznam:
            if j[17:21] != "chyb":
                sloucene.append(j)
            else:
                error = f"{path}, řádek {seznam.index(j) +1}: chyba" 
                errors.append(error)
            
    sloucene.sort()
    return sloucene, errors

def summarize_by_day(measurements):
    """Vrátí statistiky pro jednotlivé dny."""
    summaries = []
    dny = -1
    data=[]
    for i in range(len(measurements)):
        i_measurements = measurements[i]
        if i != 0 and i_measurements[0:10] == measurements[i-1][0:10]:
            #if i_measurements[17:21] != "chyb":
            data[dny].append(float(i_measurements[17:21]))
        else:
            summaries.append([i_measurements[0:10]])
            data.append([float(i_measurements[17:21])])
            dny += 1

    for i in range(len(data)):
        min_data = min(data[i])
        max_data = max(data[i])
        mean_data = mean(data[i])
        summaries[i].append(min_data)
        summaries[i].append(max_data)
        summaries[i].append(mean_data)
    print(summaries)
    return summaries


def write_outputs(measurements, summaries, errors):
    """Zapíše spojená data a report o importu."""
    with open (r"05 prace se soubory\06_slouceni_mereni_z_vice_souboru\combined_measurements.txt", "w", encoding="utf-8") as file:
        for i in measurements:
            file.write(i)
            if not "\n" in i:
                file.write("\n")
        file.write("\n")
        file.write("\nReport:\n")
        for i in summaries:
            file.write(f"{i[0]}: min {i[1]}, max {i[2]}, průměr {i[3]} \n")
        file.write("\nPřeskočené vstupy: \n")
        for i in errors:
            file.write(i)
            if not "\n" in i:
                file.write("\n")        
            

def main():
    path_a = r"05 prace se soubory\06_slouceni_mereni_z_vice_souboru\measurements_a.txt"
    path_b = r"05 prace se soubory\06_slouceni_mereni_z_vice_souboru\measurements_b.txt"
    paths = [path_a, path_b]
    measurements, errors = merge_measurements(paths)
    summaries = summarize_by_day(measurements)
    write_outputs(measurements, summaries, errors)

if __name__ == "__main__":
    main()