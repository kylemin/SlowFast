import pickle

ver = 'v2.2'
for sp in ['train', 'val']:
    with open('annotations/ava_{}_v2.2.csv'.format(sp), 'r') as f:
        gt_lines = f.readlines()

    lines = []
    for gl in gt_lines:
        line = ','.join(gl.split(',')[:-2]) + ',,0.999999\n'
        if line not in lines:
            lines.append(line)

    with open('annotations/ava_{}_gt_boxes.csv'.format(sp), 'w') as f:
        f.writelines(lines)
