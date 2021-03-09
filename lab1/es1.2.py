mport requests

def calcAvg(list):
   return sum(list)/len(list)

sites = ["http://www.google.com", "http://www.youtube.com", "http://www.facebook.com", "http://www.bloomberg.com", "http://www.netflix.com", "http://binance.com"]

times = []
avg = []
forVisual = []

for url in sites:
   for _ in range(10):
       r = requests.get(url)
       times.append(r.elapsed.microseconds/1000)
   avg.append(calcAvg(times))
   forVisual.append(url)
   forVisual.append(calcAvg(times))

for element in forVisual:
   print (element)

print ("winner: ", sites[avg.index(min(avg))])
