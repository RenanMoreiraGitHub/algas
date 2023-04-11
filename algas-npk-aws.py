# imports necessários
import datetime
from sys import getsizeof
import matplotlib.pyplot as plt
import random
import mysql.connector


dados_n = [];
dados_p = [];
dados_k = [];
dados_nivel_fertil = [];
dados_mem = [];
dados_tempo = [];

def gerar_dados(min, max, step, nivel_fertilidade):

    conexao = mysql.connector.connect(
    host= "localhost",
    user= "solo_fertil",
    password= "urubu100",
    database= "soy_fertility"
    )

    nivel_fertil = '';

    inicio_tempo = datetime.datetime.now(); 
    
    # Cria o cursor
    cursor = conexao.cursor();

    mem = 0;
    for dado in range(min, max+1, step):

        if nivel_fertilidade == 4:
            dado_n = random.randint(60, 91);
            dado_p = random.randint(5, 11);
            dado_k = random.randint(50, 101);
            nivel_fertil = 'Falta de fertilizantes';
        elif nivel_fertilidade == 3:
            dado_n = random.randint(90, 121);
            dado_p = random.randint(10, 21);
            dado_k = random.randint(100, 151);
            nivel_fertil = 'Médio de fertilidade';
        elif nivel_fertilidade == 2:
            dado_n = random.randint(120, 151);
            dado_p = random.randint(20, 41);
            dado_k = random.randint(150, 201);
            nivel_fertil = 'Média a alta fertilidade';
        else:
            dado_n = random.randint(150, 251);
            dado_p = random.randint(40, 61);
            dado_k = random.randint(200, 301);
            nivel_fertil = 'Fértil';

        dados_n.append(dado_n);
        dados_p.append(dado_p);
        dados_k.append(dado_k);
        dados_nivel_fertil.append(nivel_fertil);

        #transação
        dados_n.sort();
        dados_p.sort();
        dados_k.sort();

        mem = getsizeof(dados_n + dados_p + dados_k) * 1024;
        dados_mem.append(mem);
        final_tempo = datetime.datetime.now();
        dado_tempo = (final_tempo - inicio_tempo).total_seconds();
        dados_tempo.append(dado_tempo);

        sql = "INSERT INTO solo_fertil values(null, %s, %s, %s, %s, %s, %s);"

        values = (dado_n, dado_p, dado_k, nivel_fertil, dado_tempo, mem);

        cursor.execute(sql, values);

        print(f'Inserção realizada: Nitrogênio: {dado_n} Fósforo: {dado_p} Potássio: {dado_k} Nível de fertilidade: {nivel_fertil} Tempo gasto: {dado_tempo} Memória: {mem}')
        
        conexao.commit();


    cursor.close();
    conexao.close();

while True:
    print("------------------------- NÍVEL DE FERTILIDADE --------------------------")
    print("Escolha um nível de fertilidade para ser gerado os dados:")
    print("1 - Fértil")
    print("2 - Média a alta fertilidade")
    print("3 - Médio de fertilidade")
    print("4 - Falta de fertilizantes")
    print("0 - Parar")
    resposta = int(input("Digite o número da opção: "))

    if resposta == 0:
        break

    print("\n Agora digite o valor inicial do intervalo: ")
    intervalo_inicial = int(input("Valor inicial: "))

    print("\n Agora digite o valor final do intervalo: ")
    intervalo_final = int(input("Valor final: "))

    if resposta == 1:
        gerar_dados(intervalo_inicial, intervalo_final, 1, 1);
    elif resposta == 2:
        gerar_dados(intervalo_inicial, intervalo_final, 1, 2);
    elif resposta == 3:
        gerar_dados(intervalo_inicial, intervalo_final, 1, 3);
    elif resposta == 4:
        gerar_dados(intervalo_inicial, intervalo_final, 1, 4);
    else:
        print("Opção inválida. Escolha uma opção correta!")