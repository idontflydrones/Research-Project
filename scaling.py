import pandas as pd

D4 = pd.read_csv("state_metrics_2025.csv")

def scale_to_0_plus1(x):
    return (x - x.min()) / (x.max() - x.min())

D4["Fs_scaled"] = scale_to_0_plus1(D4["Fs"])
D4["Es_scaled"] = scale_to_0_plus1(D4["Es"])
D4["Gs_scaled"] = scale_to_0_plus1(D4["Gs"])
D4["Ps_scaled"] = scale_to_0_plus1(D4["Ps"])

D4_scaled = D4[
    [
        "State",
        "Code",
        "Fs_scaled",
        "Es_scaled",
        "Gs_scaled",
        "Ps_scaled"
    ]
]

print(D4_scaled.to_string(index=False))