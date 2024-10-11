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



def f(x):
    return math.pi * x ** 2 *( (3 * 3 - x) / 3) - 30


a = 1 #a altura não pode ser 0
b = 3
criterioParada = 0.00005
maxInteracao = 20

#outro intervalo: a = 7 #a altura não pode ser 0 b = 10


(houveErro, raiz) = bisseccao(f, a, b, criterioParada, maxInteracao)


if houveErro:
    print("O Método da Bisseção retornou um erro.")
if raiz is not None:
    print("Raiz encontrada: %s" % raiz)


#o altura do liquido qundo colocar 30 m cub. é o da primeira raiz pois o raio é 3 o diametro 6 então a segunda raiz não estaria certo