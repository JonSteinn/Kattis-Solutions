#include <stdio.h>
#include <queue>

struct City {
    int population;
    int ballots;
    double ratio;

    City() {}
    
    City(int population) {
        this->population = population;
        this->ballots = 1;
        this->ratio = (double)population;
    }

    void increase_ballots() {
        this->ballots += 1;
        this->ratio = this->population / (double)this->ballots;
    }

    int int_raito() {
        if (this->population % this->ballots == 0) {
            return this->population / this->ballots;
        } else {
            return 1+(int)(this->population / (double)this->ballots);
        }
    }
};

struct CityComparator { 
    bool operator()(City const& p1, City const& p2) {
        return p1.ratio < p2.ratio;
    } 
}; 

int max_people(int remaining, std::priority_queue<City,std::vector<City>,CityComparator>& cities) {
    City c;
    while (remaining--) {
        c = cities.top();
        cities.pop();
        c.increase_ballots();
        cities.push(c);
    }
    c = cities.top();
    return c.int_raito();
}

void test_case(int n, int b) {
    int p;
    std::priority_queue<City,std::vector<City>,CityComparator> cities;
    for (int i = 0; i < n; i++) {
        scanf("%d", &p);
        cities.push(City(p));
    }
    printf("%d\n", max_people(b-n, cities));
}

int main() {
    int n,b;
    while(1) {
        scanf("%d %d", &n, &b);
        if (n<0) break;
        test_case(n,b);
    }
    return 0;
}