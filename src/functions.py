import matplotlib.pyplot as plt
from collections import Counter

def grades_graph():

        grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]

        histogram = Counter(min(grade // 10*10, 90) for grade in grades)

        plt.axis([-5, 105, 0, 5])
        plt.xticks([10* i for i in range(11)])
        plt.xlabel("Decile")
        plt.ylabel("# of Students")
        plt.title("Distribution of Exam 1 Grades")

        plt.bar([x + 5 for x in histogram.keys()],
                histogram.values(),
                10,
                edgecolor = (0,0,0,))

        plt.show()

def y_malandro():
        mentions = [500, 505]
        years = [2017, 2018]

        plt.bar(years, mentions, 0.8)
        plt.xticks(years)
        plt.ylabel("# of times I heard someone say 'data science'")

        # se não fizer isso, matplotlib rotulará o eixo x como 0, 1
        # e adicionará um +2.013e3 off no canto 
        plt.ticklabel_format(useOffset=False)

        # o eixo y malandro mostrando apenas a parte acima de 500
        plt.axis([2016.5, 2018.5, 499, 505])
        plt.title("Look at the 'HUGE' Increase!")
        plt.show()

def y_sincero():
        mentions = [500, 505]
        years = [2017, 2018]

        plt.bar(years, mentions, 0.8)
        plt.xticks(years)
        plt.ylabel("# of times I heard someone say 'data science'")

        # se não fizer isso, matplotlib rotulará o eixo x como 0, 1
        # e adicionará um +2.013e3 off no canto 
        plt.ticklabel_format(useOffset=False)

        # o eixo y malandro mostrando apenas a parte acima de 500
        plt.axis([2016.5, 2018.5, 0, 505])
        plt.title("Look at the not so 'HUGE' Increase!")
        plt.show()