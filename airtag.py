import csv
import airtag

class AirTag:
    def __init__(self,
                 dateTime,
                 name,
                 batteryStatus,
                 locationPostionType,
                 locationLatitude,
                 locationLongitude,
                 addressStreetAddress,
                 addressStreetName,
                 addressAreaOfInterestA,
                 addressAreaOfInterestB):
        self.dateTime = dateTime
        self.name = name
        self.batteryStatus = batteryStatus
        self.locationPostionType = locationPostionType
        self.locationLatitude = locationLatitude
        self.locationLongitude = locationLongitude
        self.addressStreetAddress = addressStreetAddress
        self.addressStreetName = addressStreetName
        self.addressAreaOfInterestA = addressAreaOfInterestA
        self.addressAreaOfInterestB = addressAreaOfInterestB
    
    def to_json(self):
        return{
            "datetime":self.dateTime,
            "name":self.name,
            "lat" :self.locationLatitude,
            "lng" :self.locationLongitude,
            "streetAddress" : self.addressStreetAddress,
            "streetName" : self.addressStreetName
            }
    def getLat(self):
        return self.locationLatitude
    def getLng(self):
        return self.locationLongitude
