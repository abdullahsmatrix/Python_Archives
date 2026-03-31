# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  loading.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/29 21:51:31 by amamun          #+#    #+#               #
#  Updated: 2026/03/30 23:21:04 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
import sys
import importlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def check_dependencies() -> None:
    print("Checking dependencies:")

    required_packages: list[str] = [
        "pandas",
        "numpy",
        "matplotlib",
        "requests",
    ]
    installed_packages: dict = {}
    missing_packages: list = []

    for pkg in required_packages:
        try:
            module = importlib.import_module(pkg)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {pkg} ({version})")
            installed_packages[pkg] = version

        except ImportError:
            print(f"[MISSING] {pkg}")
            missing_packages.append(pkg)
    return installed_packages, missing_packages


def show_dependency_comparison():
    print("\nDependency Management Comparison:")
    print("- pip: simple installation, manual version")
    print("  control, possible conflicts")
    print("- poetry: dependency resolution, lock files,")
    print("  reproducible environments")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    installed, missing = check_dependencies()
    if missing:
        print("\nSome dependencies are missing.")
        print("Install using pip:")
        print("pip install -r requirements.txt")
        print("\nOr using Poetry:")
        print("poetry install")
        sys.exit()

    show_dependency_comparison()

    print("\nAnalyzing Matrix Data...")
    print("Processing 1000 data points...")
    time = np.arange(1000)
    signal = np.random.normal(loc=0, scale=1, size=1000)
    anomaly = np.abs(signal) > 2

    data = pd.DataFrame({
        "time": time,
        "signal": signal,
        "anomaly": anomaly
    })

    mean_signal = data["signal"].mean()
    num_anomalies = data["anomaly"].sum()

    print(f"Average signal: {mean_signal:.2f}")
    print(f"Detected anomalies: {num_anomalies}")

    print("\nGenerating visualisations...")
    plt.figure()
    plt.plot(data["time"], data["signal"])
    plt.title("Matrix Signal Analysis")
    plt.xlabel("Time")
    plt.ylabel("Signal Strength")
    plt.scatter(
        data["time"][data["anomaly"]],
        data["signal"][data["anomaly"]],
        )
    plt.savefig("matrix_analysis.png")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
