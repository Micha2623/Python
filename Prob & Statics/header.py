class Functions:
    def __init__(self):
        self.data = [7.0, 12.0, 20.0, 20.0, 20.0, 20.0, 25.0, 25.0, 25.0, 30.0, 32.0, 44.0, 45.0, 45.0, 55.0,88.0, 56.0, 60.0, 65.0, 87.0, 99.0]
        self.x = 0
        self.tittle = ""
        self.frequencies = {}
        
    def d_entry(self):
        print("\nProbability & Statistics numeric calculator \n\n")
        self.tittle = input("What are we going to calculate? ")
        self.x = int(input("How many datas? "))
        for n in range(self.x):
            dates = input(f"Insert the data for entry {n + 1}: ")
            self.data.append(dates)
        
    def frec(self):
        self.frequencies = {}
        for number in self.data:
            if number in self.frequencies:
                self.frequencies[number] += 1
            else:
                self.frequencies[number] = 1
        return self.frequencies