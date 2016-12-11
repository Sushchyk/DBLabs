<p align='center'>
<img src="https://raw.githubusercontent.com/Sushchyk/DBLabs/master/img/kpi.png">
</p>
<h1 align="center">Лабораторна робота №2
<h2 align="center">Розробка Web-орієнтованого додатку з використанням
документоорієнтованої СУБД MongoDB</h2>
<p align="right">Виконав студент групи КП-42 Сущик Андрій</p>
<p align="right">Варіант 19</p>
<a href="#Завдання">Завдання</a><br>
<a href="#Функції-mapreduce-та-aggregate">Функції Map/Reduce та aggregate()</a><br>
<a href="#Копії-екранних-форм">Копії екранних форм</a><br>

## Завдання 
Завдання роботи полягає у наступному:


1. Розробити схему бази даних на основі предметної галузі з ЛР№2-Ч1 у
спосіб, що застосовується в СУБД MongoDB.


2. Розробити модуль роботи з базою даних на основі пакету PyMongo.


3. Реалізувати дві операції на вибір із використанням паралельної обробки
даних Map/Reduce.


4. Реалізувати обчислення та виведення результату складного агрегативного
запиту до бази даних з використанням функції aggregate() сервера
MongoDB.


Функціональні вимоги


1. Перетворити сутності діаграми «сутність-зв’язок», розробленої в ЛР№2-
Ч1, у структури, прийнятні для обробки pymongo з урахуванням
можливості збереження сутностей у середині інших (вкладення
сутностей).


2. Забезпечити реалізацію функцій редагування, додавання та вилучення
інформації в центральну «сутність», отриману зі схеми «зірка».


3. Забезпечити реалізацію 2-х функцій агрегування даних за допомогою
технології Map/Reduce. Функції обрати самостійно з заданої предметної
галузі.


4. Забезпечити реалізацію операції агрегування даних за допомогою
технології вбудованої у MongoDB функції aggregate(). Операцію обрати
самостійно з заданої предметної галузі, але вона має містити засоби
групування, сортування, фільтрації та реконструкції масиву ($unwind)

## Функції Map/Reduce та aggregate()
```
 def sumByCountry(self):
        map = Code("""function(){
                              emit(this.country.name, this.price);
        		           };
        		           """)

        reduce = Code("""
        					  function(key, valuesPrices){
        						var sum = 0;
        						for (var i = 0; i < valuesPrices.length; i++) {
        						  sum += valuesPrices[i];
        						}
        						return sum;
        		              };
        		              """)
        results = self.db.players.map_reduce(map, reduce, "sum_by_country")
        return results.find()
```
```
     def sumByTeam(self):
        map = Code("""function(){
                              emit(this.team.full_name, this.price);
        		           };
        		           """)

        reduce = Code("""
        					  function(key, valuesPrices){
        						var sum = 0;
        						for (var i = 0; i < valuesPrices.length; i++) {
        						  sum += valuesPrices[i];
        						}
        						return sum;
        		              };
        		              """)
        results = self.db.players.map_reduce(map, reduce, "sum_by_team")
        return results.find()
```
```
    def countOfByPlayersByPositions(self):
        pipeline = [
            {"$unwind": "$position"},
            {"$group": {"_id": "$position.name", "count": {"$sum": 1}}},
            {"$sort": SON([("count", -1)])}
        ]
        return list(self.db.players.aggregate(pipeline))
````
## Копії екранних форм 
![Screenshot 1](https://raw.githubusercontent.com/Sushchyk/DBLabs/master/lab2/screenshots/1.png)
![Screenshot 1](https://raw.githubusercontent.com/Sushchyk/DBLabs/master/lab2/screenshots/2.png)

