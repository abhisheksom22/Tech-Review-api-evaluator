import pandas as pd
import matplotlib.pyplot as plt
import os

CSV_PATH = "results/scores.csv"

def plot_task_comparison(task_name, df):
    task_df = df[df["task"] == task_name]

    # Group by model and calculate average scores
    avg_scores = task_df.groupby("model")[["accuracy", "clarity", "usefulness"]].mean()

    # Plotting
    ax = avg_scores.T.plot(kind="bar", figsize=(8, 5), rot=0)
    ax.set_title(f"Average Scores for {task_name.title()}")
    ax.set_ylabel("Score (1–5)")
    ax.set_ylim(0, 5)
    ax.legend(title="Model")
    plt.tight_layout()
    plt.savefig(f"results/{task_name}_comparison.png")
    print(f"Saved: results/{task_name}_comparison.png")

def main():
    df = pd.read_csv(CSV_PATH)

    for task in ["summarization", "documentation", "bug_detection"]:
        plot_task_comparison(task, df)

if __name__ == "__main__":
    main()
