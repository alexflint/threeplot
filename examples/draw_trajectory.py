import argparse
import numpy as np

import threeplot


def camera_center(P):
    P = np.asarray(P, float)
    return -np.dot(P[:, :3].T, P[:, 3])


def load_trajectory_from_text(path):
    data = np.loadtxt(path)
    if data.shape[1] == 14:
        timestamps = data[:, 0]
        poses = [row[1:-1].reshape((3, 4)) for row in data]
        positions = np.array(map(camera_center, poses))
    elif data.shape[1] == 4:
        timestamps = data[:, 0]
        positions = data[:, 1:]
    elif data.shape[1] == 23:
        timestamps = data[:, 0]
        positions = data[:, -3:]
    else:
        raise Exception('Found %d columns, which was not recognized' % data.shape[1])
    return timestamps, positions


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str)
    parser.add_argument('output', type=str)
    args = parser.parse_args()

    timestamps, positions = load_trajectory_from_text(args.input)

    axes = threeplot.Axes()
    axes.add_series(vertices=positions, line_width=2, line_color='0xff0000', line_style='solid')

    threeplot.dump(axes, args.output)


if __name__ == '__main__':
    main()
