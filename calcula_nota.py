
def calcula_notas(): 
    #anuncia a entrada da aplicacao, saudacao
    print("Vamos calcular sua media do semestre juntos!")
    print("----------------------------------------------")
    
    
def calcula_g1():
    t1_bdd = float(input("Digite a nota do trabalho 1: "))
    p1_programacao = float(input("Digite a nota da prova de programacao 1: "))
    
    #nota_g1 vai calcular as notas pelos respectivos pesos dados pelos professores 
    nota_g1 = ((t1_bdd * 0.3) + (p1_programacao * 0.7)) 
    return nota_g1    

    
def calcula_g2():
    t2_bdd = float(input("Digite a nota do entregavel de BDD 2: "))
    t2_programacao = float(input("Digite a nota do entregavel de programacao 2: "))
    p2_bdd = float(input("Digite a nota da prova de BDD 2: "))
    p2_programacao = float(input("Digite a nota da prova de programacao 2: "))
    projeto_final_integrador = float(input("Digite a nota do projeto final integrador: "))
    
    #nota_g2 vai calcular as notas pelos respectivos pesos dados pelos professores 
    nota_g2 = (((t2_bdd + t2_programacao) * 0.3) + ((p2_bdd + p2_programacao) * 0.5) + (projeto_final_integrador * 0.2)) 
    return nota_g2

def calcula_aprovacao():
    calcula_notas() #-> chamada da funcao para exibir a mensagem inicial para o user
    
    #recepcao dos dados das funcoes acima
    g1 = calcula_g1()
    g2 = calcula_g2()
    
    #calculo da media final 
    nota_final = (g1 + g2) / 2
    print()
    print(f"A media das suas notas e: {nota_final:.2f}")
    print()
    
    #verificacao para aplicacao da mensagem de se o aluno vai ser aprovado, ficar em avaliacao ou reprovar na cadeira
    if nota_final >= 7.0:
        print("Voce foi APROVADO, parabenss!!")
    elif 5 <= nota_final < 7:
        print("Em avaliacao, se esforce um pouquinho mais, voce consegue!")
    else:
        print("Voce esta em prova final, vish, se vira meu parceiro")
        
calcula_aprovacao() #-> chamada da funcao