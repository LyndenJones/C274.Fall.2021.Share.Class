import bitio
import sys

def main():
    f = open("simple.txt", "rb")
    read_bits = bitio.BitReader(f)

    n = 0
    try:
        while True:
            bit = read_bits.readbit()
            print(bit, end="")
            n += 1
            if(n==8):
                print()
                n = 0
    except:
        f.close()

    f.close()

if __name__ == "__main__":
    main()
