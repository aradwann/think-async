import sys
import threading
from queue import Queue

"""
this is an analogy where we deal with restaurant bots as threads
to test how threads and work 
and experience the race conditions with big number of threads 
"""


class ThreadBot(threading.Thread):
    """thread bot is a subclass of thread"""

    def __init__(self):
        # target function is manage_table
        super().__init__(target=self.manage_table)
        # this bot takes care of cutlery from tables to kitchen and vice versa
        self.cutlery = Cutlery(knives=0, forks=0)
        # tasks are added to the queue and the bot will perform them during its main loop
        self.tasks = Queue()

    def manage_table(self):
        # the primary routine of the bot is infinite loop
        while True:
            task = self.tasks.get()
            if task == 'prepare table':
                kitchen.give(to=self.cutlery, knives=4, forks=4)
            elif task == 'clear table':
                self.cutlery.give(to=kitchen, knives=4, forks=4)
            elif task == 'shutdown':
                return


class Cutlery:
    def __init__(self, knives=0, forks=0):
        self.knives = knives
        self.forks = forks

    def give(self, to: 'Cutlery', knives=0, forks=0):
        """method used to transfer knives and forks from one Cutelry object to another
        typically it will be used by bots to obtain cutlery from the kitchen for new tables
        and vices versa after the table is cleared"""
        self.change(-knives, -forks)
        to.change(knives, forks)

    def change(self, knives, forks):
        """functon to alter the inventory data in the object instance"""
        self.knives += knives
        self.forks += forks

    def __repr__(self):
        return f"Cutlery has {self.knives} knives and {self.forks} forks"


kitchen = Cutlery(knives=100, forks=100)
bots = [ThreadBot() for i in range(10)]


for bot in bots:
    # get number of tables as command line parameter
    for i in range(int(sys.argv[1])):
        bot.tasks.put('prepare table')
        bot.tasks.put('clear table')
    bot.tasks.put('shutdown')

print('Kitchen inventory before service:', kitchen)

for bot in bots:
    bot.start()

for bot in bots:
    bot.join()

print('Kitchen incentory after service:', kitchen)
