# Task 4

- [x] meet with command showrobot.py (shows available model which can be rendered). Example of result with hopper model:

![x](https://i.imgur.com/6fRL880.png)

- [x] were evolved halfcheetah and hopper with evolutionary algorythm ([hopper](https://youtu.be/DwQCBcstS-s) jumping and [hafcheetah](https://youtu.be/cbRsPp8j0A0) running mostly in a good manner) and reinforcement (hopper didn't change it position and halfcheetah was falling in the very first steps). 

Seems like it happens because in evolutionary algorythm there are some random values, from hich the best are taken and training again. At the same time reinforcement learning was developed for step-by-step (gradient) learning. If to take into account all penalties which are in the script (connected to energy consumption, touching be leg another leg), it means that finding out the best solution takes much more time.

# Task 5

- [x] was created folder with all necessary files (you can see it in my [git](https://github.com/UralmashFox/BaCR) in branch 4_5_6). URDF-model and other files were studied. All packsge was compiled.
- [x] was created .ini file with policy in the *evorobotpy* folder.
- [x] the balance-bot was evaluted and teached by updated *evorobotpy/bin/es.py* file. Here is a photo of learning process:

![](https://i.imgur.com/okBv30z.png)

# Task 6

- [x] 10 replications of the experiment from the evorobotpy/xdiscrim folder were ran by using {5, 11, 15, 20, 25, 30, 35, 40, 45, 50} seeds.
- [x] the best results were:


| # Seed   | Results  |
| -------- | -------- |
| 5        | robot find goal -> stop near -> don't move (vibrating)    |
| 11       | touches nearest wall -> move left and down -> find goal -> circle around     |
| 15       | to observes center of field -> circling around goal in defferent ways     |
| 20       | spiral observing of centre field from wall to wall -> often not move around goal after finding     |
| 25       | observing field in triangular manner, not move around goal    |
| 35       |  weak attraction by goal     |
| 40       | go to goal mostly only if is goal near walls     |

Seeds 30, 45 and 50 were worst and trained again in a feedforward way. The results after retraining were following:

| # Seed   | Results  |
| -------- | -------- |
| 30       | model in spiral manner goes to goal -> don't move around goal| 
| 45       | goes from wall to goal and again to wall multiple times -> don't move around cylinder    | 
| 50       | goes either to wall (mostly) or goal and don't move in the end | 

So, there are some improvements in retraining, but, as I understood, if experiment with chosen seed is bad, no confidence that it will be better with another architecture.

![](https://i.imgur.com/Bxf6JFp.png)



