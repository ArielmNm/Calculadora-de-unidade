

def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def bitParaByte(valorASerConvertido):
    print('Valor convertido de bit para byte')
    bytesCalculado = valorASerConvertido / 8
    return bytesCalculado

def byteParaBit(valorASerConvertido):
    print('Valor convertido de byte para bit')
    bitsCalculado = valorASerConvertido * 8
    return bitsCalculado

def byteParaKilobyte(valorASerConvertido):
    print('Valor convertido de byte para kilobyte')
    bitsCalculado = valorASerConvertido /1024
    return bitsCalculado

def KilobyteParabyte(valorASerConvertido):
    print('Valor convertido de Kilobyte para byte')
    bitsCalculado = valorASerConvertido *1024
    return bitsCalculado

def KilobyteParaMegabyte(valorASerConvertido):
    print('Valor convertido de Kilobyte para Megabyte')
    bitsCalculado = valorASerConvertido /1024
    return bitsCalculado

def MegabyteParaKilobyte(valorASerConvertido):
    print('Valor convertido de Megabyte para Kilobyte')
    bitsCalculado = valorASerConvertido *1024
    return bitsCalculado

def MegabyteParaGigabyte(valorASerConvertido):
    print('Valor convertido de Megabyte para Gigabyte')
    bitsCalculado = valorASerConvertido /1024
    return bitsCalculado

def GigabyteParaMegabyte(valorASerConvertido):
    print('Valor convertido de Gigabyte para Megabyte')
    bitsCalculado = valorASerConvertido *1024
    return bitsCalculado

def GigabyteParaTerabyte(valorASerConvertido):
    print('Valor convertido de Gigabyte para Terabyte')
    bitsCalculado = valorASerConvertido /1024
    return bitsCalculado

def TerabyteParaGigabyte(valorASerConvertido):
    print('Valor convertido de Terabyte para Gigabyte')
    bitsCalculado = valorASerConvertido *1024
    return bitsCalculado

def TerabyteParaPetabyte(valorASerConvertido):
    print('Valor convertido de Terabyte para Petabyte')
    bitsCalculado = valorASerConvertido /1024
    return bitsCalculado

def PetabyteParaTerabyte(valorASerConvertido):
    print('Valor convertido de Petabyte para Terabyte')
    bitsCalculado = valorASerConvertido *1024
    return bitsCalculado


print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

