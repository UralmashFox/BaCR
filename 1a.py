import gym
env = gym.make('Humanoid-v2')
env.reset()
for _ in range(20000):
    env.render()
    observation, reward, done, info = env.step(env.action_space.sample())
env.close()