arquivo1 = open(r"C:\Users\egeraldo\OneDrive - EDENRED\Documents\PyDados/contatos-escrita.csv", encoding='latin_1', mode='w')
arquivo2 = open(r"C:\Users\egeraldo\OneDrive - EDENRED\Documents\PyDados/contatos-escrita.csv", encoding='latin_1', mode='a')

contato_carol = '11,Carol, carol@gmail.com'
contato_andreza = '12,Andreza, andreza@gmail.com'

with open(r"C:\Users\egeraldo\OneDrive - EDENRED\Documents\PyDados/contatos-escrita.csv", encoding='latin_1', mode='w') as arquivo1:
    arquivo1.write(contato_carol)

with open(r"C:\Users\egeraldo\OneDrive - EDENRED\Documents\PyDados/contatos-escrita.csv", encoding='latin_1', mode='w') as arquivo2:
    arquivo2.write(contato_andreza)

#arquivo1.close()
#arquivo2.close()
