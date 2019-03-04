import sys
import numpy as np
from numpy.random import choice as np_choice


class AntColony(object):
	def __init__(self, distances, num_ants, num_interations, decay, alpha=1, beta=1):
		
		self.distances = distances										# Матрица расстояний
		self.pheromone = np.ones(self.distances.shape) / len(distances)	# Матрица феромонов
		self.all_city = range(len(distances))							# Все города
		self.num_ants = num_ants										# Количество муравьёв	(int)
		self.num_interations = num_interations							# Кол-во интераций		(int)
		self.decay = decay												# Коэффициент испарения	(float)
		self.alpha = alpha												# alpha					(float)
		self.beta = beta												# betta					(float)
    
	def run(self):									# Основная функция
		shortest_way = None
		all_time_shortest_way = ("route", np.inf)
		for i in range(self.num_interations):
			all_route = self.gen_all_route()
			self.distribution_pheromone(all_route, self.num_ants, shortest_way=shortest_way)
			shortest_way = min(all_route, key=lambda x: x[1])
			
			
			if (shortest_way[1] < all_time_shortest_way[1]):	#Нахождение самого короткого пути
				all_time_shortest_way = shortest_way
			self.pheromone * self.decay							#Испарение феромонов
		
		return all_time_shortest_way[1]
	
	def distribution_pheromone(self, all_route, num_ants, shortest_way):	# Добавление феромонов на участки по которым пробегали муравьи 
		sorted_way = sorted(all_route, key=lambda x: x[1])						# Вход: (Все маршруты муравьёв в этой итерации, количество муравьёв, кротчайший путь)
		for way, dist in sorted_way[:num_ants]:
			for move in way:
				self.pheromone[move] += 1/self.distances[move]
				
	
	def gen_path_dist(self, way):					# Считает длину пути муравья Вход:(Маршрут муравья)
		total_distance = 0
		for l in way:
			 total_distance += self.distances[l]
		return total_distance						# Выход: (Длина маршрута)
	
	def gen_all_route(self):						# Формируем маршруты всех муравёв
		all_route = []
		for i in range(self.num_ants):
			way = self.gen_way(0)			# Город отправления.       Чтобы город отправления ждя каждого муравья выбирался рандомно: rn.randrange(0, len(self.distances))
			all_route.append((way, self.gen_path_dist(way)))
		return all_route							# Выход: (список маршрутов всех муравьёв и его длина)
		
	def gen_way(self, start):						# Формируем муршрут каждого муравья						
		way = []
		visited = set()
		visited.add(start)
		prev = start
		for i in range(len(self.distances)-1):
			move = self.pick_move(self.pheromone[prev], self.distances[prev], visited)
			way.append((prev, move))
			prev = move
			visited.add(move)
		way.append((prev, start))			# Возврат в начальную точку
		return way									# Выход: (список маршрута муравья)
		
	def pick_move(self, pheromone, dist, visited):	# Функция выбора следующего города Вход: ( Массив феромонов в следующие города, Массив расстояний до след городов, кортеж с первым городом)
		pheromone = np.copy(pheromone)
		pheromone[list(visited)] = 0
		
		choice = pheromone ** self.alpha * ((1.0/dist) ** self.beta)		# Вероятность перехода из вершины i в вершину j 
		
		norm_choice = choice / choice.sum()		# Нормирование
		
		move = np_choice(self.all_city, 1, p=norm_choice) [0]		# Выбор маршрута
		return move



#Входные данные
np.random.seed(7)
distances = np.random.randint(1, 50, size=(20, 20))

distances = np.array([[0, 2, 30, 9, 1],
                     [4, 0, 47, 7, 7],
                    [31, 33, 0, 33, 36],
                     [20, 13, 16, 0, 28],
                    [9, 36, 22, 22, 0]])

#a = sys.stdin.read()
#list_of_lists=[]

#for line in a.split('\n'):
#    new_list = [int(elem) for elem in line.split()]
#    list_of_lists.append(new_list)
#del list_of_lists[-1]

#distances = np.array(list_of_lists)

i=0
j=0
#изменнение главное диагонали, чтобы нельзя было пройти из города в тот же город
for p in range(len(distances)):
	distances[i][j]=9999
	i+=1
	j+=1


ant_colony = AntColony(distances, 5, 100, 0.95, alpha=1, beta=2)	# Запуск алгоритма
shortest_path = ant_colony.run()									# Получение самого короткого пути
sys.stdout.write(str(shortest_path))


