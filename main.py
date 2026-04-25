"""
Главный модуль для запуска симуляции экосистемы.
"""

import sys
from ecosystem import Ecosystem
from organism import Predator, Prey


def setup_initial_ecosystem() -> Ecosystem:
    """
    Создание начальной экосистемы с тестовыми организмами.
    
    Returns:
        Ecosystem: Настроенная экосистема
    """
    ecosystem = Ecosystem()
    
    # Создание хищников
    predators = [
        Predator("🦁 Лев", health=100, energy=90),
        Predator("🐺 Волк", health=85, energy=80),
    ]
    
    # Создание травоядных
    preys = [
        Prey("🐰 Заяц", health=70, energy=75),
        Prey("🦌 Олень", health=90, energy=85),
        Prey("🐑 Баран", health=75, energy=70),
        Prey("🐐 Коза", health=70, energy=65),
    ]
    
    # Добавление в экосистему
    for predator in predators:
        ecosystem.add_organism(predator)
    
    for prey in preys:
        ecosystem.add_organism(prey)
    
    return ecosystem


def main():
    """Главная функция запуска приложения."""
    try:
        # Настройка экосистемы
        ecosystem = setup_initial_ecosystem()
        
        # Запрос параметров симуляции
        print("\n⚙️ НАСТРОЙКИ СИМУЛЯЦИИ ⚙️")
        try:
            days = int(input("Введите количество дней симуляции (по умолчанию 10): ") or "10")
            days = max(1, min(100, days))  # Ограничение от 1 до 100
        except ValueError:
            days = 10
            print("Используется значение по умолчанию: 10 дней")
        
        # Запуск симуляции
        ecosystem.run_simulation(days)
        
        return 0
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Симуляция прервана пользователем")
        return 1
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())