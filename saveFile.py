def save(num_steps_array, f):
    openfile = 'n_steps_'+ str(f) + '.txt'
    with open(openfile, 'w') as f:
        for value in num_steps_array:
            f.write("%s\n" % value)
