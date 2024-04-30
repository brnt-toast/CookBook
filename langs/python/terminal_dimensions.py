import os 

stats = os.get_terminal_size()
width, height, = stats.columns, stats.lines

print(width, height)
