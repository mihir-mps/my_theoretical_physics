import pandas as pd
import numpy as np
import networkx as nx

neurons = pd.read_csv("Fruit_Fly_Quantum_Connectome.csv.csv", dtype=str)
connections = pd.read_csv("Fruit_Fly_Quantum_Connections.csv.csv", dtype=str)

G = nx.DiGraph()
G.add_nodes_from(neurons.iloc[:, 0].astype(str))

for _, r in connections.iterrows():
    G.add_edge(str(r["From"]), str(r["To"]), weight=float(r["Synapses"]))

ids = list(G.nodes)
W = nx.to_numpy_array(G, nodelist=ids, weight="weight")

if W.max() > 0:
    W /= W.max()

knowledge = {
    "Superposition": {
        "keywords": ["superposition", "state", "states", "multiple", "possibilities"],
        "answer": "A quantum system can exist in a combination of possible states."
    },
    "Heisenberg Uncertainty": {
        "keywords": ["heisenberg", "uncertainty", "position", "momentum", "precision"],
        "answer": "The Heisenberg uncertainty principle says that position and momentum cannot both be known with unlimited precision."
    },
    "Schrodinger's Cat": {
        "keywords": ["schrodinger", "cat", "measurement", "thought", "experiment"],
        "answer": "Schrödinger's cat is a thought experiment used to illustrate quantum superposition and the role of measurement."
    }
}

def activate(text):
    v = np.zeros(len(ids))
    words = text.lower().split()

    for i, word in enumerate(words):
        v[i % len(ids)] += 1

    return np.tanh(W @ v)

def ask(question):
    q = question.lower()
    scores = {}

    for concept, data in knowledge.items():
        scores[concept] = sum(word in q for word in data["keywords"])

    concept = max(scores, key=scores.get)

    if scores[concept] == 0:
        return "I don't recognize that quantum concept yet."

    activate(question)
    activate(knowledge[concept]["answer"])

    return f"[{concept}] {knowledge[concept]['answer']}"

print("Quantum Learning Fruitfly ready!")

while True:
    q = input("You: ")

    if q.lower() == "exit":
        break

    print("Fly:", ask(q))