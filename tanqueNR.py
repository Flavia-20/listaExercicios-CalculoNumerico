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
    

def f(x):
    return math.pi * x ** 2 *( (3 * 3 - x) / 3) - 30

def flin(x):
    return math.pi * x * (3 * 3 - x) - math.pi * x**2 / 3

chute = 1.5
precisao = 0.00005
maxIteracao = 50


(houveErro, raiz) = newtonRapson(f, flin, chute, precisao, maxIteracao)

if houveErro:
    print("O Método da Bisseção retornou um erro.")
if raiz is not None:
    print("Raiz encontrada: %s" % raiz)


