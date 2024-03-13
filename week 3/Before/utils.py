import seaborn as sns
import matplotlib.pyplot as plt

#difining fitness
def fitness(number):
   return "{0:04b}"format(number).count("1")


sns.lineplot(x=[i for i in range(1,16)], y=[fitness(i) for i in range(1,16)])
plt.show()

