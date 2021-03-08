# Pomodoro Game

[MD Pad](https://hackmd.io/b4w7p5jnQbilVrhoMNWm3w)

# Game design

Idle game - Pomodoro Crossover

Counting down clock
Client is required to act when the countdown reaches zero

## Classic Pomodoro Rules

- Has three phases

  - Pomodoro
    - Usually 15 - 25 Minutes, time to do work
  - Short Break
    - Usually 5 Minutes, happens after every Pomodoro
  - Long Break
    - 10 - 15 Minutes, happens after 3 - 4 Pomodoro Cycles

- The more pomodoros are done the better
- A pomodoro can be stopped

## Game state

Adjustable time scale

while true
while true
pomodoro(timePomodoro)
shortBreak(timeShort)
longBreak(timeLong)

# Interface

## Client side - react app

Views:

Counting down clock
Action buttom
Pause buttom
Configs: adjustabable time for

- pomodoro
- short break
- long break

POST?

## Server side

Create client

Client state

- Paused
- Phase
  - Time

Saved data

- Interaction history

Client score

- ?

### Example API

- /user
- /pomodoro
  %- User validation -> User inputs auth, API returns token
  - POST /pomodoro -> Create new Pomodoro (returns pomoId)
  - GET /pomodoro/{pomoId}/pomodoro -> Returns the state of current pomodoro (paused state, state type, state time, state duration)
  - POST /pomodoro/{pomoId}/state -> request state change of the pomodoro
  - POST /pomodoro/{pomoId}/pause -> request pause
  - PUT /pomodoro/{pomoId}/breaktime
  - PUT /pomodoro/{pomoId}/pomodorotime
  - PUT /pomodoro/{pomoId}/longbreaktime
  - PUT /pomodoro/{pomoId}/cycleamount
  - GET /pomodoro/{pomoId}/history -> dumps database history for pomoId

#### Objects

**pomodoro**

- pomoId
- paused flag
- **_state_**
  - statetype
  - time
  - duration
- **pomodoro-attributes** - pomodorotime - longbreaktime - breaktime - cycleamount
  **_history_** - timestamp
  pomoId ?The pomodoro object already has a id?
  stateFrom
  finished flag

Prob some database for persistent data.

- sqlsite - maybe mariaDB or postgresyl
  > [It has to set up a server I dont want to do that. Sqlite only needs a file]

# Tasks

## Sprint 1

- Setup Repository
  - Setup README
  - Setup Permissions
- Setup react project
  - Setup npm react project
  - Make design sketch
  - Setup router
  - Setup services for requests
  - Setup CSS/HTML Structure
- Setup python project (flask?)
  - Setup poetry project
    - Add dependencies
    - Initialize project
  - Setup db schema
  - Setup endpoiints
- Create poc

## Backlog

- Gamify the project
  - Come up with gameplay mechanics
- Dockerize the Project
- Add User management
- Setup CI/CD
