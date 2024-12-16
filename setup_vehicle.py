import vehicle
import setting
import numpy as np

"""
道路を生成し、道路上にに車両を生成する。
"""



class SetupVehicle:
    def __init__(self):
        pass

    def setup_vehicles(self,num_vehicle):
        """
        指定された数の車両を道路にランダムに配置します。
        num_vehicles: 車両の数
        """
        self.vehicles = []
        self.road = np.full(setting.Const().ROAD_LENGTH,-1)

        # #車両を一様分布でランダムな位置に配置
        initial_positions = np.random.choice(setting.Const().ROAD_LENGTH,num_vehicle,replace=False)
        for pos in initial_positions:
            speed = 0
            veh = vehicle.Vehicle(pos,speed,)
            self.road[pos] = speed


if __name__ == "__main__":
    initial = SetupVehicle.setup_vehicles(10)
    print(initial.road)


