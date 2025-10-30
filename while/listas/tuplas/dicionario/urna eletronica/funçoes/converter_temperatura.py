def converter(temp):
    return temp * 1.8 +32

def main():
    temp_f = converter(float(input('informe a temperatura' 'em °c -> ')))

    print(f'atemperatura em °f e {temp_f}')

main()
