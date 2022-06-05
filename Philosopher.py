import threading, time, random

class Philosopher(threading.Thread):

  #Инициализация философа
  def __init__(self, name, left_chopstick, right_chopstick):
    threading.Thread.__init__(self)
    self.stopped = False
    self.name = name
    self.left_chopstick = left_chopstick
    self.right_chopstick = right_chopstick

  #Взятие вилки
  def forkUp(self):
    if not self.stopped:
      self.left_chopstick.acquire()
      self.right_chopstick.acquire()

  #Положил вилку
  def forkDown(self):
    self.left_chopstick.release()
    self.right_chopstick.release()

  #Преостановил дейстие
  def stop(self):
    self.stopped = True

  #Выполняет действие
  def run(self):
    while not self.stopped:
      #Ожидает
      print(f'{self.name} ожидает.')
      self.forkUp()
      if self.stopped: return

      #Ест на протяжение с 3х до 15 секунд
      print(f'{self.name} ест.')
      time.sleep(random.randint(3, 10))
      self.forkDown()

      #Думает на протяжение с 3х до 15 секунд
      print(f'{self.name} размышляет.')
      if not self.stopped: time.sleep(random.randint(3, 15))
