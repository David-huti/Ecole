
def time_to_text(minutes):
 heures = minutes // 60
 minutes_restantes = minutes % 60
 print(heures, "heures et", minutes_restantes, "minutes")

 
input_minutes = int(input("Entrez le nombre de minutes : "))
time_to_text(input_minutes)