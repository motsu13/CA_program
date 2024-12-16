import vehicle
import setting

class BoundaryCondition:
    """
    変数変更後の車両の値が道路上にあるか確認し、なかった場合、適切な値に修正する
    また、先行車の位置やその車間距離も境界条件に応じて適切に修正する
    """
    def __init__(self):
        pass

    def check_condition(self,condition:str,vehicles:list):
        """
        境界条件によって道路外に超えてしまった車両の変数を適切に変更する
        (車両のパラメータ更新も含む)
        condition:境界条件(periodic,open)
        """

        if condition == "periodic":
            # 車両の位置更新
            for i in range(len(vehicles)):
                vehicles[i].position = vehicles[i].position % setting.Const().ROAD_LENGTH
            
            #車両の先行車と車間距離の更新
            for j in range(len(vehicles)):
                vehicles[j].preciding_position = vehicles[(j+1)%len(vehicles)].position #先行車両の位置
                vehicles[j].gap = ((vehicles[(j+1)%len(vehicles)].position - vehicles[j].position) - setting.Const().VEHICLE_LENGTH) % setting.Const().ROAD_LENGTH
        
        elif condition == "open":
            #スライスにすることでvehiclesの削除をmainに適応することができる
            vehicles[:] = [vehicle for vehicle in vehicles if vehicle.position < setting.Const().ROAD_LENGTH]
            
            #車両の先行車と車間距離の更新(最前列以外)
            for j in range(len(vehicles)-1):
                vehicles[j].preciding_position = vehicles[(j+1)].position #先行車両の位置
                vehicles[j].gap = (vehicles[(j+1)].position - vehicles[j].position) - setting.Const().VEHICLE_LENGTH

            #最前列の車両だけ例外処理
            #先行車両は消えたものとして更新
            vehicles[-1].preciding_position = setting.Const().ROAD_LENGTH + setting.Const().MAX_SPEED
            vehicles[-1].gap = (vehicles[-1].preciding_position - vehicles[-1].position) - setting.Const().VEHICLE_LENGTH
            
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
    print(vars(vehicle1))
    print(vars(vehicle2))
    