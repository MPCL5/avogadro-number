import stdio, math

Temp = 297.0
Visco = 9.135 * (10**-4)
Radius = .5 * (10**-6)
R = 8.31446

def main():
    iptArray = []
    while not stdio.isEmpty():
        line = stdio.readLine()
        # prvent error hello from ygame
        if not ('pygame' in line): 
            iptArray.append((float(line) * (0.175 * (10 ** -6)))**2)    

    selfDiffusion = sum(iptArray) / (2*len(iptArray))
    Boltzmann = (selfDiffusion*6*math.pi*Visco*Radius) / (Temp)
    Avogadro = R / Boltzmann

    print("Boltzmann = %.4e" % Boltzmann)
    print("Avogadro = %.4e" % Avogadro)



if __name__ == "__main__":
    main()