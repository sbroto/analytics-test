
from analytic import MaxTemperatureDetector

if __name__ == "__main__":
    dm = MaxTemperatureDetector()
    assert dm.detector(34,45) == 79