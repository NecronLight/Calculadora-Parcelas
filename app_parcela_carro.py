valor_carro = float(input("Insira o valor do carro: "))

qnt_parcelas = 0

for _ in range(10):
    qnt_parcelas += 6
    print('Quantidade de parcelas:', qnt_parcelas,"x")
    valor_parcelado = ((qnt_parcelas/200) + 1)*valor_carro
    print('O valor parcelado é de R$: {:.2f}'.format(valor_parcelado))
    print('O valor de cada parcela é de R$: {:.2f}'.format(valor_parcelado/qnt_parcelas))
    print(" ")

