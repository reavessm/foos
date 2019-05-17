import RPi.GPIO as GPIO
from time import sleep
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty
from kivy.clock import Clock

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
score = NumericProperty(0)
team1 = ObjectProperty(None)
team2 = ObjectProperty(None)

class FoosGame(Widget):
    def update(self, dt):
        try:
            time.sleep(2)
            while True:
                if GPIO.input(23):
                    time.sleep(0.5)
                    self.team1.score += 1
                    print("I SEE U!")
                    time.sleep(5)
                time.sleep(0.1)
        except:
            GPIO.cleanup()
            print("FAIL!")

class FoosApp(App):
    def build(self):
        game = FoosGame()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

if __name__ == '__main__':
    FoosApp().run()
