wzrost = int(input("Podaj wzrost w centymetrach:"))
masa = int(input("Podaj mase ciala w kilogramach: "))
wzrost_metr = wzrost/100
bmi = masa / (wzrost_metr)**2
if bmi < 18.5:
    print(f"Twoje BMI wynosi {bmi} masz niedowage")
elif 18.5 <= bmi <= 24.9:
    print(f"Twoje BMI wynosi {bmi} masz wage prawidlowa")
elif 25 <= bmi <= 29.9:
    print(f"Twoje BMI wynosi {bmi} masz nadwage")
else:
    print(f"Twoje BMI wynosi {bmi} jestes otyly")