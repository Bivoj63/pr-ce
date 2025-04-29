skore = [5, 10, 20, 25, 30, 35, 40, 50, 55, 60]
print(skore)
print(("průměr:"),sum(skore)/10)
print(("nejvíc bodů:"),max(skore))
print(("nejmíň bodů:"),min(skore))
if sum(skore) > 500:
    print("výborná práce")
elif sum(skore) < 500:
    print("Můžete to příště zkusit lépe")