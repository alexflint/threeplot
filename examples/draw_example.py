import numpy as np

import threeplot


def main():
    axes = threeplot.Axes()

    # Generate some sinusoids in the XY plane
    xs = np.linspace(-10, 10, 40)
    ys = np.sin(xs * .2) * 2
    zs = np.zeros(len(xs))
    axes.add_series(vertices=zip(xs, ys, zs),
                    line_width=2,
                    line_color='0xff0000',
                    line_style='solid')

    axes.add_series(vertices=zip(xs, ys + 5, zs),
                    line_width=5,
                    line_color='0x00ff00',
                    line_style='dashed')

    axes.add_series(vertices=zip(xs, ys - 5, zs),
                    line_width=10,
                    line_color='0x555500',
                    line_style='dotted')

    zs = np.linspace(-12, 12, 50)
    axes.add_series(vertices=zip(np.sin(zs), np.cos(zs), zs),
                    line_width=3,
                    line_color='0x009999',
                    line_style='solid')

    # Generate a point cloud
    pts = np.random.randn(50, 3)
    axes.add_series(vertices=pts,
                    marker_size=5,
                    marker_color='0x0000ff')

    threeplot.dump(axes, 'out/out.html')


if __name__ == '__main__':
    main()
