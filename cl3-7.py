import numpy as np
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score

# Simulate structure damage dataset (1 = damaged, 0 = normal)
X, y = make_classification(n_samples=100, n_features=5, n_classes=2, random_state=42)

# Initialize population of random classifiers (weights)
pop = [np.random.randn(5) for _ in range(20)]

def classify(x, w):
    return int(np.dot(x, w) > 0)

def fitness(w):
    preds = [classify(x, w) for x in X]
    return accuracy_score(y, preds)

for _ in range(50):  # 50 generations
    scores = [fitness(w) for w in pop]
    #top = [w for _, w in sorted(zip(scores, pop), reverse=True)[:10]]
    top = [w for _, w in sorted(zip(scores, pop), key=lambda x: x[0], reverse=True)[:10]]
    clones = [w + np.random.normal(0, 0.1, 5) for w in top for _ in range(2)]
    pop = clones

best = max(pop, key=fitness)
print("Best Accuracy:", fitness(best))
