entrada = open("../Dados/bacteria.fasta").read()
saida = open("bacteria.html","w")


cont = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i+j] = 0

for k in range(len(entrada)):
    cont[entrada[k]+entrada[k+1]] += 1

print(cont)