# import json
# import os
# from datetime import datetime

# ARQUIVO = "casos.json"



# def carregar_casos():
#     if os.path.exists(ARQUIVO):
#         with open(ARQUIVO, "r", encoding="utf-8") as f:
#             return json.load(f)
#         return []
    
# def salvar_casos(casos):
#     with open(ARQUIVO, "w", encoding="utf-8") as f:
#         json.dump(casos, f, ensure_ascii=False, indent=4)
        
# def proximos_id(casos):
#     if not casos:
#         return 1
#     return max(caso["id"] for caso in casos) +1

# def criar_caso(casos):
#     print("=== NOVO CASO ===\n")
#     titulo = input("Título: ")
#     local = input("Local: ")


#     caso = {
#         "id": proximos_id(casos),
#         "titulo": titulo,
#         "local": local,
#         "suspeitos": [],
#         "resolvido": False,
#         "data_criacao": datetime.now().isoformat(),
#         "data_resolucao": None
#     }
    
# casos.append()
# salvar_casos(casos)
# print("\nCaso criado com sucesso!")