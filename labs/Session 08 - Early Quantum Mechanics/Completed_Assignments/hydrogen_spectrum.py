#!/usr/bin/env python3
# hydrogen_spectrum.py

# This source talks about the "correction for finite nuclear mass" on the Bohr model:
# https://sahussaintu.files.wordpress.com/2013/07/effect-of-finite-mass-of-nucleus-on-energy-level.pdf
# I used my modern physics textbook as my source:
# Eisberg, Robert, and Robert Resnick. Quantum Physics of Atoms, Molecules, Solids, Nuclei and Particles. 2nd ed.,
# Wiley, 1985, pp. 105-107.


def main():
    R = 1.0967757e7  # rydberg constant, empirical
    eCharge = 1.60217663e-19
    eMass = 9.1093837e-31
    pMass = 1.67262192e-27
    permittivity = 8.85418782e-12
    hPlank = 6.62607015e-34
    speedLight = 299792458

    for k in range(5, 7):  # nf = 5, 6 yields pfund and humphrey series, respectively
        if k == 5:
            print("Rydberg Formula Hydrogen Pfund Series \n")
            print(" ni     wavelength  ")
            print(f"-" * 21)
        if k == 6:
            print("Rydberg Formula Hydrogen Humphrey Series \n")
            print(" ni     wavelength  \n")
            print(f"-" * 21)

        for j in range(k + 1, k + 6):  # for each k, loop j from k + 1 to k + 6
            # Formula for waveLength in nanometers
            waveLength = 1 / (R * (1 / pow(k, 2) - 1 / pow(j, 2))) * 1e9  # calculate
            # lambda by rearranging rydberg formula
            print(f"{j:>3,}{waveLength:15.4f} nm")  # prints wavelength corresponding to
            # 5 integer values of ni minimally greater than nf
        print()

    E0 = (pow(eCharge, 4) * eMass) / (8 * pow(permittivity, 2) * pow(hPlank, 2))

    for f in range(5, 7):
        if f == 5:
            print("Bohr Model Hydrogen Pfund Series \n")
            print(" ni     wavelength (nm)")
            print(f"-" * 21)
        if f == 6:
            print("Bohr Model Hydrogen Humphrey Series \n")
            print(" ni     wavelength (nm)")
            print(f"-" * 21)
        for i in range(f + 1, f + 6):
            # Initial energy level
            Ei = -E0 / pow(i, 2)
            # Final energy level
            Ef = -E0 / pow(f, 2)
            # Formula for waveLength in nanometers
            waveLength = (
                hPlank * speedLight / (Ei - Ef) * 1e9
            )  # rearrange Bohr formula for
            # photon energy
            print(f"{i:>3,}{waveLength:15.4f} nm")
        print()

    u = (eMass * pMass) / (eMass + pMass)

    for h in range(5, 7):
        if h == 5:
            print("Corrected Bohr Model Hydrogen Pfund Series \n")
            print(" ni     wavelength (nm)")
            print(f"-" * 31)
        if h == 6:
            print("Corrected Bohr Model Hydrogen Humphrey Series \n")
            print(" ni     wavelength (nm)")
            print(f"-" * 31)
        for l in range(h + 1, h + 6):
            Ei = -E0 / pow(l, 2)
            Ef = -E0 / pow(h, 2)
            waveLength = (
                (eMass / u) * hPlank * speedLight / (Ei - Ef) * 1e9
            )  # I am just taking bohr's formula and multiplying
            # it by the reduced mass of hydrogen divided by the mass of an electron, defined above (when solving for wavelength,
            #  you multiply by the reciprocal as seen here)
            R_waveLength = 1 / (R * (1 / pow(h, 2) - 1 / pow(l, 2))) * 1e9
            print(f"{l:>3,}{waveLength:15.4f} nm")
            print(
                f"(Rydberg wavelength: {R_waveLength: .4f} nm, which is an error of "
                f"{abs(waveLength - R_waveLength) * 100 / R_waveLength} %) \n"
            )  # relative error. By treating the nucleus as
            # having finite mass (i.e. it is allowed to orbit the electron, at the same time the electron orbits the
            # nucleus) you can solve the same equations bohr did with u in the place of m. For Hydrogen atom, this just
            # means that the bohr photon wavelengths are all off from rydberg's wavelengths by a constant u / m.
        print()


if __name__ == "__main__":
    main()
