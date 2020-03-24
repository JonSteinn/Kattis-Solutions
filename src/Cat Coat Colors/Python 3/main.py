from collections import defaultdict

class Cat:
    B_pairs = ['BB','Bb','bb']
    R_pairs = {'F': ['OO','Oo','oo'], 'M': ['O','o']}
    D_pairs = ['DD','Dd','dd']

    color_to_genes = {
        'Black': {
            'M': frozenset({'B','D','o'}),
            'F': frozenset({'B','D','oo'})
        },
        'Blue': {
            'M': frozenset({'B', 'dd','o'}),
            'F': frozenset({'B', 'dd','oo'})
        },
        'Chocolate': {
            'M': frozenset({'bb','D','o'}),
            'F': frozenset({'bb','D','oo'})
        },
        'Lilac': {
            'M': frozenset({'bb','dd','o'}),
            'F': frozenset({'bb','dd','oo'})
        },
        'Red': {
            'M': frozenset({'D','O'}),
            'F': frozenset({'D','OO'})
        },
        'Cream': {
            'M': frozenset({'dd','O'}),
            'F': frozenset({'dd','OO'})
        },
        'Black-Red Tortie': {
            'F': frozenset({'B','D','Oo'})
        },
        'Chocolate-Red Tortie': {
            'F': frozenset({'bb','D','Oo'})
        },
        'Blue-Cream Tortie': {
            'F': frozenset({'B','dd','Oo'})
        },
        'Lilac-Cream Tortie': {
            'F': frozenset({'bb','dd','Oo'})
        }
    }

    genes_to_color = {}
    
    @staticmethod
    def generate_all_possible(genes,gender):
        R,B,D = [],[],[]
        for g in genes:
            if 'b' in g.lower():
                B.extend((b for b in Cat.B_pairs if g in b))
            elif 'o' in g.lower():
                R.extend((r for r in Cat.R_pairs[gender] if g in r))
            else:
                D.extend((d for d in Cat.D_pairs if g in d))
        if not B:
            B.extend(Cat.B_pairs)
        return R,B,D

    @staticmethod
    def all_possible(genes,gender):
        R,B,D = Cat.generate_all_possible(genes,gender)
        return (frozenset({r,b,d}) for r in R for b in B for d in D)

    @staticmethod
    def fill_gene_map():
        Cat.genes_to_color['M'] = {}
        Cat.genes_to_color['F'] = {}
        for color,v in Cat.color_to_genes.items():
            for gender,genes in v.items():
                for gene in Cat.all_possible(genes,gender):
                    Cat.genes_to_color[gender][gene] = color
            
    @staticmethod
    def find_color_male(r1,b1,b2,d1,d2):
        b1,b2 = sorted([b1,b2])
        d1,d2 = sorted([d1,d2])
        return Cat.genes_to_color['M'][frozenset({b1+b2,d1+d2,r1})]

    @staticmethod
    def find_color_female(r1,r2,b1,b2,d1,d2):
        b1,b2 = sorted([b1,b2])
        d1,d2 = sorted([d1,d2])
        r1,r2 = sorted([r1,r2])
        return Cat.genes_to_color['F'][frozenset({b1+b2,d1+d2,r1+r2})]


    def __init__(self, color, gender):
        if not Cat.genes_to_color:
            Cat.fill_gene_map()

        genes = Cat.color_to_genes[color][gender]
        self.R, self.B, self.D = Cat.generate_all_possible(genes, gender)

    def offspring_likelihood(self, other):
        total, color_counter = 0, defaultdict(lambda: 0)
        for r1 in self.R:
            for r2 in r1:
                for b1 in self.B:
                    for b2 in b1:
                        for d1 in self.D:
                            for d2 in d1:
                                for r3 in other.R:
                                    for r4 in r3:
                                        for b3 in other.B:
                                            for b4 in b3:
                                                for d3 in other.D:
                                                    for d4 in d3:
                                                        total += 2
                                                        # Assuming self is female here...
                                                        color_counter[Cat.find_color_male(r2,b2,b4,d2,d4)] += 1
                                                        color_counter[Cat.find_color_female(r2,r4,b2,b4,d2,d4)] += 1
        # https://www.imdb.com/title/tt0105121/
        for k in color_counter.keys():
            color_counter[k] /= total
        return sorted(color_counter.items(), key=lambda z: (-z[1],z[0]))


def main():
    mom = Cat(input(),'F')
    dad = Cat(input(),'M')
    lis = mom.offspring_likelihood(dad)
    print('\n'.join(('%s %.9f' % (a,b) for a,b in lis)))

if __name__ == "__main__":
    main()