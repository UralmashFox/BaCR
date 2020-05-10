import gym
import numpy as np
import os
import rex_gym
import time
import configparser
import sys
from gym import spaces
env = gym.make('RexWalk-v0', render = True)
# env = gym.make(env, render = True)
# import rex_gym
env.reset()
steps = 200
episodes = 10
epoches = 100
pvariance = 0.1
# variance of initial parameters
ppvariance = 0.03
# variance of perturbations
nhiddens = 50
# number of hidden neurons
# the number of inputs and outputs depends on the problem
# we assume that observations consist of vectors of continuous value
# and that actions can be vectors of continuous values or discrete actions
awards = np.zeros(episodes)
ninputs = env.observation_space.shape[0]
if (isinstance(env.action_space, gym.spaces.box.Box)):
    noutputs = env.action_space.shape[0]
else:
    noutputs = env.action_space.n
# initialize the training parameters randomly by using a gaussian distribution with
#average 0.0 and variance 0.1
# biases (thresholds) are initialized to 0.0
W1 = np.random.randn(nhiddens,ninputs) * pvariance
# first layer
W2 = np.random.randn(noutputs, nhiddens) * pvariance
# second layer
b1 = np.zeros(shape=(nhiddens, 1))
# bias first layer
b2 = np.zeros(shape=(noutputs, 1))
# bias second layer
W1_all = [W1 for i in range (episodes)]
W2_all = [W2 for i in range (episodes)]
b1_all = [b1 for i in range (episodes)]
b2_all = [b2 for i in range (episodes)]

W1_all_copy = W1_all
W2_all_copy = W2_all
b1_all_copy = b1_all
b2_all_copy = b2_all
for epoch in range(epoches):
    awards = np.zeros(episodes)
    print ('epoch', epoch)
    for episode in range(episodes):
        observation = env.reset()
        if epoch==0:
            W1 = np.random.randn(nhiddens,ninputs) * pvariance
            # first layer
            W2 = np.random.randn(noutputs, nhiddens) * pvariance
            # second layer
            b1 = np.zeros(shape=(nhiddens, 1))
            # bias first layer
            b2 = np.zeros(shape=(noutputs, 1))
            # bias second layer
            W1_all[episode] = W1
            W2_all[episode] = W2
            b1_all[episode] = b1
            b2_all[episode] = b2
        else:
            W1 = W1_all[episode]
            # first layer
            W2 = W2_all[episode]
            # second layer
            b1 = b1_all[episode]
            # bias first layer
            b2 = b2_all[episode]
        for step in range(steps):
            env.render()
            # env = gym.make(env, render = True)
            # observation, reward, done, info = env.step(env.action_space.sample())
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
            # if (isinstance(env.action_space, gym.spaces.box.Box)):
            #     action = 
            # else:
            action = np.argmin(A2)
            observation, reward, done, info = env.step(action)
            awards[episode] += reward
    print(awards)
    n = 0
    while n<(len(awards)/2):
        max_award = np.argmin(abs(awards))
        W1_all_copy[n] = W1_all[max_award]
        W2_all_copy[n] = W2_all[max_award]
        b1_all_copy[n] = b1_all[max_award]
        b2_all_copy[n] = b2_all[max_award]
        awards[max_award] = awards[max_award]
        n = n+1
    while n<len(awards):
        W1_all_copy[n] = W1_all_copy[n-int(len(awards)/2)]+np.random.normal(0,ppvariance,W1_all_copy[n].shape)
        W2_all_copy[n] = W2_all_copy[n-int(len(awards)/2)]+np.random.normal(0,ppvariance,W2_all_copy[n].shape)
        b1_all_copy[n] = b1_all_copy[n-int(len(awards)/2)]
        b2_all_copy[n] = b2_all_copy[n-int(len(awards)/2)]
        n += 1
    W1_all = W1_all_copy
    W2_all = W2_all_copy
    b1_all = b1_all_copy
    b2_all = b2_all_copy
    # print(W1_all[0])
    # print(W1_all[5])
env.close()