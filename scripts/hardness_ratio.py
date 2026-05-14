soft_flux = [1.1,1.5,2.3,3.2,4.1]
hard_flux = [0.8,0.9,1.0,1.1,1.2]

ratio = []

for h, s in zip(hard_flux, soft_flux):
    ratio.append(h/s)

print("Hardness Ratios:")
print(ratio)
