# ========================================================================================================================================================================================================================================
#INSTITUIÇÃO: Colégio Estadual Jardim Oriente (CEJO)/ SENAI
#CURSO:Técnico em desenvolvimento de Sistemas
#ESTUDANTE:Rianna késia dos Santos Aráujo
#TURMA:1°A(Matutino)
#DATA:13/10/2026
#UC:lógica de Programação 1 / programação de Apps 1
#DESCRIÇÂO:Prática de laço WHILE(Menu Interativo com Cadastro)
#=======================================================================================================================================================================================================================================

opcao= -1
lista_clientes=[]

while opcao!=0:
    #Exibir na tela
    print("\n=======================")
    print(" SISTEMA DE GESTÃO CEJO/SENAI")
    print(" ========================")
    print("1 -Cadastrar |Novo cliente")
    print("2 - Listar |Clientes cadastrados ")
    print("3 - consultar| Status do servidor")
    print("0 -Sair do sistema")

    estrada=input("\nDigite a opção desejada")

    if entrada.strip().isdigit():
     opcao= int(estrada)
    else:
     opcao=-1
    #OPÇÃO 1: CADASTRAR CLIENTE
    if opcao==1:
     print("\n>>[MÓDULO]: TELA DE CADASTRO DE CLIENTE")

    #Receba o nome e já remove espaços extras das pontas
     nome_cliente=input("Digite o nome do cliente;").strip()

     #Impede cadastrar um nome vazio(só Enter ou só espaços)
    if nome_cliente=="":
      print("⚠ O nome do cliente não pode ficar em branco. Cadastro cancelado")
    else:
     # O comando .append()adiciona o novo nome ao final da lista
      lista_cliente.append(nome_cliente)
      print("✅Cliente '{nome_cliente}' cadastro com sucesso!")
    #OPÇÃO 2:LISTAR CLIENTES
     elif opcao ==2
    
     

    #len() conta quantos itens existem na lista
       if len(lista_clientes)==0:
     print("⚠ Nenhum cliente cadastrado ainda.")
       else:
     print(f"Total de clientes: {len(lista_clientes)}\n")

     #O laço 'for' percorre a lista por item.
     #enumerate() entrega a posição (indice) e o ( cliente).
     #Somamos+1 poeque o Python começa a contar do 0.

       for indice, cliente in enumerate(lista_clientes):
                                         print(f"{indice + 1},{cliente}")

     #OPÇÃO 3: STATUS DO SERVIDOR(simulação)
   elif opcao == 3:
    print("\n>>[MÓDULO]: Servidor operando 100% online.")

     #OPÇÃO 0: SAIR
   elif opcao==0
     print("\n❌ Opção inválida! Digite apenas 0,1,2 ou 3.")

     # FIM DE PROGRAMAÇÃO.
                                         
                                         
                                                                                       
                                   
                            
                               
