import math
'''
class TravelMethod definition
'''
class TravelMethod(object):
    def __init__(self,tmtype,tmcode,tmduration,tmschedule,tmdestination,tmorigin):
        self.tmtype=tmtype
        self.tmcode=tmcode
        self.tmduration=tmduration
        self.tmschedule=tmschedule
        self.tmdestination=tmdestination
        self.tmorigin=tmorigin