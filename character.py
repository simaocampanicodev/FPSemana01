characters = []
count = 3
for i in range (count):
    name = str(input(""))
    attack = int(input(""))
    defense = int(input(""))
    character = ([name, (attack, defense)])
    characters.append(character)
    
print (characters)

max_attack = -1
max_defense = -1
max_attack_character = None
max_defense_character = None

for character in characters:
    if (character[1][0]) > max_attack:
        max_attack = (character[1][0])
        max_attack_character = character
    if (character[1][1]) > max_defense:
        max_defense = (character[1][1])
        max_defense_character = character

print(("Ataque ") + str(max_attack_character[0]) + " "  + str(max_attack_character[1][0]))
print(("Defesa ") + str(max_defense_character[0]) + " " + str(max_defense_character[1][1]))