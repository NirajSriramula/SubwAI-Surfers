from callback import TrainAndLoggingCallback
from environment import WebGame

SAVE_DIR = './train/'
LOG_DIR = './logs/'
callback = TrainAndLoggingCallback(check_freq=1000, save_path=SAVE_DIR)
env = WebGame()
from stable_baselines3 import DQN
model = DQN('CnnPolicy', env, tensorboard_log=LOG_DIR, verbose=1, buffer_size=1200000, learning_starts=1000)
model.learn(total_timesteps=5000, callback= callback)