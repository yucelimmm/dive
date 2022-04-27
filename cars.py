class Cars:
    def __init__(self, make, model, trim, year, color, ):
        self.make = make
        self.model = model
        self.trim = trim
        self.year = year
        self.color = color
    def drive(self):
        print( self.make + " is diviving at the moment")

    def stop(self):
        print(self.make +" is not in any action")
    