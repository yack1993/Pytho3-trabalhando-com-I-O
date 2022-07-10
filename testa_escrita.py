#arquivo_contatos = open(r"C:\Users\egeraldo\OneDrive - EDENRED\Documents\PyDados/contatos-escrita.csv", encoding='latin_1', mode='a')
#arquivo_contatos = open(r"C:\Users\egeraldo\OneDrive - EDENRED\Documents\PyDados/contatos-escrita.csv", encoding='latin_1', mode='w')
#arquivo_contatos = open(r"C:\Users\egeraldo\OneDrive - EDENRED\Documents\PyDados/contatos-escrita.csv", encoding='latin_1', mode='a+') #nsere o que pedimos ao final do arquivo
arquivo_contatos = open(r"C:\Users\egeraldo\OneDrive - EDENRED\Documents\PyDados/contatos-escrita.csv", encoding='latin_1', mode='w+') #escrita e leitura


contatos = ['11,carol,carol@gmail.com\n',
           '12,Ana,ana@gmail.com\n',
           '13,Tais,Tais@gmail.com\n',
           '14,Felipe, felipe@gmail.com\n']

for contato in contatos:
    arquivo_contatos.write(contato)


arquivo_contatos.flush()

arquivo_contatos.seek(28)
arquivo_contatos.write('12,Ana,ana@gmail.com\n'.upper())
arquivo_contatos.flush()
arquivo_contatos.seek(0)

for linha in arquivo_contatos:
    print(linha)
#arquivo_contatos.close()

#input('Pressione <Enter> para encerrar o programa')
#arquivo_contatos.write(contato)