# bug_predictor.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Dataset: [Has_Loop, Line_Length, Buggy?]
data = {
    "Has_Loop": [1, 0, 0, 1, 0, 1, 1, 0],  # 1 = has loop/if
    "Line_Length": [20, 5, 25, 30, 8, 40, 15, 10],  # Length of line
    "Buggy": [1, 0, 1, 1, 0, 1, 0, 0]  # 1 = buggy
}
df = pd.DataFrame(data)

# Train AI model
X = df[["Has_Loop", "Line_Length"]]
y = df["Buggy"]
model = RandomForestClassifier().fit(X, y)

def predict_bug(code_line):
    """Predicts if a line of code is bug-prone."""
    has_loop = 1 if ("for " in code_line or "if " in code_line) else 0
    line_len = len(code_line)
    prob = model.predict_proba([[has_loop, line_len]])[0][1]
    return round(prob * 100, 2)  # Returns % chance of bug

# Demo
test_code = [
    "for i in range(100):",  # Complex loop → high bug risk
    "x = 5"  # Simple → low risk
]
for line in test_code:
    print(f"Line: {line} | Bug Risk: {predict_bug(line)}%")
