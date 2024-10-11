import math

def bisseccao(f, a, b, criterioParada, maxInteracao):

    Fa = f(a)
    Fb = f(b)

    if Fa * Fb > 0:
        print("ERRO! A função não muda de sinal")
        return(True, None)
    
    print("k\t  a\t\t  fa\t\t  b\t\t  fb\t\t  x\t\t  fx\t\t")
    
    m = (a + b) /2
    Fm = f(m)

    print("-\t%e\t%e\t%e\t%e\t%e\t%e" % (a, Fa, b, Fb, m, Fm))

    if abs(Fm) < criterioParada:
        return(False, m)
    
    k = 1

    while k <= maxInteracao:
        if Fa * Fm > 0:
            a = m
            Fa = Fm
        else:
            b = m
            Fb = Fm


        m = (a + b) /2
        Fm = f(m)

        print("%d\t%e\t%e\t%e\t%e\t%e\t%e" % (k, a, Fa, b, Fb, m, Fm))


        if abs(Fm) <= criterioParada:
            return(False, m)
        
        k = k+1

    print("ERRO! número máximo de iterações atingido.")
    return (True, m)


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


a = 10 ** 9
b =  10 ** 12 
criterioParada = 0.00005
maxInteracao = 70


(houveErro, raiz) = bisseccao(f, a, b, criterioParada, maxInteracao)


if houveErro:
    print("O Método da Bisseção retornou um erro.")
if raiz is not None:
    print("Raiz encontrada: %s" % raiz)
