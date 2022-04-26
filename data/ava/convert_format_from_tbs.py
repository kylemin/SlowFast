import pickle
FPS = 30
AVA_VALID_FRAMES = range(902, 1799)

ver = 'v2.2'
for sp in ['train', 'val']:
    if sp == 'train':
        file_tubelets = '/datasets/ava-actions/data_serialized/ava_{}_{}_tubelets.pkl'.format(sp, ver)
    else:
        file_tubelets = '/datasets/ava-actions/data_serialized/ava_{}_tubelets.pkl'.format(sp)

    with open(file_tubelets, 'rb') as f:
        tubelets = pickle.load(f)

    lines = []
    for v in sorted(tubelets.keys()):
        for ktid, tbs in enumerate(tubelets[v]):
            t = AVA_VALID_FRAMES[ktid]
            for it, (first_i, s, b, a) in enumerate(tbs):
                x1, y1, x2, y2 = b[-first_i]
                line = '{},{:04d},{:.3f},{:.3f},{:.3f},{:.3f},,{:.6f}'.format(v, t, x1, y1, x2, y2, 0.999999)
                lines.append(line+'\n')

    with open('annotations/ava_{}_predicted_boxes.csv'.format(sp), 'w') as f:
        f.writelines(lines)
