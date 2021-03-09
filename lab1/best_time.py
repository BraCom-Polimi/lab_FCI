import requests 
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use("TkAgg")

servers = [
    ("http://www.ansa.it","green","Ansa"),
    ("http://www.gazzetta.it","pink","Gazzetta"),
    ("http://www.polimi.it","blue","Polimi"),
    ("http://www.polito.it","brown","Polito"),
]

averages = []

n = 5
plt.figure()
for server,c,name in servers:
    print(f"Analizzo il sito {server}")
    tempi = []
    for _ in range(n):
        r = requests.get(server)
        t = r.elapsed.microseconds/1000
        tempi.append(t)
    plt.plot(tempi,color=c,label=name)
    plt.axhline(np.average(tempi) , color=c, linestyle=":")
    averages.append(np.average(tempi))

print(f"Il miglior tempo medio è {min(averages)}ms di {servers[averages.index(min(averages))][2]}")

plt.grid()
plt.legend()
plt.xlabel("ID Misurazione")
plt.ylabel("Tempo di risposta [ms]")

plt.show()

    