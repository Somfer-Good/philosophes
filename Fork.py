import threading

#Класс вилки
class Fork(threading.Semaphore):

  def __init__(self, name):
    threading.Semaphore.__init__(self)
    self.name = name