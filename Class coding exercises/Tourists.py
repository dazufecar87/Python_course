import json
from collections import defaultdict

count = defaultdict(int)
paises = []

with open("tourists.json", "r") as read_file:
  tourists = json.load(read_file)["data"]
  
  for tourist in tourists:
    paises.append(tourist['País de procedencia'])

  for pais in paises:
    count[pais] += 1
  
  print(count)
    
N = int(input('Ingresa un numero '))

while N != 1: 
  
  if N%2 == 0:
    print("N was even")
    N = N / 2
    print(N)
  else:
    N = (N*3) + 1
    print("N was odd")
    print(N)
