from gpiozero import LED
from time import sleep
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty
from kivy.clock import Clock

class FoosGame(Widget):
    score = NumericProperty(0)
    team1 = ObjectProperty(None)
    team2 = ObjectProperty(None)
    
    def update(self, dt):
        self.team1.score += 1
        self.team2.score += 1

class FoosApp(App):
    
    def build(self):
        game = FoosGame()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

if __name__ == '__main__':
    FoosApp().run()


