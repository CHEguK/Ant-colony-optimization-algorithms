# Ant-colony-optimization-algorithms
Простой муравьиный алгоритм для задачи коммивояжера / Ant colony optimization algorithm for travelling salesman problem

Вероятность перехода муравья из города i в город j определяется по формуле:
  choice = pheromone ** self.alpha * ((1.0/dist) ** self.beta)                (1)

Пошаговое описание:
1) Ввод матрицы расстояний - distation
2) Инициализация параметров:

a) num_ant - количество муравьёв в одной итерации
b) num_interations - количество итераций
c) decay - коэффициент испарения феромона
d) alpha - определяет влияние концетрации феромона на выбор муравья
e) beta - определяет влияние расстояния на выбор муравья
3) Создание единичной матрицы (pheromone) - начальная концетрация феромона

// Основной цикл
4) Цикл по колличеству итераций i=1, i=num_interations
  1. Цикл по всем муравьям k=1, k=num_ants
    a) В функции gen_way строится маршрут по формуле (1)
    b) В функции gen_path_dist расчитывается длина маршрута
  2. Конец цикла по муравьям (Получаем список с маршрутами и их длинами)
  
  3. Обновляем феромоны (def distribution_pheromone)
  
  4. Из всех маршрутов в итерации находим самый короткий - shortest_way
  5. Проверка на лучшее решение: сравниваем лучший маршрут из этой итерации(shortest_way) с самым лучшим маршрутов за всё
  время(all_time_shortest_way).
  6. Если shortest_way < all_time_shortest_way, то all_time_shortest_way = shortest_way
  
  7. Испарение феромона

4) Конец цикла по колличеству итераций

Получаем лучшее, найденное, решение при заданных параметрах.
  

    
    
