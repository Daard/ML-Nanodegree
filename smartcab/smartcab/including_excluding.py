from math import factorial as f
from math import pow as p
class experiment(object):

    @staticmethod
    def run(trials = 4, outs = 2):
        sum = 0.0
        for i in range(outs+1):
           iteration = p(-1, i) * p((1.0)*(outs - i)/outs, trials) * f(outs)/f(i)/f(outs - i)
           sum += iteration
        print("probability:", sum)

experiment.run(trials=140, outs=24)