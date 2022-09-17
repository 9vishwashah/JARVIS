class Fruits:
    def __init__(self):

        self.__prglucose()

    def classfunction(self):
        print("will work fine for all the objects of this class.")

    def __prglucose(self):
        print("Prominantly glucose")
objFriut = Fruits()
objFriut.classfunction()
#objFriut.__prglucose()

