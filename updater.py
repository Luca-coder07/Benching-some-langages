# generate_score_graph.py
import matplotlib.pyplot as plt

def create_graph(score):
    fig, ax = plt.subplots()
    ax.pie([score, 100-score], labels=[f"{score}%", ""], colors=["#4CAF50", "#dddddd"], startangle=90)
    ax.axis("equal")
    plt.savefig("images/score.png")

create_graph(84)

