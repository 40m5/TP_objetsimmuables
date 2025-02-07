from dataclasses import dataclass
import asyncio
import random

@dataclass(frozen=True)
class Personne:
    nom: str
    age: int


p = Personne("Alice", 25)
print(p)  


def anniversaire(personnes):
    return [Personne(p.nom, p.age + 1) for p in personnes]


personnes = [Personne("Alice", 25), Personne("Bob", 30)]
nouvelle_liste = anniversaire(personnes)

print(nouvelle_liste)  


async def getRandomNumber():
    await asyncio.sleep(1)  
    return random.randint(1, 100)

async def main():
    number = await getRandomNumber()
    print(f"Nombre aléatoire : {number}")

asyncio.run(main())

async def main():
    num1, num2 = await asyncio.gather(getRandomNumber(), getRandomNumber())
    print(f"Nombre 1 : {num1}, Nombre 2 : {num2}")

asyncio.run(main())


