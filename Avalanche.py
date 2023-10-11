import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Povećajte veličinu snijega i brzinu kretanja lavine
snijeg = np.zeros((200, 200))
snijeg[100, 100] = 40  # Početni sloj snijega u sredini

brzina_kretanja_lavine = 20  # Povećajte brzinu kretanja lavine
gustoca_snijega = 0.5

lavina_x = np.random.randint(80, 120)  # Početna pozicija lavine (x-koordinata)
lavina_y = np.random.randint(80, 120)  # Početna pozicija lavine (y-koordinata)
lavina_smjer_x = np.random.choice([-1, 1])  # Smjer kretanja lavine (lijevo/desno)
lavina_smjer_y = np.random.choice([-1, 1])  # Smjer kretanja lavine (gore/dolje)

# Funkcija za animaciju
def update(frame):
    global snijeg, lavina_x, lavina_y, lavina_smjer_x, lavina_smjer_y
    novi_snijeg = np.copy(snijeg)
    
    # Pomaknite lavinu
    lavina_x += lavina_smjer_x
    lavina_y += lavina_smjer_y
    
    # Ako lavina dosegne rub, promijenite smjer
    if lavina_x <= 0 or lavina_x >= 199:
        lavina_smjer_x *= -1
    if lavina_y <= 0 or lavina_y >= 199:
        lavina_smjer_y *= -1
    
    for i in range(1, 199):
        for j in range(1, 199):
            # Računanje promjene snijega na temelju brzine lavine i gustine snijega
            promjena_snijega = (snijeg[i, j] - snijeg[i+1, j+1]) * brzina_kretanja_lavine * gustoca_snijega
            novi_snijeg[i+1, j+1] += promjena_snijega
    
    # Dodajte "lavinsku masu" na novu poziciju
    novi_snijeg[lavina_x, lavina_y] = 60  # Više snijega u lavini
    
    snijeg = novi_snijeg
    im.set_array(snijeg)

fig, ax = plt.subplots()
im = ax.imshow(snijeg, cmap='viridis')
ani = FuncAnimation(fig, update, frames=range(5000), repeat=False, blit=False)  # Povećajte broj okvira za dulje trajanje

plt.colorbar(im)
plt.show()
