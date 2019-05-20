import RPi.GPIO as GPIO
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.image import Image
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.clock import Clock
import random, os, time

class Team(Widget):
    score = NumericProperty(0)

class FoosGame(Widget):
    team1 = ObjectProperty(None)
    team2 = ObjectProperty(None)
    winningTeam = StringProperty()
    img = Image()

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.IN)
    GPIO.setup(22, GPIO.IN)
    
    print("LOADING THE GAME...")
    time.sleep(10)
    print("FINISHED LOADING.")

    def update(self, dt):

        #self.img.disabled

        try:
            if GPIO.input(23):
                self.team1.score += 1
                print("Team White scored.")
                #self.img.disabled = False
                #self.img.source = './pic/Mario-Balotelli-Playing-Foosball.jpg'
                time.sleep(5)
                #self.img.source = ''
                #self.img.disabled = True

            if GPIO.input(22):
                self.team2.score += 1
                print("Team Blue scored.")
                time.sleep(5)

            if self.team1.score >= 10:
                print("team 1 wins")
                self.winningTeam = "White Team Wins!"
            elif self.team2.score >= 10:
                self.winningTeam = "Blue Team Wins!"
            
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
