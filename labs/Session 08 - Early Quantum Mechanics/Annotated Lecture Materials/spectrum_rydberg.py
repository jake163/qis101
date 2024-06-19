#!/usr/bin/env python3
# spectrum_rydberg.py


def main():
    R = 1.0967757e7  # rydberg constant, empirical

    print("Rydberg Formula Hydrogen Spectral Lines")

    for k in range(1, 5):  # loop k from 1 to 4
        for j in range(k + 1, k + 6):  # for each k, loop j from k + 1 to k + 6
            # Formula for waveLength in nanometers
            waveLength = 1 / (R * (1 / pow(k, 2) - 1 / pow(j, 2))) * 1e9  # calculate
            # lambda by rearranging rydberg formula
            print(f"{j:>3,}{waveLength:10.0f} nm")  # prints wavelength corresponding to
            # different j (excited n) values (up to k + 4) per k (initial n). In other
            # words, you get lyman, balmer, paschen, brackett series
        print()


if __name__ == "__main__":
    main()
