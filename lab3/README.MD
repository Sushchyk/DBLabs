<p align='center'>
<img src="https://raw.githubusercontent.com/Sushchyk/DBLabs/master/img/kpi.png">
</p>
<h1 align="center">Лабораторна робота №3
<h2 align="center">Розробка засобів кешування з використанням redis</h2>
<p align="right">Виконав студент групи КП-42 Сущик Андрій</p>
<p align="right">Варіант 19</p>
<a href="#Завдання">Завдання</a><br>
<a href="#Копії-екранних-форм">Копії екранних форм</a><br>
## Завдання 
Завдання роботи полягає у наступному:


1. Встановити сервер redis.


2. Розробити модуль кешування на основі пакету redis-py.


3. Підготувати тестові дані (50-100тис. документів MongoDB).


4. Реалізувати збереження результатів пошуку в базі даних redis (створити
кеш).


5. Реалізувати функцію отримання результатів пошуку з кешу, у випадку,
коли основна база даних не оновлювалась до створення кешу.


Функціональні вимоги


1. Згенерувати набір даних бази даних MongoDB у кількості 50-100 тис.
документів згідно із предметною галуззю.


2. Забезпечити створення кешу та підтримку його у актуальному стані за
допомогою сервера redis. Ключем кешу вибрати параметри пошуку,
обрані користувачем.


3. Перевірити швидкість отримання результатів пошуку з використанням
кешу та без нього.


## Копії екранних форм 
![Screenshot 1](https://raw.githubusercontent.com/Sushchyk/DBLabs/master/lab3/screenshoots/2.png)
![Screenshot 2](https://raw.githubusercontent.com/Sushchyk/DBLabs/master/lab3/screenshoots/1.png)
![Screenshot 3](https://raw.githubusercontent.com/Sushchyk/DBLabs/master/lab3/screenshoots/3.png)
