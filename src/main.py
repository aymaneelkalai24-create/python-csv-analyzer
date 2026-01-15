import csv
def analyze_csv(file_path):
    scores = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["score"] is not None and row["score"] != "":
                scores.append(float(row["score"]))

    print("Nombre d'étudiants :", len(scores))
    print("Moyenne :", sum(scores) / len(scores))
    print("Score maximum :", max(scores))
    print("Score minimum :", min(scores))
if __name__ == "__main__":
    analyze_csv("../data/data.csv")

