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
    


def f(h, r=2, L=5, V=8):
 
  return (r**2 * math.acos((r - h) / r) - (r - h) * math.sqrt(2 * r * h - h**2)) * L - V


def flin(h, r=2, L=5):
  return L * (math.sqrt(2 * r * h - h**2) + (r - h) * (r - h) / math.sqrt(2 * r * h - h**2))


chute = 0.5
precisao = 0.00005
maxIteracao = 50


(houveErro, raiz) = newtonRapson(f, flin, chute, precisao, maxIteracao)

if houveErro:
    print("O Método da Bisseção retornou um erro.")
if raiz is not None:
    print("Raiz encontrada: %s" % raiz)

