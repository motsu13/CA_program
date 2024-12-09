import numpy as np

#定数ファイル
import setting

"""
車両の動きクラス
変数:
車両の位置
車両の速度
先行車両との車間距離:gap
先行車両の位置
"""


class Vehicle:
    def __init__(self, position:int, speed:int, preciding_position:int):
        """
        車両の初期位置と初期速度を設定。
        position: 車両の初期位置（整数）
        speed: 車両の初期速度（0から最大速度までの整数）
        preciding_position: 先行車両の位置
        gap: 先行車両との車間距離(車両の前端と先行車両の後ろ端の間の距離)
        """
        self.position = position  # 現在の車両位置を保存
        self.speed = speed  # 現在の車両速度を保存

        self.preciding_position = preciding_position #先行車両の位置
        self.gap = (preciding_position - position) - setting.Const().VEHICLE_LENGTH


    def move(self):
        """
        車両の位置を更新。
        """
        self.position = self.position + self.speed

    def accelerate(self):
        """
        車両を加速させます。現在の速度が最大速度より小さい場合、速度を1増やす。
        """
        if self.speed < setting.Const().MAX_SPEED: #車両の最大速度
            self.speed += 1

    def decelerate(self):
        """
        前の車両までの距離と自分の速度を比較し、距離が小さければ速度を減速。
        """
        #前方車両との車間距離を判断
        if self.gap < self.speed:
            self.speed = self.gap

    def random_decelerate(self):
        """
        指定された確率で車両をランダムに減速。
        """
        if np.random.rand() < setting.Const().DECELERATION_PROBABILITY: #減速するかしないか
            self.speed = max(0, self.speed - setting.Const().DECELERATION)  # 減速しても速度が負にならないようにする

    def update_vehicle_parameter(self,preciding_position):
        """
        更新された位置を元に前方車両の位置を正しく取得
        preceding_position: 先行車両の位置
        """
        self.preciding_position = preciding_position #先行車両の位置
        self.gap = (preciding_position - self.position) - setting.Const().VEHICLE.LENGTH
        


if __name__ == "__main__":
    vehicle1 = Vehicle(1,1,3)
    print(vehicle1.speed)
    vehicle1.accelerate()
    print(vehicle1.speed)
    vehicle1.decelerate()
    print(vehicle1.speed)
    vehicle1.random_decelerate()
    print(vehicle1.speed)
    print(vehicle1.position)
    vehicle1.move()
    print(vehicle1.position)
