
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
    


def f(T):
  Cp = 0.99403 + 1.671 * 10**-4 * T + 9.7215 * 10**-8 * T**2 - 9.5838 * 10**-11 * T**3 + 1.9520 * 10**-14 * T**4
  return Cp - 1.1

def flin(T):
  return 1.671 * 10**-4 + 2 * 9.7215 * 10**-8 * T - 3 * 9.5838 * 10**-11 * T**2 + 4 * 1.9520 * 10**-14 * T**3

chute = 1
precisao = 0.00005
maxIteracao = 50


(houveErro, raiz) = newtonRapson(f, flin, chute, precisao, maxIteracao)

if houveErro:
    print("O Método da Bisseção retornou um erro.")
if raiz is not None:
    print("Raiz encontrada: %s" % raiz)

