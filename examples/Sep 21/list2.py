print("Footbal Favorites!")
teams = ["The Saints", "Ravens", "The RedSkins", "49ers",
"Giants"]

for team in teams:
    print(f"- {team}")

while True:
    cont = input("Do you want to remove any teams? ").strip().lower()
    if cont != "y":
        break       #leave program
    teamname = input("Enter Team Name: ")
    teams.remove(teamname)
print("Goodbye")
