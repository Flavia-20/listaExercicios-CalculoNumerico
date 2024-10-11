import math

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

def f(N):
  """
  Função que representa a equação do problema.
  """
  T0 = 300
  T = 1000
  u0 = 1360
  q = 1.7 * 10 ** -19
  ni = 6.21 * 10 ** 9
  p = 6.5 * 10 ** 6

  u = u0 * (T0 / T) ** 2.42
  n = (N + math.sqrt(N ** 2 + 4 * ni ** 2)) / 2
  rho = 1 / (q * n * u)

  return rho - p

print(f"f(0) = {f(0)}")
print(f"f(10^12) = {f(10**12)}")

