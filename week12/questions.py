import random

starter_Pokemon = ("Charmander", "Charmeleon", "Charzard", "MegaCharzard")
fire = (" FirePunch", " FlareBlitz", " BlastBurn", " Overheat")
normal = (" HyperBeam", " Helping hand", " BodySlam", " GigaImpact")
dragon = (" Outrage", " DragonPulse", " DragonClaw", " DragonDance")
flying = (" Huricane", " Fly", " AirSlash", " AirCutter")
 
print(random.choice(starter_Pokemon)+random.choice(fire)+
      random.choice(normal)+random.choice(dragon)+
      random.choice(flying))
      
