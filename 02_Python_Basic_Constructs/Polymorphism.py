class Worker:
    def work(self):
        print("Working")

    def perform_task(self):
        print("Perfoming Task ",end="")
        self.work()

class DelivaryMan(Worker):
    def work(self):
        print("Delivaring Goods")    

class LumberJack(Worker):
    def work(self):
        print("Delivaring Man is Ramesh")


deliveryMan = DelivaryMan()
lumberJack = LumberJack()

deliveryMan.perform_task()
lumberJack.perform_task()




