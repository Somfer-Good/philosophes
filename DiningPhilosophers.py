import random, signal
from Philosopher import Philosopher
from Fork import Fork

f1 = Fork('f1')
f2 = Fork('f2')
f3 = Fork('f3')
f4 = Fork('f4')
f5 = Fork('f5')

names = ['Philosopher_1','Philosopher_2','Philosopher_3','Philosopher_4','Philosopher_5']
random.shuffle(names)

p1 = Philosopher(names[0], f1, f2)
p2 = Philosopher(names[1], f2, f3)
p3 = Philosopher(names[2], f3, f4)
p4 = Philosopher(names[3], f4, f5)
p5 = Philosopher(names[4], f5, f1)

philosophers = [p1, p2, p3, p4, p5]

#Вывод обедающих философов
def init():
  print('Философы:')
  for p in philosophers:
    print(p.name, end=' ')

#Старт действий
def start():
  for p in philosophers:
    p.start()
  for p in philosophers:
    p.join()

#Обед оканичвается
def exit(signum, frame):
  for p in philosophers:
    p.stop()
  print('\nОбед закончился.\n')

#Точка входа в программу
if __name__ == '__main__':
  signal.signal(signal.SIGINT, exit)
  init() #Инициализация
  start() #Начинаем обед
  print("\nВсе остановили свои действия.")
