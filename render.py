import argparse

import numpy as np
from jinja2 import Environment, FileSystemLoader


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

	env = Environment(loader=FileSystemLoader('templates'))
	template = env.get_template('viewer.html')

	timestamps, positions = load_trajectory_from_text(args.input)

	lo = np.min(positions, axis=0)
	hi = np.max(positions, axis=0)
	positions -= (lo + hi) / 2
	diameter = np.ceil(np.linalg.norm(hi - lo))
	num_grid_cells = int(diameter)

	with open(args.output, 'w') as fd:
		fd.write(template.render(vertices=positions,
								 diameter=diameter,
								 num_grid_cells=num_grid_cells));


if __name__ == '__main__':
	main()

