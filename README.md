# Development of a locomotor environment based on an real biped or quadruped robotic platform

## Abstract
Simulation of robot is very important step is modern technology. It makes testing easier, cheaper and allows to modify environments, inputs, and so on. In this work development of environment of Laikago robot, based on created environment from https://github.com/nicrusso7/rex-gym, is presented. There are described results of experiments with changing reward functions and desired coordinate as an input.

## Goal
Try to find the best reward functions for each of the environments (walking, turning, galloping, standing up)

## Tasks
* Become familiar with package;
* describe reward functions;
* try to experiment;
* find out which experiment was the best with which reward function.

## Rex-gym
in the git there are already pre-evolved models which represent trained model. You can see them here: turning, walking, galloping, standing up.

## Reward functions
Instead of 4 rewards for each environment, there are only 3: turning, standing up, walking + galloping. The last 2 were combined, because galloping is limited for the time. In the next there will be descriptions for each reward function.

### Turning
The reward of turning is based on position and orientation. If to set target position and orientation, then sum of differences per each x, y, z - axes and roll, pitch, yaw anlges and results in some moment of a time are 2 errors.
Primarily, if difference between target and results is less then 0.1, then model worked succesfully.
In the beginning, the reward is: reward = position_reward + proximity_reward, where proximity_reward is an orientational reward. In the future there will be discussion about changes in coefficients.

### Standing up
The reward of standing up is based only on the coordinates x, y, z: reward = position_reward. The error in which is can be said that model succeded is again 0.1. Also there is "jump!" - warning written in the reward (in case if z is twice more than target). But it doesn't play any role in the lerning process.

### Walking + Galloping
The reward for both these environment is common and based on distance, energy, shake, drift, max available reward. It just sums up all these errors with all the coeffitions equal to 1.
The only important difference is in the reset function: for galloping there is a dependancy on time limit. At the same time no limits in time for other environment (only restriction is time for each step).

## Coefficient changing and experiments
There were done experiments in case to check reward function on their productivity.

### Turning
As far as there are 2 variables in the reward function, both coefficients may be changed.
If to increase coefficient for coordinate error the model in a process of learning will just stand in one location or will try to turn and freeze in some coodinate as it shown [there](https://studio.youtube.com/video/cFqn0hx-tTI/edit).
Otherwise, if to increase weight for orientation error, and decrease position, model will turn and change position, as far as it's not so important now. The result is [here](https://youtu.be/CV7unrleLK8)

### Standing Up
This environment is the most robust and the simpliest. THe only problem which was detected is the falling after standing, as you can see [here](https://www.youtube.com/watch?v=9MCefvkMpKc). To solve this problem I tried to do following:
- [x] increase/dicrease coefficient
- [x] change target z-coordinate
- [x] change seed

Unfortunatelly, nothing helped.

### Walking
The final result of the evolution strategy on the 11-th seed is shown [here](https://youtu.be/_LXAq0rcTUo). As far as there is no restriction on time, the process is slow, but pretty good-looking.
The least succesfull experience was with increasing drift coefficient: model starts having problems with back legs, as can be seen [here](https://youtu.be/lNKeHifVmMk)

### Galloping
The final result of the evolution strategy on the 16-th seed is shown [here](https://youtu.be/AtWtqh63LlQ). And it differs from the original version by [reinforcement learning](https://youtu.be/Iiwo-fY63r0). There were attempts to change coefficients like for "RexWalking" environment, but the changes for better output weren't achived.

## Conclusion
As can be seen from done work, the easiest environment was "StandingUp". Thats it, because the reward function as is the simpliest from all 4. Evolution strategy can take place here.
The hardest one was "Galloping" environment. Of course, here can be done evolution too. On the other hand, reinforcement learning does this work much better.
What is more, if to compare rewards for different environments, they're differ. Changes of coefficient at the same places for one environment may lead to not the same results as in another environment.
Reinforcement learning did much better in comprehensive situation and evolution algorythm did its best in a more simple. By the way, evolution also can be handy for every given environment.


