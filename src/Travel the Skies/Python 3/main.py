class Airport:
    TOTAL = 0
    DAYS = 0
    FLIGHTS = 0
    AIRPORTS = []
    PEOPLE_WAITING = []

    @staticmethod
    def is_optimal():
        for day in range(Airport.DAYS):
            for airport in Airport.AIRPORTS:
                ppl = Airport.PEOPLE_WAITING[day][airport.index]
                for v,c in airport.days[day]:
                    if c > ppl:
                        return False
                    ppl -= c
                    Airport.PEOPLE_WAITING[day+1][v] += c
                Airport.PEOPLE_WAITING[day+1][airport.index] += ppl 
        return True

    @staticmethod
    def read_data():
        Airport._read_total()
        Airport._read_flights()
        Airport._read_people()
    
    @staticmethod
    def _read_total():
        Airport.TOTAL, Airport.DAYS, Airport.FLIGHTS = map(int,input().split())

    @staticmethod
    def _read_flights():
        for i in range(Airport.TOTAL):
            Airport.AIRPORTS.append(Airport(i, Airport.DAYS))
        for _ in range(Airport.FLIGHTS):
            u,v,d,c = map(int,input().split())
            Airport.AIRPORTS[u-1].flight_to(d-1, v-1, c)

    @staticmethod
    def _read_people():
        for _ in range(Airport.DAYS + 1): # +1 to dump remaining after days on last day
            Airport.PEOPLE_WAITING.append([0] * Airport.TOTAL)
        for _ in range(Airport.TOTAL * Airport.DAYS):
            a,b,c = map(int,input().split())
            Airport.PEOPLE_WAITING[b-1][a-1] += c

    def __init__(self, v, k):
        self.index = v
        self.days = [[] for _ in range(k)]

    def flight_to(self, d, v, c):
        self.days[d].append((v,c))

def main():
    Airport.read_data()
    print('optimal' if Airport.is_optimal() else 'suboptimal')

if __name__ == "__main__":
    main()