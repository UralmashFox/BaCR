# Report
## Task 1
Firstly I tried to run the very first code with CartPole-v0 (script 1a) and I got following result:

![](https://i.imgur.com/nZ9QPEL.png)

Also I tried to run other environments, for example Atari-games:

![](https://i.imgur.com/0jiewER.png)

Then I pasted the second part of the first task (script 1b) and inspected the minimal and maximum values of
each observation and action elements: 

![](https://i.imgur.com/MYCKPX8.png)

## Task 2
### part - a
Firstly I ran simple random iterations (script new2a.py) and got following results:

![](https://i.imgur.com/rEdoVcx.png)

obviously, model was falling every time.
### part - b
Then I write evolutional part (script new2b.py). Model became more stable (what can be detected in every running). And after a small ammount of iteration all the awards became maximum and pendulum became stable! BUT! As I said it happens in each running, but when I ran it firstly - the pendulum was falling. Now it's OK.

![](https://i.imgur.com/WiuP3rp.png)

When I increased variance for recomputing weights and biases up to 0.5, Cart became unstable after 5-th episode. But somehow sometimes it could balance. At the same time I increased numder of hidden neurons up to 15 and after 8-th iteration CartPole bacame more stable even after 5-th iretarion, but it got about 10 populations. Seems like good random numbers.

## Task 3
- I installed the libraries net*.so net*.dll in *bin* directory by:
```
`python3 setupevonet.py build_ext --inplace
cp net*.so ../bin # or cp net*.dll ../bin`
```
- I studied the structure of creation network policy by:
```
bin/testnet.py
```
- I met with parameters of network by:
```
bin/es.py
```
- I studied an *acrobat* by:
```
python3 ../bin/es.py -f acrobot.ini -s 11
```
were used a lot of seeds such as 1, 10, 11, 22, 77 and so on. Finally I got results by following commands for visualazing model:
```
python3 ../bin/es.py -f acrobot.ini -t bestgS11.npy
```
and visualizing results:
```
python3 ../bin/plotstat.py
python3 ../bin/plotave.py
```
Results:

![](https://i.imgur.com/2buvL1v.png)

So, I can see that actually there are not big differences, but with seed = 77 there is a bigger variance.
Moreover, I tried to tune in *acrobot.ini* some parameters as **ntrials** (gave more steps for visualization), **maxsteps**, **stepsize**, **sampleSize** (let to correct overfitting).
Also I tried to run other environment such as *humanoid*, *hopper* and so on, but they takes a lot of time to training (5 mins for 1% done)

