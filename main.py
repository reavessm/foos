import RPi.GPIO as GPIO
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.clock import Clock
import pyglet, random, os, time

class Team(Widget):
    score = NumericProperty(0)

class FoosGame(Widget):
    print("in Foos Game")
    team1 = ObjectProperty(None)
    team2 = ObjectProperty(None)
    winningTeam = StringProperty()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.IN)
    
    def update(self, dt):
        try:
            print("in try")
            time.sleep(2)
            if GPIO.input(23):
                print("in if")
                self.team1.score += 1
                print("I SEE U!")
                time.sleep(5)
            time.sleep(0.1)

            if self.team1.score >= 3:
                print("team 1 wins")
                winningTeam = "White Team"
                exit()
            #elif self.team2.score >= 3:
            #    winningTeam.team = "Blue Team"
        except:
            GPIO.cleanup()
	    print("FAIL!")

class FoosApp(App):
    def build(self):
        print("In Foos App")
        game = FoosGame()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

if __name__ == '__main__':
    FoosApp().run()
