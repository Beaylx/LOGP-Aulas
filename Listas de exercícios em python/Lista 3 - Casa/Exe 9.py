numero = 1

while True:
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")
    
    numero += 1 
  
    if numero > 20:
        break