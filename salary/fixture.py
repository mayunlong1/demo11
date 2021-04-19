import linecache


def load_yaml():
    the_line = linecache.getline('demo.yaml', 2)
    print(the_line)

print(load_yaml())
