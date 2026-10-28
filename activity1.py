import numpy as np

india = np.array([287,312,198,345,267,389,223,301,278,334])
aus = np.array([265,334,201,298,289,367,245,278,301,312])

print("="*45)
print(" INDIA vs AUSTRALIA - ODI SERIES")
print("="*45)

print("Watch India Australia Winner")
for i in range(10):
    winner = "India" if india[i] > aus[i] else "Australia"
    print(i+1, india[i], aus[i], winner)

for name, scores in [("INDIA", india), ("AUSTRALIA", aus)]:
    print(f"{name} STATS")
    print("Average: ", np.mean(scores))
    print("Highest: ", np.max(scores))
    print("Lowest: ", np.min(scores))
    print("Total: ", np.sum(scores))
    print("Std Deviation: ", round(np.std(scores), 1))
    top = np.argsort(scores)[-3:][::-1]
    print("Top 3 Scores: ", scores[top])
    print("Matches: ", top + 1)