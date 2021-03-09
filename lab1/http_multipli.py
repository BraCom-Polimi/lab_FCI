import requests 
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use("TkAgg")

servers = [
    ("http://www.gazzetta.it","pink","Gazzetta"),
    ("http://www.ansa.it","green","Ansa"),
    ("http://www.amazon.com","orange","Amazon")
]

n = 10
plt.figure()
for server,c,name in servers:
    print(f"Analizzo il sito {server}")
    tempi = []
    for _ in range(n):
        r = requests.get(server)
        t = r.elapsed.microseconds/1000
        tempi.append(t)
    plt.plot(tempi,color=c,label=name)

plt.grid()
plt.legend()
plt.xlabel("ID Misurazione")
plt.ylabel("Tempo di risposta [ms]")

plt.show()

    