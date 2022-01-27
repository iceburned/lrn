skumriq = float(input())
caca = float(input())
palamud = float(input())
safrid = float(input())
midi = int(input())

palamud_cena = (skumriq + (skumriq * 0.60)) * palamud
safrid_cena = (caca + (caca * 0.80)) * safrid
midi_cena = 7.50 * midi
sum_sum = palamud_cena + safrid_cena + midi_cena
print(f'{sum_sum:.2f}')
