import vehicle
import setting


class BoundaryCondition():
    def __init__(self):
        pass

    def check_condition(self,condition:str,vehicle):
        """
        境界条件によって道路外に超えてしまった車両の変数を適切に変更する
        condition:境界条件(periodic,open)
        """
        if condition == "periodic":
            vehicle.position = vehicle.position % setting.Const.ROAD_LENGTH

if __name__ == "__main__":
    vehicles = []
    vehicle1 = vehicle.Vehicle(3,5,104)
    vehicle2 = vehicle.Vehicle(104,5,3)

    print(type(vehicle.Vehicle.position))  # 'int' 型であるべき
    print(type(setting.Const.ROAD_LENGTH))  # 

    BoundaryCondition().check_condition("periodic",vehicle1)
    vehicles.append(vehicle1)
    vehicles.append(vehicle2)

    

print(vehicles)
print(vehicle1.position)
print(vehicle2.position)

