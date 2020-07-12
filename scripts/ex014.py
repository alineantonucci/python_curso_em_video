# Conversor de temperatura

celsius = float(input('Informe a temperatura em ºC: '))
print('A temperatura de {}ºC, corresponde a {}ºF e {}ºK.'
      .format(celsius,
              celsius * 1.8 + 32,celsius + 273,17))
