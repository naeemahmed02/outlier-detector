import unittest
from outlier_detector import OutlierDetector

class TestOutlierDetector(unittest.TestCase):
    def test_iqr_method(self):
        detector = OutlierDetector(method="iqr")
        data = [10, 12, 15, 102, 108, 13, 14, 17]
        results = detector.detect_outliers(data)
        self.assertEqual(results["outliers"], [102, 108])
    
    def test_zscore_method(self):
        detector = OutlierDetector(method="zscore", threshold=2)
        data = [10, 12, 15, 102, 108, 13, 14, 17]
        results = detector.detect_outliers(data)
        self.assertIn(102, results["outliers"])
        self.assertIn(108, results["outliers"])

if __name__ == "__main__":
    unittest.main()
