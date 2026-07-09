# Arquivo para os estudantes preencherem as lacunas
# Preencha os espaços em branco (______) com o código correto para interagir com o MongoDB

# LACUNA 1: Importe a função get_database do arquivo pymongo_get_connection_eventos
from pymongo_get_connection_eventos import get_database

def main():
    # 1. Obtendo a conexão com o banco de dados
    dbname = get_database()
    if dbname is None:
        print("Não foi possível conectar ao banco de dados. Encerrando.")
        return

    # 2. Selecionando a coleção 'participantes'
    # LACUNA 2: Nome da coleção
    colecao = dbname["participantes"]

    print("\n--- 1. INSERÇÃO (Create) ---")
    # LACUNA 3: Crie a estrutura do documento a ser inserido, inclua pelo menos 4 campos
    novo = {
        "_id": "part0111",
        "nome" : "Participante 111",
        "email": "participante111@email.com",
        "idade" :19
    }
    # Inserindo um único documento
    # Dica: Qual método usamos para inserir apenas UM documento?
    #colecao.insert_one(novo)# LACUNA 4: Método de inserção
    print("Participante inserido com sucesso!")

    print("\n--- 2. CONSULTA (Read) ---")
    # Buscando o participante recém-inserido pelo ID
    # LACUNA 5: Crie um filtro de busca para a coleção que você selecionou
    filtro_busca = {"_id":"part0111"}
    
    # Dica: Qual método usamos para buscar apenas UM documento?
    # LACUNA 5: Método de busca
    participante_encontrado = colecao.find_one(filtro_busca) 
    print(f"Participante encontrado: {participante_encontrado}")

    print("\n--- 3. ATUALIZAÇÃO (Update) ---")
    # LACUNA 6: Crie um filtro para atualização
    filtro_update = {"_id":"part0111"}
    # LACUNA 7: Monte a estrutura de atualização
    novos_valores =  {"$set": {"nome": "Participante 222"}}
    # LACUNA 8: Teste a atualização
    colecao.update_one(filtro_update,novos_valores)
    print("Participante atualizado com sucesso!")

    print("\n--- 4. EXCLUSÃO (Delete) ---")
    # Excluindo o participante de teste
    # LACUNA 9: Crie um filtro para exclusão
    filtro_delete = {"_id": "part0111"}
    
    # Dica: Qual método usamos para excluir apenas UM documento?
    colecao.delete_one(filtro_delete) # LACUNA 6: Método de exclusão
    print("Participante excluído com sucesso!")
    
    print("\n--- 5. CONSULTA AVANÇADA ---")
    # Crie uma consulta utilizando agregação ou operadores de comparação
    # Faça um comentário, indocando o que a consulta faz, exemplo: Listando os participantes em ordem alfabética
    

if __name__ == "__main__":
    main()
