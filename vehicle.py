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
    def __init__(self, position:int, speed:int):
        """
        車両の初期位置と初期速度を設定。
        position: 車両の初期位置（整数）
        speed: 車両の初期速度（0から最大速度までの整数）
        preciding_position: 先行車両の位置
        gap: 先行車両との車間距離(車両の前端と先行車両の後ろ端の間の距離)
        """
        self.position = position  # 現在の車両位置を保存
        self.speed = speed  # 現在の車両速度を保存
        #以下1stepごとに更新が必要
        self.preciding_position #= preciding_position
        self.gap #= (preciding_position - position) - setting.Const().VEHICLE.LENGTH


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

    def decelerate(self):
        """
        前の車両までの距離と自分の速度を比較し、距離が小さければ速度を減速。
        gap:
        """
        #前方車両との車間距離を判断
        if self.gap < self.speed:
            self.speed = self.gap

    def random_decelerate(self):
        """
        指定された確率で車両をランダムに減速。
        """
        if np.random.rand() < setting.Const().DECELERATION_PROBABILITY: #減速するかしないか
            self.speed = max(0, self.speed - )  # 減速しても速度が負にならないようにする



if __name__ == "__main__":
    vehicle1 = Vehicle(1,1)

    vehicle1.accelerate()
    print(vehicle1.speed)
