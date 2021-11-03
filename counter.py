
p = 'output.txt'
def tuplie_maker(p):
    with open(p, encoding='utf8') as f:
        all_lines = f.readlines()
    K = ' - b'
    results = []
    for line in all_lines:
        parts = line.split(K)
        results.append(parts)
    #for item in results:
    #    print(item)
    p = []
    for item in results:
        p.append(item)
    return p
print(tuplie_maker(p))