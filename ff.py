
print("=== Välkommen till frågesporten! ===")
print("Svara på frågorna och försök få så många poäng som möjligt.")
print()

poang = 0

fragor = [
    {
        "fraga": "1. Vad heter Sveriges huvudstad?",
        "alternativ": ["A. Göteborg", "B. Stockholm", "C. Malmö"],
        "svar": "B"
    },
    {
        "fraga": "2. Hur många ben har en spindel?",
        "alternativ": ["A. 6", "B. 8", "C. 10"],
        "svar": "B"
    },
    {
        "fraga": "3. Vilket språk används i detta program?",
        "alternativ": ["A. Python", "B. Java", "C. HTML"],
        "svar": "A"
    },
    {
        "fraga": "4. Vad är 7 * 8?",
        "alternativ": ["A. 54", "B. 56", "C. 64"],
        "svar": "B"
    },
    {
        "fraga": "5. Vilken planet kallas den röda planeten?",
        "alternativ": ["A. Mars", "B. Venus", "C. Jupiter"],
        "svar": "A"
    }
]

for fraga in fragor:
    print(fraga["fraga"])

    for alternativ in fraga["alternativ"]:
        print(alternativ)

    svar = input("Ditt svar (A, B eller C): ").upper()

    if svar == fraga["svar"]:
        print("Rätt svar! +1 poäng")
        poang += 1
    else:
        print("Fel svar!")
        print("Rätt svar var", fraga["svar"])

    print()

print("=== QUIZET ÄR SLUT! ===")
print("Du fick", poang, "av", len(fragor), "poäng.")

if poang == 5:
    print("Perfekt! Du fick alla rätt!")
elif poang >= 3:
    print("Bra jobbat!")
else:
    print("Försök igen så går det ännu bättre!")
