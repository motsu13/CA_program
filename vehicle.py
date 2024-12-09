import numpy as np

#定数ファイル
import setting

"""
車両の動きクラス
変数:
車両の位置
車両の速度
先行車両との車間距離
先行車両の位置
"""

class Vehicle:
    def __init__(self, position:int, speed:int):
        """
        車両の初期位置と初期速度を設定。
        position: 車両の初期位置（整数）
        speed: 車両の初期速度（0から最大速度までの整数）
        """
        self.position = position  # 現在の車両位置を保存
        self.speed = speed  # 現在の車両速度を保存


    def move(self, new_position):
        """
        車両の位置を更新。
        new_position: 車両が移動する新しい位置
        """
        self.position = new_position

    def accelerate(self):
        """
        車両を加速させます。現在の速度が最大速度より小さい場合、速度を1増やす。
        """
        if self.speed < setting.Const().MAX_SPEED: #車両の最大速度
            self.speed += 1

    def deceleration(self,road,max_speed,boundary_condition):
        """
        前の車両までの距離と自分の速度を比較し、距離が小さければ速度を減速。
        """
        length_vehicle = 1#車両の全長
        distance_next_vehicle = 1 # 次の車両までの車間距離

        #前方車両との車間距離を判断
        if boundary_condition == 'open':
            while (self.position + distance_next_vehicle) < len(road) and road[(self.position + distance_next_vehicle)] == -1:
                distance_next_vehicle += 1
                if distance_next_vehicle > max_speed:
                    break
            if (self.position + distance_next_vehicle) >= len(road):
                #右端に着いたら車両を遠くに飛ばす
                self.speed = len(road)#右辺は最大
            
            elif distance_next_vehicle <= self.speed:
                #前の車両までの距離が最大速度以下の場合、その距離に減速する
                self.speed = max(distance_next_vehicle - length_vehicle,0)

    def random_decelerate(self, probability):
        """
        指定された確率で車両をランダムに減速。
        probability: 車両が減速する確率（0から1の範囲）
        """
        if np.random.rand() < probability:
            self.speed = max(0, self.speed - 1)  # 減速しても速度が負にならないようにする



if __name__ == "__main__":
    vehicle1 = Vehicle(1,1)

    vehicle1.accelerate()
    print(vehicle1.speed)
