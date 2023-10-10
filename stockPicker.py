
class Stock:
    def __init__(self, name, price, m1, m6, y1, y5, ratio) -> None:
        self.name = name
        self.price = price
        self.m1 = m1
        self.m6 = m6
        self.y1 = y1
        self.y5 = y5
        self.ratio = ratio
        
    def __str__(self):
        return f"{self.name}, {self.price}, {self.m1}, {self.m6}, {self.y1}, {self.y5}, {self.ratio},|"
    
    def __repr__(self):
        return str(self)
        
def read_csv(filename:str):
    ret = []
    with open(filename) as f:
        for sequences in f:
            ret.append(sequences.strip().split(","))
    return ret[1:]

def create_stocks(csv, projection):
    ratio = 0
    stocks = []
    for line in csv:
        if projection == "1M":
            ratio = float(line[2]) / float(line[1])
        elif projection == "6M":
            ratio = float(line[3]) / float(line[1])
        elif projection == "1Y":
            ratio = float(line[4]) / float(line[1])
        elif projection == "5Y":
            ratio = float(line[5]) / float(line[1])
            
        stock = Stock(line[0], line[1], line[2], line[3], line[4], line[5], ratio)
        stocks.append(stock)
        
    return stocks

def create_heap(stocks):
    import heapq as pq
    heap = []
    for stock in stocks:
        pq.heappush(heap,(-stock.ratio, stock))
    return heap

def generate_results(budget, heap):
    import heapq as pq
    result = []
    while budget > 0:
        curr,object = pq.heappop(heap)
        if budget >= float(object.price):
            result.append(f"{object.name}")
            budget -= float(object.price)
        else:
            fraction = round(budget / float(object.price),2)
            budget -= float(object.price) * fraction
            result.append(f"{fraction} {object.name}")
            
    return result
    
    

if __name__ == "__main__":
    from sys import argv
    if len(argv) > 1:
        sequences = read_csv(argv[1])
        stocks = create_stocks(sequences, argv[3])
        heap = create_heap(stocks)
        results = generate_results(float(argv[2]), heap)
        print(results)