print("Simple Currency Converter")
print("--------------------------------------------------------------------------------")
print("Available currencies: USD,EUR, INR, GBP, JPY, AUD, CAD, CHF, CNY, NZD, SEK, ZAR, SGD, MXN, KRW, TRY")

print("""
*** Currency Converter Glossary ***

USD — United States Dollar
EUR — Euro (European Union)
INR — Indian Rupee
GBP — British Pound Sterling
JPY — Japanese Yen
AUD — Australian Dollar
CAD — Canadian Dollar
CHF — Swiss Franc
CNY — Chinese Yuan (Renminbi)
NZD — New Zealand Dollar
SEK — Swedish Krona
ZAR — South African Rand
SGD — Singapore Dollar
MXN — Mexican Peso
KRW — South Korean Won
TRY — Turkish Lira
""")


rates = {
    
  "USD": 1.0,
  "EUR": 0.88,
  "INR": 85.5,
  "GBP": 0.74,
  "JPY": 144.0,
  "AUD": 1.56,
  "CAD": 1.38,
  "CHF": 0.82,
  "CNY": 7.19,
  "NZD": 1.68,
  "SEK": 9.59,
  "ZAR": 17.88,
  "SGD": 1.29,
  "MXN": 19.33,
  "KRW": 1381.0,
  "TRY": 39.24    
}

while True:
    from_cur = input("From currency: ").upper()ss
    to_cur = input("To currency: ").upper()

    if from_cur not in rates or to_cur not in rates:
        print("Invalid currency, try again.")
        continue

    amount = float(input(f"Enter amount in {from_cur}: "))
    usd = amount / rates[from_cur]
    converted = usd * rates[to_cur]

    print(f"{amount} {from_cur} = {converted}{to_cur}")

    again = input("Need to check more currency values? Go ahead, just type yes if not enter no  ").lower()
    if again != 'yes':
        print("“Thanks for using the currency converter! If you need more conversions later, just come back anytime. Goodbye!”")
        break
