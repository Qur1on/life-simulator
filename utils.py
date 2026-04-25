"""
Вспомогательные функции для симуляции экосистемы.
"""

import random
from typing import List, Any


def get_random_element(elements: List[Any]) -> Any:
    """
    Возвращает случайный элемент из списка.
    
    Args:
        elements: Список элементов
        
    Returns:
        Случайный элемент или None если список пуст
    """
    return random.choice(elements) if elements else None


def clamp(value: int, min_value: int, max_value: int) -> int:
    """
    Ограничивает значение в заданных пределах.
    
    Args:
        value: Исходное значение
        min_value: Минимальное значение
        max_value: Максимальное значение
        
    Returns:
        Ограниченное значение
    """
    return max(min_value, min(max_value, value))


def format_statistics(predators: int, preys: int, day: int) -> str:
    """
    Форматирует статистику для вывода.
    
    Args:
        predators: Количество хищников
        preys: Количество травоядных
        day: Номер дня
        
    Returns:
        Отформатированная строка со статистикой
    """
    return f"📊 День {day}: 🦁={predators} 🐰={preys}"