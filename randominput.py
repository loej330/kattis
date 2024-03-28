import random
trials = 5 

print(trials)
for i in range(trials):
    print(random.random() * 20)
    print(random.random() * 40)
    print(random.uniform(0, 50))
    print(random.uniform(0, 20))