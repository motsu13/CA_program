import vehicle
import setting
import numpy as np
"""
道路を生成し、道路上にに車両を生成する。道路は一次元のリストとして示される。
道路上では車両は速度の値として示され、-1は車両が存在しないものとして示す
"""

class SetupVehicle:
    def __init__(self):
        pass

    def setup_vehicles(self,num_vehicle):
        """
        指定された数の車両を道路にランダムに配置します。
        num_vehicles: 車両数
        """
        self.vehicles = []# 車両リスト
        self.road = np.full(setting.Const().ROAD_LENGTH,-1) #道路

        # 車両の位置を一様分布で選択して配置し順番に並べる
        initial_positions = np.sort(np.random.choice(setting.Const().ROAD_LENGTH,num_vehicle,replace=False))
        
        # 得られた位置を元に車両を道路上に配置
        for i in range(len(initial_positions)):
            speed = 0
            veh = vehicle.Vehicle(initial_positions[i],
                                  speed,initial_positions[(i+1)%len(initial_positions)])
            self.vehicles.append(veh)
            self.road[initial_positions[i]] = speed


if __name__ == "__main__":
    initial = SetupVehicle()
    initial.setup_vehicles(10)
    print(initial.road)
    for i in range(10):
        print(initial.vehicles[i].position)

