import random

print("Welcome to beat the zombie a game where a party fights a evil zombie. Where you select the attacks of the hero's in your party and try and defeat the zombie! Also a reminder please use spaces when you are inputing something.")
Difficulty = ["Easy", "Medium", "Hard"]
print(Difficulty)   
SelectedDifficulty = input("Please Select a Difficulty")


party = ["Wizard", "Warrior", "Cleric"]
ZombieDead = False
ClericDead = False
WarriorDead = False
WizardDead = False
PartyDead = False
WizardHealth = 25
WarriorHealth = 30
ClericHealth = 20
PartyHealth = WizardHealth + WarriorHealth + ClericHealth #Its 65
ZombieHealth = 100
if SelectedDifficulty == (" Easy"):
  ZombieHealth = 30
elif SelectedDifficulty == (" Medium"):
  ZombieHealth = 200
elif SelectedDifficulty == (" Hard"):
  ZombieHealth = 350
print("The zombie battlelord has appeared quickly now we must defeat him!")
WizardAttacks = ["Fire", "Thunder", "Ice"]
WarriorAttacks = ["Slice", "Whirlwind"]
ClericAttacks = ["Heal", "Holy"]
ZombieAttacks = ["Slam", "Death"]
ZombieShocked = False

while PartyHealth > 0:
  print(WizardAttacks)
  Wizardattack = input("Its the wizards turn!")
  if Wizardattack == (" Fire" or "Fire"):
    print("You have burned the zombie!")
    ZombieHealth -= 25
    print(ZombieHealth)
  elif Wizardattack == (" Thunder" or "Thunder"):
    print("You have shocked the zombie!")
    ZombieHealth -= 15
    ZombieShocked = True
    print(ZombieHealth)
  elif Wizardattack == (" Ice" or "Ice"):
    print("You have frozen the zombie!")
    ZombieHealth -= 20
    print(ZombieHealth)
  if ZombieHealth <= 0:
    print("You have won! The Zombie is dead")
    ZombieDead = True
  if ZombieDead == True:
    break
  print(WarriorAttacks)
  Warriorattack = input("Its now the Warriors turn!")
  if Warriorattack == (" Slice" or "Slice"):
    print("You have sliced up the Zombie dealing 10 damage!")
    ZombieHealth -= 10
    print(ZombieHealth)
  elif Warriorattack == (" Whirlwind"):
    print("The Zombie Is winded!")
    ZombieHealth -= 15
    print(ZombieHealth)
  if ZombieHealth <= 0:
    print("You have won! The Zombie is dead")
    ZombieDead = True
  if ZombieDead == True:
    break
  print(ClericAttacks)
  Clericattack = input("Its the holy clerics turn!")
  if Clericattack == (" Heal" or " Heal"):
    healed = input("Choose a party member to heal!")
    if healed == (" Warrior"):
      WarriorHealth += 10
      print("You have healed the warrior!")
      print(WarriorHealth)
    elif healed == (" Wizard"):
      WizardHealth += 10
      print("You have healed the wizard!")
      print(WizardHealth)
    elif healed == (" Cleric"):
      ClericHealth += 10
      print("The cleric choose to heal himself")
      print(ClericHealth)
  elif Clericattack == (" Holy" or "Holy"):
    print("The zombie has been hit with holy magic!")
    ZombieHealth -= 10
    print(ZombieHealth)
  print("Oh no its the zombies turn to attack watch out for his slam!")
  if ZombieShocked == True:
    print("Your thunder spell shocked the zombie!")
    ZombieHealth -= 15
    print(ZombieHealth)
    ZombieShocked = False
  if ZombieHealth <= 0:
    print("You have won! The Zombie is dead")
    ZombieDead = True
  if ZombieDead == True:
    break
  Zombieattack = random.randint(1,2)
  if Zombieattack == 1:
    print("Oh no it's his slam attack!")
    SlamTarget = random.randint(1,3)
    if SlamTarget == 1:
      print("Oh no the wizard was hit with the slam!")
      WizardHealth -= 5
      print(WizardHealth)
    if SlamTarget == 2:
      print("Oh no the Warrior was hit with the slam!")
      WarriorHealth -= 10
      print(WarriorHealth)
    if SlamTarget == 3:
      print("Oh no the Cleric was hit with the slam!")
      ClericHealth -= 5
      print(ClericHealth)
  if Zombieattack == 2:
    print("Oh no he has casted his death spell!")
    WizardHealth -= 10
    ClericHealth -= 10
    WarriorHealth -= 10
    print(WizardHealth)
    print(WarriorHealth)
    print(ClericHealth)
    print("The entire party has been hit with his death spell!")
  if ZombieHealth <= 0:
    print("You have won! The Zombie is dead")
    ZombieDead = True
  if ZombieDead == True:
    break
  if WizardHealth <= 0:
    WizardDead = True
    print("Oh no the Wizard is dead! RETREAT")
    break
    PartyDead = True
  if WarriorHealth <= 0:
    WarriorDead = True
    print("Oh no the Warrior is dead! RETREAT")
    break
    PartyDead = True
  if ClericHealth <= 0:
    ClericDead = True
    print("Oh no the Cleric is dead! RETREAT")
    break
    PartyDead = True

if ZombieDead == True:
  print("The Battle is over we have won!")
if PartyDead == True:
  print("Oh no we have lost the entire world is doomed!")