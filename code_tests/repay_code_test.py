# read the string filename
filename = input()

host_count = {}
with open(filename) as f:
    for line in f:
        host = line.split()[0]
        if host not in host_count:
            host_count[host] = 1
        else:
            host_count[host] += 1

with open('records_' + filename, 'w+') as the_file:
    for key, value in host_count.items():
        the_file.write(key + " " + str(value) + '\n')