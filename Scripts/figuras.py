#Metodo para salvar a figura do grafico
import matplotlib.pyplot as plt

x = [1,3,5,7,9]
y = [2,3,7,1,0]
z = [200,105,400,250,150]

titulo = 'Scatterplot: gráfico de dispersão'
eixox = 'Eixo X'
eixoy = 'Eixo y'

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x, y, label="Meus pontos", color="g", marker='h', s=z)
plt.legend()
#apenas para ligar os pontos
plt.plot(x,y, color='k', linestyle='-.')
plt.savefig('figura1.pdf')
plt.savefig('figura1.png', dpi=300)
#plt.show()