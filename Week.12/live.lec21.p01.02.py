import bitio

def main():
    f = open("simple.txt","rb")
    read_bits = bitio.BitReader(f)
    try:
        while True:
            byte = read_bits.readbits(8)
            print(byte)
            print(chr(byte))
    except:
        f.close()

    f.close()

if __name__ == "__main__":
    main()
