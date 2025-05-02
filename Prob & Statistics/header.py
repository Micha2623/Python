class Functions:
    def __init__(self):
        self.data = []
        self.x = 0
        self.tittle = ""
        self.frequencies = {}
        
    def d_entry(self):
        print("\nProbability & Statistics numeric calculator \n\n")
        self.tittle = input("What are we going to calculate? ")
        self.x = int(input("How many datas? "))
        for n in range(self.x):
            dates = float(input(f"Insert the data for entry {n + 1}: "))
            self.data.append(dates)
        
    def frec(self):
        self.frequencies = {}
        for number in self.data:
            if number in self.frequencies:
                self.frequencies[number] += 1
            else:
                self.frequencies[number] = 1
        return self.frequencies