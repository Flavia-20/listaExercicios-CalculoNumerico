

def calcular_valor(i):
    resultado = 35000 * (i * (1 + i) ** 7) / ((1 + i) ** 7 - 1) - 8500
    return resultado

# Exemplo de uso:
P = 35000  # Valor principal
n = 7      # Número de períodos
A = 8500   # Valor subtraído

resultado = calcular_valor(0.1)
print(f"O resultado é: {resultado:.2f}")


print(6.5 * (10 ** 6))

def fT():
    letraGrega = 1360 *(1000/300)**-2.42
    #f(letraGrega)
    return letraGrega

print(fT())

# Valores conhecidos
rho = 650000  # Valor de ρ
q = 1.7 * 10**-9  # Valor de q
mu = 73.81971170832576  # Valor de μ

# Calculando n
n = 1 / (q * mu * rho)

print(f"O valor de n é: {n:.5e}")


