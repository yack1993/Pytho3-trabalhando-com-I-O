import contatos_utis
try:
   #contatos = contatos_utis.csv_para_contatos(r"C:\Users\egeraldo\OneDrive - EDENRED\Documents\PyDados/contatos.csv")
   #contatos_utis.contatos_para_pickle(contatos, r"C:\Users\egeraldo\OneDrive - EDENRED\Documents\PyDados/contatos.pickle")

   #contatos = contatos_utis.pickle_para_contatos(r"C:\Users\egeraldo\OneDrive - EDENRED\Documents\PyDados/contatos.pickle") #carrega os arquivos pickle
   #contatos_utis.contatos_para_json(contatos, r"C:\Users\egeraldo\OneDrive - EDENRED\Documents\PyDados/contatos.json") #salva os arquivos em json

   contatos = contatos_utis.json_para_contatos(r"C:\Users\egeraldo\OneDrive - EDENRED\Documents\PyDados/contatos.json")

   for contato in contatos:
       print(f'{contato.id} - {contato.nome} - {contato.email}')

except FileNotFoundError:
    print("Arquivo não encontrado")
except PermissionError:
    print("Sem permissão de escrita")


