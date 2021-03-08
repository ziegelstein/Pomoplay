#! /bin/python3

from flask import Flask
app = Flask(__name__)

#- /pomodoro
#    %- User validation -> User inputs auth, API returns token
#    - POST /pomodoro -> Create new Pomodoro (returns pomoId)
#    - GET  /pomodoro/{pomoId}/pomodoro -> Returns the state of current pomodoro (paused state, state type, state time, state duration)
#    - POST /pomodoro/{pomoId}/state -> request state change of the pomodoro
#    - POST /pomodoro/{pomoId}/pause -> request pause
#    - PUT  /pomodoro/{pomoId}/breaktime
#    - PUT  /pomodoro/{pomoId}/pomodorotime
#    - PUT  /pomodoro/{pomoId}/longbreaktime
#    - PUT  /pomodoro/{pomoId}/cycleamount
#    - GET  /pomodoro/{pomoId}/history -> dumps database history for pomoId

@app.route("/pomodoro",methods=["POST"])
def new():
    return "new user"

@app.route("/pomodoro/<pomoId>/pomodoro",methods=["GET"])
def pomodoro(pomoId):
    return "user = " + pomoId

@app.route("/pomodoro/<pomoId>/state",methods=["POST"])
def state(pomoId):
    return "request state change"

@app.route("/pomodoro/<pomoId>/pause",methods=["POST"])
def pause(pomoId):
    return "request pause"

@app.route("/pomodoro/<pomoId>/breaktime",methods=["PUT"])
def breaktime(pomoId):
    return "longbreaktime"

@app.route("/pomodoro/<pomoId>/pomodorotime",methods=["PUT"])
def pomodorotime(pomoId):
    return "pomodorotime"

@app.route("/pomodoro/<pomoId>/longbreaktime",methods=["PUT"])
def longbreaktime(pomoId):
    return "longbreaktime"

@app.route("/pomodoro/<pomoId>/cycleamount",methods=["PUT"])
def cycleamount(pomoId):
    return "cycleamount"

@app.route("/pomodoro/<pomoId>/history",methods=["GET"])
def history(pomoId):
    return "dumps database history"
