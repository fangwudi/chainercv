import argparse
import matplotlib.pyplot as plot
import numpy as np

from chainercv.datasets.pascal_voc import voc_utils
from chainercv.links import SSD300
from chainercv.links import SSD512
from chainercv import utils
from chainercv.visualizations import vis_bbox


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--model', choices=('ssd300', 'ssd512'), default='ssd300')
    parser.add_argument('image')
    args = parser.parse_args()

    if args.model == 'ssd300':
        model = SSD300(pretrained_model='voc0712')
    elif args.model == 'ssd512':
        model = SSD512(pretrained_model='voc0712')

    img = utils.read_image(args.image, color=True)
    bboxes, labels, scores = model.predict(img[np.newaxis])
    bbox, label, score = bboxes[0], labels[0], scores[0]

    vis_bbox(
        img, bbox, label, score, label_names=voc_utils.pascal_voc_labels)
    plot.show()


if __name__ == '__main__':
    main()
