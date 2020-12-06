import random
import matplotlib.pylab as plt
import numpy as np

def vns(s,r):
    """
    Aplica o método VNS para minimização. Utiliza a função f(s) como 
    Função objetivo da otimização e a função BuscaLocal(s, k) como maneira
    de localizar a vizinhança de um determinado vetor solução s.
    
    Recebe:
        s => Solução inicial do problema, não é a solução ótima.
        r => número de vizinhanças que o problema vai se aprofundar.
        
    Retorna:
        _s => vetor com a sequência ótima para o problema de minimização, além
        de mostrar em tela a evolução do algoritmo e um gráfico com os resultados.
    """
    sal_min = 1045.00
    n = 10
    vendedor = []
    op = []
    vendedor.append(np.linspace(23116, 48544, 20)) 
    vendedor.append(np.linspace(20000, 40000, 20))
    #composição salarial:
    for i in range(0, n):
        a = []
        a.append((i+1)*0.01)
        a.append(sal_min*((i+1)))
        op.append(a)
    print(op)
    print(vendedor)
    v = []
    print(0, "   ", s, "Z =", fo(s, vendedor, op))
    _s = s.copy()
    y = 0
    i = 0
    while (i < 200):#criterio de parada
        k = 1
        while(k <= r):
            _s_ = BuscaLocal(_s, k)
            if( fo(_s_, vendedor, op) > fo(_s, vendedor, op)):
                _s = _s_
                k = 1
                y+=1
                v.append(fo(_s, vendedor, op))
                print(y, "   ", _s, "Z =", fo(_s, vendedor, op))
            else:
                k+=1
                y+=1
                v.append(fo(_s, vendedor, op))
                print(y, "   ", _s, "Z =", fo(_s, vendedor, op))
        i+=1
    plt.plot(list(range(1, len(v)+1)), v, 'b-', label = "Lucro")
    plt.title("VNS")
    plt.legend()
    plt.xlabel("Iterações")
    plt.ylabel("Vendas")
    plt.show()
    print (vendedor[_s[0]][_s[1]], op[_s[2]][0], op[_s[3]][1]/1045.00)
    return _s 

def BuscaLocal(s, k):
    """
    Realiza busca local de forma sorteada levando em consideração a vizinhança
    N1 e N2.
    
    Recebe:
        s => sequência original da vizinhança
        k => número da vizinhança (1 para N1 e 2 para N2).
    
    Retorna:
        dif => um novo vetor modificado levando em consideração a nova
        vizinhança.
    """
    dif = s.copy()
    if(k < 2):
        if(dif[0]==0): dif[0] = 1
        else: dif[0] = 0
        i = random.randint(0,19)
        dif[1] = i
        j = random.randint(0,9)
        z = random.randint(0,1)
        dif[2] = j
        dif[3] = z
    else:
        i = random.randint(0,3)
        j = random.randint(0,3)
        aux = dif[i]
        dif[i] = dif[j]
        dif[j] = aux
    return dif

### codificação: VETOR DE 4 POSIÇÕES -> Primeira posição (0,1) representa o vendedor; Segunda posição representa
### qual valor da venda entre o linspace melhor favorece em len(vendedor[0] ou vendedor[1]); Terceira posição representa
### qual melhor porcentagem favorece a função (0, n); Quarta posição representa qual melhor salário fixo representa (0, 1)
def fo(s, vendedor, op): 
    for j in range(0, 4):
        receita = vendedor[s[0]][s[1]]
        custo = ((vendedor[s[0]][s[1]]*op[s[2]][0]) + op[s[3]][1])
    return (receita-custo)
