"""
Simple Analytics
"""
import json


class MaxTemperatureDetector(object):
    """
        Main class for the Analytics
    """
    def __init__(self):
        print "Create maxTemperatureDetector"

    def detector(self, inputJson):
        """
            Detection function
        """
        inputJson = json.loads(inputJson)
        print(inputJson)

        temperature = max(inputJson['data']['time_series']['temperature'])
        timestamp = inputJson['data']['time_series']['time_stamp']
        latest = max(timestamp[0], timestamp[-1])

        outputJson = json.dumps({"data": {"time_series":{"growth": [temperature*3], "time_stamp": [latest]}}})
        print (outputJson)
        return outputJson
