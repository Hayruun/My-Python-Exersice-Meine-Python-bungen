# 1- "Bmw, Mercedes, Opel, Mazda" elemanalarına sahip bir liste oluşturunuz.

listAutos=['Bmw','Mercedes','Opel','Mazda']

# 2- Liste kaç elemanlıdır ?
print(len(listAutos))

# 3- Listenin ilk ve son elemanı nedir ?
print('Listenin ilk elemanı:',listAutos[0])
# result = listAutos[0]
#print(result)
print('Listenin son elemanı:',listAutos[3])

# 4- Mazda değerini Toyota ile değiştirin.
listAutos[-1] = 'Toyota'
print(listAutos)
# 5- Mercedes listenin bir elemanı mıdır ?
result = 'Mercedes' in listAutos
print(result)
# 6- Listenin -2 indeksindeki değer nedir?
result = listAutos[-2]
print(result)
# 7- Listenin ilk 3 elemanını alın.
result = listAutos[0:3]
print(result)
# 8- Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
#listAutos[-2] = 'Toyota'
#listAutos[-1] = 'Renault'
listAutos[-2:] = ['Toyota','Renault']
print(listAutos)
# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
#listAutos.append('Audi')
#listAutos.append('Nissan')
#print(listAutos)
result = listAutos + ['Audi','Nissan']
print(result)
# 10- Listenin son elemanını silin.
#listAutos.remove[-1]
#print(listAutos)
del listAutos[-1]
result = listAutos
# 11- Liste elemanlarını tersten yazdırınız.
result = listAutos[::-1]
print(result)
# 12- Aşağıdaki verileri bir liste içinde saklayınız.
studentA = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB = ['Sena','Turan',1999,[80,80,70]]
studentC = ['Ahmet','Turan',1998,[80,70,90]]

# Liste elemanlarını ekrana yazdırınız.

result = studentA[0]
result = studentB[1]
result = studentC[3][1]

result = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"
print(result)
