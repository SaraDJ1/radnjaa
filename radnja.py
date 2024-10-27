proizvodi={
    "jakna":4000,
    "bojice":120,
    "telefon":670000,
    "lubenica":200}
ime_proizvoda=input("Sta ste kupili od proizvoda?")
kolicina=int(input("Koliko komada?"))
cena=proizvodi[ime_proizvoda]
ukupna_cena= cena * kolicina
if kolicina>=10:
    print("Vasa cena je:",ukupna_cena * 0.9)
elif kolicina>=20:
    print("Vasa cena je:",ukupna_cena * 0.8)