"""
Модуль с классами организмов для экосистемы.
Содержит базовый класс Organism и специфичные классы Predator и Prey.
"""

from abc import ABC, abstractmethod
import random
from typing import Optional


class Organism(ABC):
    """
    Абстрактный базовый класс для всех организмов в экосистеме.
    
    Attributes:
        name (str): Имя/вид организма
        health (int): Здоровье (0-100)
        energy (int): Энергия (0-100)
        is_alive (bool): Жив ли организм
    """
    
    def __init__(self, name: str, health: int = 100, energy: int = 100):
        """
        Инициализация организма.
        
        Args:
            name: Имя организма
            health: Начальное здоровье
            energy: Начальная энергия
        """
        self.name = name
        self.health = max(0, min(100, health))
        self.energy = max(0, min(100, energy))
        self.is_alive = True
    
    @abstractmethod
    def act(self, ecosystem) -> None:
        """
        Абстрактный метод действия организма в экосистеме.
        
        Args:
            ecosystem: Ссылка на экосистему для взаимодействия
        """
        pass
    
    def take_damage(self, damage: int) -> None:
        """
        Получение урона организмом.
        
        Args:
            damage: Количество урона
        """
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False
            self.health = 0
            print(f"💀 {self.name} погиб!")
    
    def restore_health(self, amount: int) -> None:
        """Восстановление здоровья."""
        self.health = min(100, self.health + amount)
    
    def consume_energy(self, amount: int) -> bool:
        """
        Расход энергии.
        
        Returns:
            bool: Достаточно ли энергии для действия
        """
        if self.energy >= amount:
            self.energy -= amount
            return True
        return False
    
    def gain_energy(self, amount: int) -> None:
        """Пополнение энергии."""
        self.energy = min(100, self.energy + amount)
    
    def __str__(self) -> str:
        status = "🟢" if self.is_alive else "💀"
        return f"{status} {self.name} (❤️:{self.health} ⚡:{self.energy})"


class Prey(Organism):
    """Травоядное животное - жертва."""
    
    def __init__(self, name: str, health: int = 80, energy: int = 80):
        super().__init__(name, health, energy)
        self.type = "prey"
    
    def act(self, ecosystem) -> None:
        """Действие травоядного: поиск еды или побег."""
        if not self.is_alive:
            return
        
        # Расход энергии на жизнедеятельность
        if not self.consume_energy(5):
            self.take_damage(10)
            return
        
        # 40% шанс поиска еды
        if random.random() < 0.4:
            food_amount = random.randint(10, 30)
            self.gain_energy(food_amount)
            self.restore_health(5)
            print(f"🌿 {self.name} съел траву +{food_amount} ⚡")
    
    def escape(self) -> bool:
        """Попытка убежать от хищника."""
        escape_chance = 0.5 + (self.energy / 200)
        return random.random() < escape_chance


class Predator(Organism):
    """Хищное животное - охотник."""
    
    def __init__(self, name: str, health: int = 100, energy: int = 100):
        super().__init__(name, health, energy)
        self.type = "predator"
    
    def act(self, ecosystem) -> None:
        """Действие хищника: охота."""
        if not self.is_alive:
            return
        
        # Расход энергии на жизнедеятельность
        if not self.consume_energy(8):
            self.take_damage(15)
            return
        
        # Поиск жертвы
        prey = ecosystem.find_random_prey()
        if prey and random.random() < 0.6:
            self.hunt(prey)
        else:
            print(f"🦁 {self.name} не нашёл добычу, теряет энергию")
    
    def hunt(self, prey: Prey) -> None:
        """
        Охота на жертву.
        
        Args:
            prey: Объект жертвы
        """
        damage = random.randint(15, 35)
        print(f"⚔️ {self.name} атакует {prey.name}! Урон: {damage}")
        
        # Жертва пытается убежать
        if prey.escape():
            print(f"🏃 {prey.name} убежал!")
            self.consume_energy(5)
        else:
            prey.take_damage(damage)
            self.gain_energy(damage // 2)
            
            if not prey.is_alive:
                print(f"🍖 {self.name} съел {prey.name}!")