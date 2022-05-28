class Student:
    def __init__(self,name,age,tracks,score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)
        print(f'{name} is a student aged {age}.')
        print(f'He is enrolled in the following tracks :\n{tracks}')
        print(f'His Score is {score}\n')
    #methods
    def change_name(self,new_name):
        self.new_name = str(new_name)
        print(f'The students new name is {self.new_name}')
    def change_age(self,new_age):
        self.new_age = int(new_age)
        print(f'His new age is {self.new_age}')
    def add_track(self,add_track):
        self.add_track = add_track
        print(f'His newly enrolled tracks are: {self.add_track}')
    def get_score(self):
        print(f'His Score remains {self.score}')



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

print(Bob.change_name("Peter"))
print(Bob.change_age(34))
print(Bob.add_track("UI/UX"))
print(Bob.get_score())