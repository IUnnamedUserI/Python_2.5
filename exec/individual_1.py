#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = tuple(map(int, input("Введите оценки учеников: ").split()))
    print(f"Количество оценок: {len(a)}")
    print(f"Количество пятёрок: {a.count(5)}")
    