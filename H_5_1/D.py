class Programmer:

    def __init__(self, name, post):
        self.name = name
        self.post = post
        self.working_out = 0
        self.salary_scale = {'Junior': 10, 'Middle': 15, 'Senior': 20}
        self.bablo = 0

    def work(self, time):
        self.working_out += time
        self.bablo += time * self.salary_scale[self.post]

    def rise(self):
        if self.post == 'Junior':
            self.post = 'Middle'
        elif self.post == 'Middle':
            self.post = 'Senior'
        else:
            self.salary_scale['Senior'] += 1

    def info(self):
        return f'{self.name} {self.working_out}ч. {self.bablo}тгр.'