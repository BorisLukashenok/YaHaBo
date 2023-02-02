class RedButton:
    def __init__(self):
        self.coun = 0

    def count(self):
        return self.coun
    
    def click(self):
        print("Тревога!")
        self.coun += 1