import numpy as np
import matplotlib.pyplot as plt
class decomposicao_fourier:
  def __init__(self):
    self.t = np.linspace(0, 2 * np.pi, 1000)
    self.onda_quadrada = np.sign(np.sin(self.t))


  def processo(self,terms):
    soma_sinais = np.zeros_like(self.t) 

    for k in range(1, (terms * 2), 2): 

            onda_atual = (4 / (np.pi * k)) * np.sin(k * self.t)
            soma_sinais += onda_atual 
    
    plt.figure(figsize=(12, 7))
    plt.plot(self.t, self.onda_quadrada, label="Onda Quadrada Ideal", color='black', linewidth=3, linestyle='dashed')
    plt.plot(self.t, soma_sinais, label=f"Soma de {terms} ondas") if terms > 1 else plt.plot(self.t, soma_sinais, label=f"Soma de {terms} onda")
    plt.title("Como a Decomposição de Fourier constrói um sinal")
    plt.xlabel("Tempo (t)")
    plt.ylabel("Amplitude")
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.plot(self.t, soma_sinais, label=f"Soma de {terms} ondas")
    #plt.show()
    plt.savefig(fr"output/decomposicao_fourier.png")

if __name__ == "__main__":
    dec = decomposicao_fourier()
    dec.processo(1)