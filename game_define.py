import numpy as np
import agent_define
import concurrent.futures
import time
from copy import deepcopy

SIMUL_TIMES = 50000
PRINT_PER_SIMUL_TIMES = 1000
N = 1000


class Game(object):

    def __init__(self, setting, agent, k=0, workers=0):
        self.setting = setting
        self.agent = agent
        self.k = k
        if workers:
            self.workers = workers
        else:
            self.workers = None
        assert setting in ['basic-1', 'basic-2', 'basic-3', \
                           'advanced-1-Uniform', 'advanced-1-Normal', 'advanced-2']
        assert (setting in ['basic-2', 'basic-3', 'advanced-2']) == (k != 0)

    def get_values(self):
        if self.setting in ['basic-1', 'basic-2', 'basic-3']:
            # try to make unknown distribution
            values = []
            for i in range(87):
                values.append(np.random.chisquare(np.random.randint(3, 387), size=(np.random.randint(12, 148),)))
            values = np.concatenate(values, axis=None)[:N]
            np.random.shuffle(values)
        elif self.setting == 'advanced-1-Normal':
            mean = np.random.uniform(-10000, 10000)
            std = np.random.uniform(0, 10000)
            values = np.random.normal(loc=mean, scale=std, size=(N,))
        elif self.setting == 'advanced-1-Uniform':
            upper = np.random.uniform(0, 10000)
            lower = np.random.uniform(-10000, 0)
            values = np.random.uniform(low=lower, high=upper, size=(N,))
        elif self.setting == 'advanced-2':
            values = np.random.uniform(low=0, high=1, size=(N,))
            shift = np.arange(1, N + 1) / N / self.k
            values += shift
        return values

    def process_one_simulation(self, agent):

        agent = deepcopy(agent)
        agent.restart()
        chance = self.k if self.setting == 'basic-3' else 1
        choice = set()

        values = self.get_values()
        for value_idx, value in enumerate(values):
            if chance:
                if agent.decide(value):
                    choice.add(value_idx)
                    chance -= 1
            else:
                break

        return self.evaluate_one_simulation(values, choice)

    def evaluate_one_simulation(self, values, choice):

        if self.setting == 'basic-2':
            ans = set(np.argsort(values)[-self.k:])
        else:
            ans = set([np.argmax(values)])

        # print(values, choices, ans)

        is_hit = int(bool(ans & choice))
        return is_hit

    def evaluate(self):

        agents = [self.agent] * SIMUL_TIMES
        score = 0
        with concurrent.futures.ProcessPoolExecutor(max_workers=self.workers) as executor:
            for simul_id, is_hit in enumerate(executor.map(self.process_one_simulation, agents), 1):
                score += is_hit
                # if simul_id % PRINT_PER_SIMUL_TIMES == 0:
                #     print('Has simulated %d of %d times...' % (simul_id, SIMUL_TIMES))


        return score / SIMUL_TIMES