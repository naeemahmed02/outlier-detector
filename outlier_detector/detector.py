import numpy as np
import matplotlib.pyplot as plt

class OutlierDetector:
    def __init__(self, threshold=1.5, method="iqr"):
        """
        Initialize the Outlier Detector.
        Args:
            threshold (float): The multiplier for the IQR or Z-score.
            method (str): The outlier detection method ('iqr' or 'zscore').
        """
        if method not in ["iqr", "zscore"]:
            raise ValueError("Invalid method. Choose 'iqr' or 'zscore'.")
        self.threshold = threshold
        self.method = method

    def detect_outliers(self, data):
        """
        Detect outliers in the dataset.
        Args:
            data (list or numpy array): The dataset.
        Returns:
            dict: Contains sorted data, outliers, refined data, and parameters.
        """
        data = np.array(data)
        if self.method == "iqr":
            return self._iqr_method(data)
        elif self.method == "zscore":
            return self._zscore_method(data)

    def _iqr_method(self, data):
        """Detect outliers using the IQR method."""
        sorted_data = np.sort(data)
        q1, q3 = np.percentile(sorted_data, [25, 75])
        iqr = q3 - q1
        lower_fence = q1 - (self.threshold * iqr)
        upper_fence = q3 + (self.threshold * iqr)
        
        outliers = data[(data < lower_fence) | (data > upper_fence)]
        refined_data = data[(data >= lower_fence) & (data <= upper_fence)]
        
        return {
            "sorted_data": sorted_data,
            "outliers": outliers.tolist(),
            "refined_data": refined_data.tolist(),
            "q1": q1,
            "q3": q3,
            "iqr": iqr,
            "lower_fence": lower_fence,
            "upper_fence": upper_fence
        }

    def _zscore_method(self, data):
        """Detect outliers using the Z-score method."""
        mean = np.mean(data)
        std_dev = np.std(data)
        z_scores = (data - mean) / std_dev
        outliers = data[np.abs(z_scores) > self.threshold]
        refined_data = data[np.abs(z_scores) <= self.threshold]
        
        return {
            "mean": mean,
            "std_dev": std_dev,
            "outliers": outliers.tolist(),
            "refined_data": refined_data.tolist(),
            "z_scores": z_scores.tolist()
        }

    def plot_data(self, data, results):
        """
        Plot the original data and highlight outliers.
        Args:
            data (list or numpy array): The dataset.
            results (dict): The result from detect_outliers().
        """
        plt.figure(figsize=(10, 6))
        plt.plot(data, "bo-", label="Data")
        plt.scatter(
            [i for i, val in enumerate(data) if val in results["outliers"]],
            results["outliers"],
            color="red",
            label="Outliers",
            zorder=5,
        )
        plt.axhline(y=results.get("lower_fence", -np.inf), color="green", linestyle="--", label="Lower Fence")
        plt.axhline(y=results.get("upper_fence", np.inf), color="green", linestyle="--", label="Upper Fence")
        plt.title("Data with Outliers Highlighted")
        plt.xlabel("Index")
        plt.ylabel("Value")
        plt.legend()
        plt.show()
