def save(num_steps_array):
    with open('n_steps.txt', 'w') as f:
        for value in num_steps_array:
            f.write("%s\n" % value)
