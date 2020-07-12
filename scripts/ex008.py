# Escreva um programa que leia um valor em metros e o exiba convertendo e, centímetros e milímetros

medida = float(input('Digite uma distância em metros: '))
print(
    'A medida de {} m corresponde a:\n{:.3f} km.\n{:.2f} hm.\n{:.2f} dam.\n{} dm.\n{} cm.\n{} mm.'.format(
    (medida),
    (medida/1000),
    (medida/100),
    (medida/10),
    (medida*10),
    (medida*100),
    (medida*1000)
))
