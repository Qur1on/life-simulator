"""
Простые тесты для экосистемы.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from organism import Predator, Prey
from ecosystem import Ecosystem


def test_add_organism():
    """Тест добавления организма."""
    try:
        eco = Ecosystem()
        lion = Predator("Лев")
        eco.add_organism(lion)
        assert len(eco.organisms) == 1
        print("✅ Тест 1 (добавление): пройден")
        return True
    except Exception as e:
        print(f"❌ Тест 1 (добавление): ошибка - {e}")
        return False


def test_remove_dead():
    """Тест удаления мёртвых."""
    try:
        eco = Ecosystem()
        dead = Predator("Мёртвый", health=0)
        alive = Predator("Живой", health=100)
        eco.add_organism(dead)
        eco.add_organism(alive)
        
        # Принудительно помечаем как мёртвого
        dead.is_alive = False
        dead.health = 0
        
        eco.remove_dead_organisms()
        assert len(eco.organisms) == 1
        assert eco.organisms[0].name == "Живой"
        print("✅ Тест 2 (удаление): пройден")
        return True
    except Exception as e:
        print(f"❌ Тест 2 (удаление): ошибка - {e}")
        return False


def test_find_prey():
    """Тест поиска жертвы."""
    try:
        eco = Ecosystem()
        rabbit = Prey("Заяц")
        eco.add_organism(rabbit)
        found = eco.find_random_prey()
        assert found is not None
        assert found.name == "Заяц"
        print("✅ Тест 3 (поиск жертвы): пройден")
        return True
    except Exception as e:
        print(f"❌ Тест 3 (поиск жертвы): ошибка - {e}")
        return False


def test_predator_energy_loss():
    """Тест потери энергии хищником."""
    try:
        eco = Ecosystem()
        wolf = Predator("Волк", energy=50)
        eco.add_organism(wolf)
        initial_energy = wolf.energy
        wolf.act(eco)
        assert wolf.energy < initial_energy
        print("✅ Тест 4 (потеря энергии): пройден")
        return True
    except Exception as e:
        print(f"❌ Тест 4 (потеря энергии): ошибка - {e}")
        return False


def test_prey_eating():
    """Тест поедания травы травоядным."""
    try:
        eco = Ecosystem()
        rabbit = Prey("Заяц", energy=30)
        eco.add_organism(rabbit)
        
        # Просто проверяем, что метод act работает без ошибок
        rabbit.act(eco)
        print("✅ Тест 5 (поедание травы): пройден")
        return True
    except Exception as e:
        print(f"❌ Тест 5 (поедание травы): ошибка - {e}")
        return False


def run_all_tests():
    """Запуск всех тестов."""
    print("\n" + "="*40)
    print("🧪 ЗАПУСК ТЕСТОВ")
    print("="*40 + "\n")
    
    tests = [
        test_add_organism,
        test_remove_dead,
        test_find_prey,
        test_predator_energy_loss,
        test_prey_eating
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("="*40)
    print(f"📊 РЕЗУЛЬТАТ: {passed}/{len(tests)} тестов пройдено")
    
    if passed == len(tests):
        print("✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
        print("="*40 + "\n")
        return True
    else:
        print(f"❌ НЕ ПРОЙДЕНО {len(tests) - passed} тестов")
        print("="*40 + "\n")
        return False


if __name__ == "__main__":
    run_all_tests()