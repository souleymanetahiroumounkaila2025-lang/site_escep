
import requests
ville = input("Entrer le nom d'une ville: ")
temp = requests.get(f"https://wttr.in/{ville}?format=%t").text
print(f"ville:{ville}\ntemperature actuelle:{temp}")

