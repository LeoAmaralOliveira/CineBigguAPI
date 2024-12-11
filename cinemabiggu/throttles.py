from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class ViewerThrottle(AnonRateThrottle):
    rate = '30/min'

class EditorThrottle(AnonRateThrottle):
    rate = '60/min'
