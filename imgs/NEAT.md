### NEAT
- 3 input neurons
one output neurons
neat changes weights 
and add other nodes
and remove and add connection
to find a toplogy that works best for problem solving.

neural network being evolved using a genetic algooo.

- **_Inputs_**: Bird Y, Top Pipe, Buttom Pipe
- **_Outputs_**: Jump (Yes,No)
- **_Activation function_**: TanH ( output value will be in range 1: jump or -1: no jump)
- **_Population size_**: 100 (more population more variance more randomness.)
- **_Fitness function_**: how far you can gettt in level..(**distance**)
- **_Max generations_**: try again after max gen: 30


##### config-feedforward.txt:
- **Try these changes**:
    - `fitness_criterion = min`
    - `fitness_threshold= 100` : we stop running program when fitness reaches this level.
    - `reset_on_extinction` : 3 i/p one o/p is one species

    - [neat-python.docs](https://neat-python.readthedocs.io/en/latest/)