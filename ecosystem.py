"""
Модуль экосистемы, управляющий всеми организмами и их взаимодействиями.
"""

from typing import List, Optional
import random
from organism import Organism, Predator, Prey


class Ecosystem:
    """
    Класс экосистемы, содержащий всех организмов и управляющий симуляцией.
    
    Attributes:
        organisms (List[Organism]): Список всех организмов
        day (int): Текущий день симуляции
    """
    
    def __init__(self):
        """Инициализация пустой экосистемы."""
        self.organisms: List[Organism] = []
        self.day = 0
    
    def add_organism(self, organism: Organism) -> None:
        """
        Добавление организма в экосистему.
        
        Args:
            organism: Добавляемый организм
        """
        self.organisms.append(organism)
        print(f"➕ {organism.name} добавлен в экосистему")
    
    def remove_dead_organisms(self) -> int:
        """
        Удаление всех мёртвых организмов.
        
        Returns:
            int: Количество удалённых организмов
        """
        initial_count = len(self.organisms)
        self.organisms = [org for org in self.organisms if org.is_alive]
        removed = initial_count - len(self.organisms)
        if removed > 0:
            print(f"🗑️ Удалено мёртвых организмов: {removed}")
        return removed
    
    def find_random_prey(self) -> Optional[Prey]:
        """
        Поиск случайной жертвы среди живых организмов.
        
        Returns:
            Optional[Prey]: Объект жертвы или None
        """
        prey_list = [org for org in self.organisms 
                    if isinstance(org, Prey) and org.is_alive]
        return random.choice(prey_list) if prey_list else None
    
    def reproduce_organisms(self) -> None:
        """Размножение организмов при достаточной энергии."""
        new_organisms = []
        
        for org in self.organisms:
            if org.is_alive and org.energy > 70 and random.random() < 0.2:
                # Создание потомка
                if isinstance(org, Prey):
                    child = Prey(f"{org.name} Jr.", 
                                health=org.health // 2,
                                energy=org.energy // 2)
                elif isinstance(org, Predator):
                    child = Predator(f"{org.name} Jr.",
                                    health=org.health // 2,
                                    energy=org.energy // 2)
                else:
                    continue
                
                new_organisms.append(child)
                org.energy -= 20
                print(f"👶 Новый организм: {child.name}")
        
        self.organisms.extend(new_organisms)
    
    def simulate_day(self) -> None:
        """Симуляция одного дня в экосистеме."""
        self.day += 1
        print(f"\n{'='*50}")
        print(f"🌍 ДЕНЬ {self.day}")
        print(f"{'='*50}")
        
        # Все организмы совершают действия
        for organism in self.organisms[:]:  # Копия списка
            if organism.is_alive:
                organism.act(self)
        
        # Удаление мёртвых и размножение
        self.remove_dead_organisms()
        self.reproduce_organisms()
        
        # Вывод статистики
        self.print_statistics()
    
    def print_statistics(self) -> None:
        """Вывод статистики экосистемы."""
        predators = sum(1 for org in self.organisms 
                       if isinstance(org, Predator) and org.is_alive)
        preys = sum(1 for org in self.organisms 
                   if isinstance(org, Prey) and org.is_alive)
        
        print(f"\n📊 Статистика дня {self.day}:")
        print(f"   🦁 Хищники: {predators}")
        print(f"   🐰 Травоядные: {preys}")
        print(f"   📈 Всего: {len(self.organisms)}")
        
        # Детальный список
        print("\n🏞️ Текущие обитатели:")
        for org in self.organisms:
            print(f"   {org}")
    
    def run_simulation(self, days: int = 10) -> None:
        """
        Запуск симуляции на определённое количество дней.
        
        Args:
            days: Количество дней симуляции
        """
        print("🚀 ЗАПУСК СИМУЛЯЦИИ ЭКОСИСТЕМЫ 🚀")
        print(f"📅 Планируется дней: {days}\n")
        
        for _ in range(days):
            self.simulate_day()
            
            # Проверка на вымирание
            if len(self.organisms) == 0:
                print("\n💔 ЭКОСИСТЕМА ПОГИБЛА! 💔")
                break
        
        print("\n" + "="*50)
        print("🎬 СИМУЛЯЦИЯ ЗАВЕРШЕНА 🎬")
        self.print_statistics()
#test