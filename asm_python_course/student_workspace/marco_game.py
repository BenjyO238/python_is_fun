import time

demon_health = 100
your_health = 100

name = input("Enter your name to enter into doom...: ")
time.sleep(0.5)
print("Hello,", name)
time.sleep(1)
print("You are now in doom...")
print("Entering you into the game.")
time.sleep(1)
print("Entering you into the game..")
time.sleep(1)
print("Entering you into the game...")
time.sleep(2)

print("hello", name)
time.sleep(2)
print("i see that you have joined the doom game")
time.sleep(2)
crok = input("nice to meet you, even if you cant see me, my name is crok.")
time.sleep(4)
name = input("Im sorry what is your name again, I forgot.")
time.sleep(3)
accepted = input(f"you have an adventure to do, do you accept {name}?")
time.sleep(2)

if accepted.strip() == "yes" or accepted.strip() == "yeah" or accepted.strip(
) == "yep" or accepted.strip() == "yea":
  print("ok let you go on your adventure!")
else:
  print("ok your loss not playing.")
  exit()

print("you are walking to the gates of darkness and you go through")
time.sleep(3)
print("as you walk some demon wants to battle you! you have to fight him!")
time.sleep(3)
print("YOU HAVE ENGAGED IN A BATTLE WITH A DEMON!")
time.sleep(3)
print("the demon has 100 HP! and you have 100 HP!")
time.sleep(1)
print("you have your hands as your weapons, what will you do?")
time.sleep(3)
print("attack,")
time.sleep(1)
print("defend,")
time.sleep(1)
print("or run?")
time.sleep(1)
choice = input("what will you do?")
if choice.strip() == "attack":
  demon_health -= 10
  print(
      f"you attacked the demon and did 10 damage! Now he has {demon_health} health!"
  )
if choice.strip() == "defend": your_health -= 5
print(f"you defended and took 5 damage! Now you have {your_health} health!")
if choice.strip() == "run": exit()
print("the demon attacks you and does 10 damage! now you have 90 health!")
input("what will you do?")
