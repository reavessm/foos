import RPi.GPIO as GPIO
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.image import Image
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.clock import Clock
import random, os, time
import sqlite3

# To get kivy to play video streams, look at
# github.com/atuldo/videoStream/blob/master/videoStream.py
# The address will be http://localhost:8082

# To scroll with tmux, hit Ctrl+b then [.  Press q to quit scroll mode 

class SQL(object):
    conn = sqlite3.connect('foos.db')
    c = conn.cursor()

    c.execute("DROP TABLE IF EXISTS Scores")
    c.execute("CREATE TABLE Scores (team TEXT, score INTEGER)")
    c.execute("INSERT INTO Scores VALUES ('White', 0), ('Blue', 0)")
    c.execute("CREATE TABLE IF NOT EXISTS History (blueScore INTEGER, \
        whiteScore INTEGER, winner TEXT, datetime DATETIME)")

    #def __init__(self, fileName='foos.db'):
	#self.conn = sqlite3.connect(fileName)
	#c = self.conn.cursor()

#        self.c.execute("DROP TABLE IF EXISTS Scores")
#        self.c.execute("CREATE TABLE Scores (team TEXT, scoreINTEGER)")
#	self.c.execute("INSERT INTO Scores VALUES ('White', 0), ('Blue', 0)")
#	self.c.execute("CREATE TABLE IF NOT EXISTS History (blueScore INTEGER, \
#	    whiteScore INTEGER, winner TEXT, datetime DATETIME)")
    
    def whiteScore(self):
        print("WhiteScore")
        statement = "UPDATE Scores SET score = score + 1 WHERE team = 'White'"
        print(statement)
        self.c.execute(statement)
        print("Post execute")
        self.conn.commit()
        print("Post commit")

    def blueScore():
        statement = "UPDATE Scores SET score = score + 1 WHERE team = 'Blue'"
        print(statement)
        self.c.execute(statement)
        print("Post execute")
        self.conn.commit()
        print("Post commit")

    def gameOver():
        self.c.execute("INSERT INTO History VALUES ((SELECT score FROM Scores \
                WHERE team = 'Blue'), (SELECT score FROM Scores WHERE team = \
                'White'), (SELECT team FROM Scores WHERE score = (SELECT \
                max(score) FROM Scores)), datetime('now', 'localtime'))")
        self.conn.commit()
        self.conn.close()

class Team(Widget):
    score = NumericProperty(0)

class FoosGame(Widget):
    team1 = ObjectProperty(None)
    team2 = ObjectProperty(None)
    winningTeam = StringProperty()

    sql = SQL()

    def __init__(self, **kwargs):
        super(FoosGame, self).__init__(**kwargs)
        self.img = Image(source = "./pic/" + str(random.choice(os.listdir("./pic"))))
        self.add_widget(self.img)
        self.img.size = (1000, 800)
        self.img.pos = self.pos
        self.img.allow_stretch = True
        self.img.opacity = 0.0

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.IN)
    GPIO.setup(22, GPIO.IN)

    print("LOADING THE GAME...")
    time.sleep(10)
    print("FINISHED LOADING.")

    def update(self, dt):

        try:
            if GPIO.input(23):
                self.team1.score += 1
                os.system('python video.py')
                print("Team White scored.")
                self.sql.whiteScore()
                time.sleep(5)

            if GPIO.input(22):
                self.team2.score += 1
                os.system('python video.py')
                print("Team Blue scored.")
                #self.sql.blueScore
                time.sleep(5)

            if self.team1.score >= 10:
                print("team 1 wins")
                self.winningTeam = "White Team Wins!"
                self.img.opacity = 1.0
                self.img.source = "./pic/" + str(random.choice(os.listdir("./pic")))
                self.img.reload()
                #self.sql.gameOver()
            elif self.team2.score >= 10:
                self.winningTeam = "Blue Team Wins!"
                #self.sql.gameOver()
                self.img.opacity = 1.0
                self.img.source = "./pic/" + str(random.choice(os.listdir("./pic")))
                self.img.reload()
            
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
