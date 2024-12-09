"""
定数をまとめる
"""
class Const(object):
    _ACCELERATION = 1
    _DECELERATION = 1
    _DECELERATION_PROBABILITY = 0.5
    _MAX_SPEED = 5
    _VEHICLE_LENGTH = 1

    _ROAD_LENGTH = 100

    @property
    def ACCELERATION(self):
        return self._ACCELERATION
    
    @property
    def DECELERATION(self):
        return self._DECELERATION
    
    @property
    def DECELERATION_PROBABILITY(self):
        return self._DECELERATION_PROBABILITY
    
    @property
    def MAX_SPEED(self):
        return self._MAX_SPEED
    
    @property
    def VEHICLE_LENGTH(self):
        return self._VEHICLE_LENGTH
    
    @property
    def ROAD_LENGTH(self):
        return self._ROAD_LENGTH

if __name__ == "__main__":
    print(Const().DECELERATION)
    