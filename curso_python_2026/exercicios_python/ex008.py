medida = float(input('Digite o valor em metros: '))
km = medida / 1000
hm = medida / 100
dm = medida / 10
cm = medida * 100
mm = medida * 1000
print('A conversão de {}m corresponde a:'.format(medida))
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dm'.format(dm))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))