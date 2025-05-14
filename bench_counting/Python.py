import time

start_time = time.perf_counter()

i = 0
while i < 1000000: i+=1

end_time = time.perf_counter()
execution_time = end_time - start_time

data = {}
try:
    with open("../data/data.txt", 'r') as f:
        for ligne in f:
            if ':' in ligne:
                nom, val = ligne.strip().split(':')
                data[nom.strip()] = float(val.strip())
except FileNotFoundError:
    print("Fichier incorrect")

data["Python"] = execution_time

with open("../data/data.txt", 'w') as f:
    for nom, val in data.items():
        f.write(f"{nom}: {val}\n")
