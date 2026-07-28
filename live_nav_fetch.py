import os
import requests
import pandas as pd

# AMFI scheme codes
schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

output_folder = os.path.join("data", "raw")

for scheme_name, scheme_code in schemes.items():

    print("=" * 60)
    print(f"Fetching {scheme_name} ({scheme_code})")

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        print("Scheme:", data["meta"]["scheme_name"])

        nav_df = pd.DataFrame(data["data"])

        file_name = f"{scheme_name}.csv"
        file_path = os.path.join(output_folder, file_name)

        nav_df.to_csv(file_path, index=False)

        print(f"Saved -> {file_name}")

    else:
        print(f"Failed to fetch {scheme_name}")

print("\nAll NAV files downloaded successfully!")