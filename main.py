from abc import ABC, abstractmethod
import random
import asyncio
from typing import List, Tuple


class Frog(ABC):
    """Базовый класс жабы"""

    def __init__(self) -> None:
        self.attack: int = 15
        self.health: int = 150
        self.armor: int = 5

    @abstractmethod
    def modify_params(self) -> None:
        """Функция для модификации жабы"""
        pass

    def calculate_armor(self) -> int:
        """Расчет урона"""
        return random.randint(0, self.armor)

    def calculate_damage(self) -> int:
        """Расчет брони"""
        return random.randint(self.attack // 2, int(self.attack))


class Assassin(Frog):
    """Класс Ассасина"""

    def modify_params(self) -> None:
        self.health = int(self.health * 1.25)


class Adventurer(Frog):
    """Класс Авантюриста"""

    def modify_params(self) -> None:
        self.attack = int(self.attack * 1.5)


class Craftsman(Frog):
    """Класс Ремесленника"""

    def modify_params(self) -> None:
        self.armor *= 2


async def fight(frog1: Frog, frog2: Frog) -> int:
    """Функция боя между двумя жабами"""

    while frog1.health > 0 and frog2.health > 0:
        frog1_damage: int = frog1.calculate_damage() - frog2.calculate_armor()
        frog2.health -= frog1_damage
        if frog2.health <= 0:
            return 1
        frog2_damage: int = frog2.calculate_damage() - frog1.calculate_armor()
        frog1.health -= frog2_damage
        if frog1.health <= 0:
            return 2


async def battle() -> Tuple[int, int]:
    """Функция боев"""

    frog_class: List[type] = [Assassin, Adventurer, Craftsman]
    score: List[int] = [0, 0]

    for _ in range(100):
        frog1: Frog = random.choice(frog_class)()
        frog1.modify_params()
        frog2: Frog = random.choice(frog_class)()
        frog2.modify_params()
        champion: int = await fight(frog1, frog2)
        score[champion - 1] += 1
    return tuple(score)


async def main() -> None:
    """Главная функция"""

    results: List[Tuple[int, int]] = await asyncio.gather(battle(), battle())
    for i, result in enumerate(results):
        print(f"Результаты {i + 1}-го цикла боев:")
        print(f"Победы первой жабы: {result[0]}")
        print(f"Победы второй жабы: {result[1]}")


if __name__ == "__main__":
    asyncio.run(main())
