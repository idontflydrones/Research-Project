
import pandas as pd

files = [
    "state_metrics_2025.csv",
    "state_metrics_2024.csv",
    "state_metrics_2023.csv",
    "state_metrics_2022.csv",
    "state_metrics_2021.csv",
    "state_metrics_2020.csv",
    "state_metrics_2019.csv",
    "state_metrics_2018.csv",
    "state_metrics_2017.csv",
    "state_metrics_2016.csv",
    "state_metrics_2015.csv",
    "state_metrics_2014.csv"
]

def scale_to_0_plus1(x):
    return (x - x.min()) / (x.max() - x.min())

for filename in files:
    D4 = pd.read_csv(filename)

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

    new_filename = "scaled_" + filename
    D4_scaled.to_csv(new_filename, index=False)

    print("Saved", new_filename)
    #comment
