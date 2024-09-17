import math

def newtonRapson(f, flin, chute, precisao,maxIteracao):
   
    if abs(f(chute)) <= precisao:
        return (False, chute)
    
    print("k\t x\t\t f(x)\t\t f'(x)")
    print("%d\t%e\t%e\t%e" %(0, chute, f(chute), flin(chute)))


    for k in range(1, maxIteracao+1):
        x1 = chute - f(chute)/flin(chute)

        print("%d\t%e\t%e\t%e" %(k, chute, f(x1), flin(x1)))

        if abs(f(x1)) < precisao:
            return (False, x1)
        
        chute = x1

      
    print("Erro, numeros maximo de iterações atingido")
    return(True, x1)
    


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


def flin(N):
  """
  Função que representa a derivada da equação do problema (usando a regra da cadeia).
  """
  T0 = 300
  T = 1000
  u0 = 1360
  q = 1.7 * 10 ** -19
  ni = 6.21 * 10 ** 9

  u = u0 * (T0 / T) ** 2.42
  n = (N + math.sqrt(N ** 2 + 4 * ni ** 2)) / 2

  # Derivada de n em relação a N
  dn_dN = 0.5 * (1 + N / math.sqrt(N ** 2 + 4 * ni ** 2))

  # Derivada de rho em relação a n
  drho_dn = -1 / (q * u * n ** 2)

  # Derivada de rho em relação a N usando a regra da cadeia
  drho_dN = drho_dn * dn_dN

  return drho_dN

chute = 0.5
precisao =0.00005
maxIteracao = 50


(houveErro, raiz) = newtonRapson(f, flin, chute, precisao, maxIteracao)

if houveErro:
    print("O Método da Bisseção retornou um erro.")
if raiz is not None:
    print("Raiz encontrada: %s" % raiz)

