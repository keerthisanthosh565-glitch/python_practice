class Animal:
    def eat(self):
        print("Animal eat")

class walker:
    def walker(self):
        print("walk")

class Dog(Animal,walker):
    def bark(self):
        print("Barks")

dog = Dog()
dog.eat()
dog.walker()
dog.bark()

#********************************#

class Camera:
    def Takephoto(self):
        print("capturing photo")

class Call:
    def makecall(self):
        print("calling friends")

class Smartphone(Camera,Call):
    def internet(self):
        print("Browsing internet")

smartphone= Smartphone()
smartphone .internet()
smartphone.makecall()
smartphone.Takephoto()

#*********************************************#

class Mediaplayer:
    def play_video(self):
        print("playing video")

class InternetDevice:
    def connect_wifi(self):
        print("connect to wifi")

class SmartTv(Mediaplayer,InternetDevice):
    def change_channel(self):
        print("changing Tv channel")

smartTv=SmartTv()
smartTv.play_video()
smartTv.connect_wifi()
smartTv.change_channel()

#*******************************************#

