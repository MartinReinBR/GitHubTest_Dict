telRegister = {}
for i in range(0,5):
    inp = input("Mata in Namn och Telefonnummer spearerat med ett _: ")
    parts = inp.split("_")
    namn = parts[0]
    tel = parts[1]
    telRegister[namn] = tel

while True:
    namn = input("Mata in namn du vill söka på: ")
    if namn in telRegister:
        print(telRegister[namn])
    else:
        print("Namn inte hittat.")

print("Hello")