import vehicle
import setting


class BoundaryCondition:
    """
    変数変更後の車両の値が道路上にあるか確認し、なかった場合、適切な値に修正する
    """
    def __init__(self):
        pass

    def check_condition(self,condition:str,vehicles:list):
        """
        境界条件によって道路外に超えてしまった車両の変数を適切に変更する
        condition:境界条件(periodic,open)
        """
        
        if condition == "periodic":
            for vehicle in vehicles:
                vehicle.position = vehicle.position % setting.Const().ROAD_LENGTH
        elif condition == "open":
            #スライスにすることでvehiclesの削除をmainに適応することができる
            vehicles[:] = [vehicle for vehicle in vehicles if vehicle.position < setting.Const().ROAD_LENGTH]
        else:
            print("境界条件の表記ミス")
        

if __name__ == "__main__":
    vehicles = []
    vehicle1 = vehicle.Vehicle(3,5,100)
    vehicle2 = vehicle.Vehicle(100,5,3)

    print(type(vehicle1.position))  # 'int' 型であるべき
    print(type(setting.Const().ROAD_LENGTH))  # 
    vehicles.append(vehicle1)
    vehicles.append(vehicle2)

    print(vehicles)
    print(vehicle1.position)
    print(vehicle2.position)

    BoundaryCondition().check_condition("open",vehicles)    

    print(vehicles)
    print(vehicle1.position)
    print(vehicle2.position)
