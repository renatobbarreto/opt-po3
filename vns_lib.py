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
    fo = []
    print(0, "   ", s, "Z =", f(s))
    _s = s.copy()
    y = 0
    i = 0
    while (i < 50):#criterio de parada
        k = 1
        while(k <= r):
            _s_ = BuscaLocal(_s, k)
            if( f(_s_) < f(_s)):
                _s = _s_
                k = 1
                y+=1
                fo.append(f(_s))
                print(y, "   ", _s, "Z =", f(_s))
            else:
                k+=1
                y+=1
                fo.append(f(_s))
                print(y, "   ", _s, "Z =", f(_s))
        i+=1
    plt.plot(list(range(1, len(fo)+1)), fo, 'b-', label = "Custo")
    plt.title("VNS")
    plt.legend()
    plt.xlabel("Iterações")
    plt.ylabel("Vendas")
    plt.show()
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
        i = random.randint(0,3)
        aux = dif[i]
        dif[i] = dif[i+1]
        dif[i+1] = aux
    else:
        i = random.randint(0,4)
        j = random.randint(0,4)
        aux = dif[i]
        dif[i] = dif[j]
        dif[j] = aux
    return dif

### codificação: VETOR DE 4 POSIÇÕES -> Primeira posição (0,1) representa o vendedor; Segunda posição representa
### qual valor da venda entre o linspace melhor favorece em len(vendedor[0] ou vendedor[1]); Terceira posição representa
### qual melhor porcentagem favorece a função (0, n); Quarta posição representa qual melhor salário fixo representa (0, n)
def fo(s):
    sal_min = 1045.00
    n = #?
    vendedor = []
    op = list()
    vendedor[0] = np.linspace(23116, 48544, 1000) 
    vendedor[1] = np.linspace(20000, 40000, 1000)
    
    #composição salarial:
    for i in range(0, n):
        op[i][0] = (i*0,01)
        op[i][1] = (sal_min*(0.5*i)) 
    for j in range(0, 4):
    receita = #não entendi como ficaria aqui (?)
    custo = vendedor[s[0]][s[1]]*op[s[2]][0] + op[0][s[3]]
    return (receita - custo)
