arquivo = open(r"C:\Users\egeraldo\OneDrive - EDENRED\Documents\PyDados/contatos-escrita.csv", encoding='latin_1', mode='w')

print(type(arquivo.buffer))

#conteudo = arquivo.buffer.read()
#print(conteudo)

contato = bytes('15,verônia,veronica@gmail.com', 'latin_1')
arquivo.buffer.write(contato)

arquivo.close()