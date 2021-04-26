from student import Student


class DataStudent(Student):
    # DataStudent inherits from the Student class
    cursus = "Data Science"

    def __init__(self, name, age, batch):
        super().__init__(name, age)
        self.batch = batch
