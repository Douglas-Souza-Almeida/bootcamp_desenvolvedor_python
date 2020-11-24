#exemplo de uso da estrutura de repetição for
lista=[]
for i in range(10):
   i=i+1
   inserir=input('Informe o item %d para incluir na lista: ' %i)
   lista.insert(i, inserir)
print('A lista salva será:')
print(lista)