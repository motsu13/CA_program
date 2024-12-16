"""
Naschモデルを運用
"""
import vehicle
import setting
import boundary
import setup_vehicle

class NaschModel:
    def __init__(self,num_vehicle:int,condition:str):
        """
        Naschモデルの初期化
        num_vehicle : 車両数
        """
        self.num_vehicle = num_vehicle
        self.condition = condition
        
        # 車両を初期生成する
        initial_setup = setup_vehicle.SetupVehicle()
        initial_setup.setup_vehicles(num_vehicle)
        
        self.vehicles = initial_setup.vehicles #Vehicleインスタンスのリスト
        self.road = initial_setup.road #道路

    def update_vehicles(self):
        """
        （Naschモデルのルールに従い）各車両の位置と速度を更新。
        """
        for veh in self.vehicles:
            # 1. 加速（速度が最大速度に達するまで速度を増加）
            veh.accelerate()
            # 2. 前方の車両までの距離に応じた減速
            veh.decelerate()
            # 3. ランダム減速（指定された確率で減速）
            veh.random_decelerate()
            # 4. 新しい位置を計算して車両を移動
            veh.move()
            
        # 更新したvehicleパラメータが道路上かどうかを確認し、道路外の場合は境界条件によって処理
        # その他パラメータを更新する(上ではpositionとspeedしか更新されていない)
        boundary.BoundaryCondition().check_condition(self.condition,self.vehicles)




if __name__ == "__main__":
    model1 = NaschModel(10,"periodic")
    
    for i in range(10):
        print(vars(model1.vehicles[i]))
    
    model1.update_vehicles()
    print()

    for i in range(10):
        print(vars(model1.vehicles[i]))