import gym
import numpy as np
env = gym.make('CartPole-v0')
pvariance = 0.1 # variance of initial parameters
ppvariance = 0.02 # variance of perturbations
nhiddens = 5 # number of hidden neurons
# the number of inputs and outputs depends on the problem
# we assume that observations consist of vectors of continuous value
# and that actions can be vectors of continuous values or discrete actions
ninputs = env.observation_space.shape[0]
if (isinstance(env.action_space, gym.spaces.box.Box)):
 noutputs = env.action_space.shape[0]
else:
 noutputs = env.action_space.n
# initialize the training parameters randomly by using a gaussian distribution with
# average 0.0 and variance 0.1
# biases (thresholds) are initialized to 0.0
a = 0
all_a = []
new_all_a = []
W1_all = []
W2_all = []
b1_all = []
b2_all = []

W1_new = []
W2_new = []
b1_new = []
b2_new = []
episodes = 10
for i_episode in range(episodes):
    W1 = np.random.randn(nhiddens,ninputs) * pvariance # first layer
    W1_all.append(W1)
    print(W1_all)
    W2 = np.random.randn(noutputs, nhiddens) * pvariance # second layer
    W2_all.append(W2)
    b1 = np.zeros(shape=(nhiddens, 1)) # bias first layer
    b1_all.append(b1)
    b2 = np.zeros(shape=(noutputs, 1)) # bias second layer
    b2_all.append(b2)
    observation, reward, done, info = env.reset()
    for sizesi_episode in range(200):
        env.render()
        # action = env.action_space.sample()
        # convert the observation array into a matrix with 1 column and ninputs rows
        observation.resize(ninputs,1)
        # compute the netinput of the first layer of neurons
        Z1 = np.dot(W1, observation) + b1
        # compute the activation of the first layer of neurons with the tanh function
        A1 = np.tanh(Z1)
        # compute the netinput of the second layer of neurons
        Z2 = np.dot(W2, A1) + b2
        # compute the activation of the second layer of neurons with the tanh function
        A2 = np.tanh(Z2)
        # if actions are discrete we select the action corresponding to the most activated unit
        if (isinstance(env.action_space, gym.spaces.box.Box)):
            action = A2
        else:
            action = np.argmax(A2)
        observation, reward, done, info = env.step(env.action_space.sample())
        print("observation", observation, "reward", reward, "done", done, "info", info)
        a = a+reward
    all_a.append(a)
    a = 0
# all_a = np.reshape(np.array(all_a), episodes)
# all_a_copy = all_a
# all_a = np.sort(all_a)
print(all_a)
for i in range (int(episodes/2)):
    # new_all = np.array(new_all_a.append(all_a[all_a.size-i-1]))
    # count = np.where(all_a[all_a.size-i-1] == all_a)
    count = np.argmax(all_a)
    # print(type())
    all_a[count] = int(min(all_a))
    W1_new.append(W1_all[count])
    W2_new.append(W2_all[count])
    b1_new.append(b1_all[count])
    b2_new.append(b2_all[count])
for i in range (int(episodes/2)):
    W1_new.append(W1_all[i]+ppvariance)
    W2_new.append(W2_all[i]+ppvariance)
    b1_new.append(b1_all[i]+ppvariance)
    b2_new.append(b2_all[i]+ppvariance)
W1_new = np.reshape(W1_new, (nhiddens, ninputs, episodes))
W2_new = np.reshape(W2_new, (noutputs, nhiddens, episodes))
b1_new = np.reshape(b1_new, (nhiddens, 1, episodes))
b2_new = np.reshape(b2_new, (noutputs, 1, episodes))
print ("new W1", W1_new.shape, "new W2", W2_new.shape, "new b1", b1_new.shape, "new b2", b2_new.shape)
print(W1_new)
print(W2_new)
print(b1_new)
print(b2_new)
env.close()
