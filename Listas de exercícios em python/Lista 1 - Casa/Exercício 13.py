s0=2
v0=3
a=10

t=float(input("Digite o valor de t (em segundos): "))
s= s0+v0*t+0.5*a*(t ** 2)

print(f"O valor de s (posição final) é:",'%.2f' %s, "m." )