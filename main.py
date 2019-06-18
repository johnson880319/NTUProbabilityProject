from game_define import Game, N
import agent_define as ad
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-w', '--workers', dest='worker_num', type=int, default=0)
args = parser.parse_args()
worker_num = args.worker_num

g = Game(setting='basic-1', agent=ad.Agent(N), workers=worker_num)
print('Basic-1 Score:', g.evaluate())

g = Game(setting='basic-2', agent=ad.Basic_2_Agent(N, 2), k=2, workers=worker_num)
print('Basic-2 Score for k = 2:', g.evaluate())

g = Game(setting='basic-2', agent=ad.Basic_2_Agent(N, 5), k=5, workers=worker_num)
print('Basic-2 Score for k = 5:', g.evaluate())

g = Game(setting='basic-2', agent=ad.Basic_2_Agent(N, 20), k=20, workers=worker_num)
print('Basic-2 Score for k = 20:', g.evaluate())

g = Game(setting='basic-3', agent=ad.Basic_3_Agent(N, 2), k=2, workers=worker_num)
print('Basic-3 Score for k = 2:', g.evaluate())

g = Game(setting='basic-3', agent=ad.Basic_3_Agent(N, 5), k=5, workers=worker_num)
print('Basic-3 Score for k = 5:', g.evaluate())

g = Game(setting='basic-3', agent=ad.Basic_3_Agent(N, 20), k=20, workers=worker_num)
print('Basic-3 Score for k = 20:', g.evaluate())

g = Game(setting='advanced-1-Uniform', agent=ad.Advanced_1u_Agent(N), workers=worker_num)
print('Advanced-1-Uniform Score:', g.evaluate())

g = Game(setting='advanced-1-Normal', agent=ad.Advanced_1n_Agent(N), workers=worker_num)
print('Advanced-1-Normal Score:', g.evaluate())

g = Game(setting='advanced-2', agent=ad.Advanced_2_Agent(N, 100), k=100, workers=worker_num)
print('Advanced-2 Score:', g.evaluate())