import math


prestacao = float (input("coloque a prestação: "))
vprestacao = float (input("coloque o valor da prestação: "))
multa = float (input("coloque o valor da multa: "))
dias = float (input ("quantidade de dias de atraso: "))



resultado = vprestacao + vprestacao*(multa/ 100)*dias

print ("o valor do resultado é ", resultado)