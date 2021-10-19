import time     

class PrepaidCard(object):
    def __init__(self,initial_credit=1000):
        self.credit = initial_credit
        self.last_update = time.time()  # set current time

    def show_info(self):  
        print('Credit: {0} Last Update: {1}'.
               format(self.credit,
                      time.ctime(self.last_update)))

    def pay(self, price):
        rest = self.credit - price
        if rest < 0:
           print('Fail')
           return
        print('Success')
        self.credit -= price
        self.last_update = time.time()

if __name__ == '__main__':
    work_card = PrepaidCard()
    special_card = PrepaidCard(5000)

    work_card.pay(500)
    work_card.show_info()

    special_card.pay(10000)
