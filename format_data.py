from datetime import datetime

if __name__ == '__main__':
    out = open("data/cpu_usage.csv", "w")
    with open('mixer_server.log') as f:
        content = f.read().splitlines()
    base = 0
    for line in content:
        parts = line.split(',')
        time = int(datetime.strptime(parts[0], '%Y-%m-%d %H:%M:%S').timestamp())
        if base == 0:
            base = time
        out.write("%d,%d\n" % ((time - base) // 120, int(parts[1])))
    out.close()
