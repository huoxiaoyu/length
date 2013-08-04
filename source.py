units = {
        'mile':'miles',
        'yard':'yards',
        'inch':'inches',
        'foot':'feet',
        'fath':'faths',
        'furlong':'furlong',
        }
rate = {}
if __name__ == "__main__":
    inp = open('input.txt')
    print 'huoxiaoyu90@163.com\n'
    while True:
        x = inp.readline()
        if len(x) == 1: break
        items = x.split(' ')
        rate[items[1]] = float(items[3])

    while True:
        x = inp.readline()
        if len(x) == 1: break
        items = x[:-1].split(' ')
        parts = len(items) / 3 + 1
        ans = 0.0
        for y in range(parts):
            key = [z for z in units if (items[y*3+1] in (z, units[z]))][0]
            if y and items[y*3-1] == '-': 
                ans -= rate[key]*float(items[y*3])
            else:
                ans += rate[key]*float(items[y*3])
        print '%.2f'%ans, 'm'
