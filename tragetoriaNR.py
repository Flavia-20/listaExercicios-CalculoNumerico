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
    


def f(theta0, v0=30, x=90, y0=1.8, y=1, g=9.81):
    return (math.tan(math.radians(theta0)) * x - (g * x**2) / (2 * v0**2 * math.cos(math.radians(theta0))**2) + y0) - y

def flin(theta0, v0=30, x=90, g=9.81):
    theta_rad = math.radians(theta0)
    return x / (math.cos(theta_rad)**2) + (g * x**2 * math.sin(theta_rad)) / (v0**2 * math.cos(theta_rad)**3)


chute = 1.8
precisao = 0.0005
maxIteracao = 7000


(houveErro, raiz) = newtonRapson(f, flin, chute, precisao, maxIteracao)

if houveErro:
    print("O Método da Bisseção retornou um erro.")
if raiz is not None:
    print("Raiz encontrada: %s" % raiz)

