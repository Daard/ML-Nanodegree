from random import randint
class experiment(object):

    @staticmethod
    def run(counts = 100, size = 4, outs = 2):
        """ Run a simulation of the experiment.
               'counts' is the number of repeats, which will give a consistent estimate of probability
               'size' is the number of tries
               'outs' is the number of possible states """
        count = 0.0
        for j in range(counts):
            a = [0 for x in range(size)]
            for i in range(size):
                a[i] = randint(0, outs-1)
            if outs == len(set(a)):
                count += 1
        print("has different:", count/counts)

experiment.run(counts=300, size=20, outs=6)