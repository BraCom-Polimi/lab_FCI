import requests 
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use("TkAgg")

url = "http://www.google.com"
r = requests.get(url)

print(f"Tipo variabile r: {type(r)}")
print(f"Url contattato: {r.url}")
print(f"Codice di errore: {r.status_code}")
print(f"Tempo di risposta: {r.elapsed.microseconds/1000}ms")

plt.figure()
tempi = [50,40,23,44,19,33,55,72,44,52] # Dummmy data
n = 10
""" for _ in range(n):
    r = requests.get(url)
    t = r.elapsed.microseconds/1000
    tempi.append(t) """

print(f"Tempo medio dopo {n} richieste: {np.average(tempi)}")
print(f"Tempo massimo dopo {n} richieste: {np.max(tempi)}")
print(f"Tempo minimo dopo {n} richieste: {np.min(tempi)}")

plt.plot(tempi)
plt.xlabel("ID Misurazione")
plt.ylabel("Tempo di risposta [ms]")
plt.title(f"Tempi di risposta per {r.url}")
plt.axhline(np.average(tempi) , color='r')
plt.show()