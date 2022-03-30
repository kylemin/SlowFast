import pickle
FPS = 30
AVA_VALID_FRAMES = range(902, 1799)

sp = 'train'
#sp = 'val'

file_detections = '/datasets/ava-actions/data_serialized/ava_{}_detections.pkl'.format(sp)
with open(file_detections, 'rb') as f:
    bboxes, scores = pickle.load(f)

lines = []
for v in sorted(bboxes.keys()):
    for t in AVA_VALID_FRAMES:
        kfid = (t-900)*FPS
        for i, b in enumerate(bboxes[v][kfid]):
            l = '{},{:04d},{:.3f},{:.3f},{:.3f},{:.3f},,{:.6f}'.format(v, t, b[0], b[1], b[2], b[3], scores[v][kfid][i])
            lines.append(l+'\n')

with open('annotations/ava_{}_predicted_boxes.csv'.format(sp), 'w') as f:
    f.writelines(lines)
