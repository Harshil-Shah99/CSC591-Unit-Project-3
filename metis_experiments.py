from nni.experiment import Experiment
start = time.time()
experiment = Experiment('local')
search_space = {
    'lr': {'_type': 'loguniform', '_value': [0.0001, 0.1]},
    'momentum': {'_type': 'uniform', '_value': [0, 1]},
}

experiment.config.trial_command = 'python main.py --epochs 10'
experiment.config.trial_code_directory = '.'
experiment.config.search_space = search_space
experiment.config.tuner.name = 'Metis'
experiment.config.tuner.class_args = {
    'optimize_mode': 'maximize',
    'exploration_probability': 0.2,
}
experiment.config.max_trial_number = 10
experiment.config.trial_concurrency = 2
experiment.run(8080)
print('Time taken for evolution experiments: {:.4f}'.format(end - start))
input('Press enter to quit')
experiment.stop()
