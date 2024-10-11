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

    if abs(Fm) <= criterioParada:
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



def f(theta0, v0=30, x=90, y0=1.8, y=1, g=9.81):
  return (math.tan(math.radians(theta0)) * x - (g * x**2) / (2 * v0**2 * math.cos(math.radians(theta0))**2) + y0) - y



a = 0.5
b = 0.85
criterioParada = 0.0005
maxInteracao = 20


(houveErro, raiz) = bisseccao(f, a, b, criterioParada, maxInteracao)


if houveErro:
    print("O Método da Bisseção retornou um erro.")
if raiz is not None:
    print("Raiz encontrada: %s" % raiz)
