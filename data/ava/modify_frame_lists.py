for sp in ['train', 'val']:
    with open('frame_lists/{}_ori.csv'.format(sp), 'r') as f:
        lines = f.readlines()

    new_lines = []
    for i, l in enumerate(lines):
        if i == 0:
            new_lines.append(l)
        else:
            row = l.split(' ')
            row[3] = '{}/{:05d}.jpg'.format(row[0], int(row[2])+1)
            new_lines.append(' '.join(row))

    with open('frame_lists/{}.csv'.format(sp), 'w') as f:
        f.writelines(new_lines)
