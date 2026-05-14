flux_plot.py
import matplotlib.pyplot as plt

age = [13,14,15,16,17,18,19,20]
soft_flux = [1.1,1.5,2.3,3.2,4.1,5.0,5.8,6.0]
hard_flux = [0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5]

plt.plot(age, soft_flux, marker='o', label='Soft X-ray Flux')
plt.plot(age, hard_flux, marker='s', label='Hard X-ray Flux')

plt.xlabel("Age (Years)")
plt.ylabel("Flux")
plt.title("SN1987A Flux Evolution")
plt.legend()

plt.savefig("combined_flux.png")
plt.show()
