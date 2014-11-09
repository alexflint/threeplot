# Threeplot

HTML-based 3D plotting in Python

Threeplot is a simple 3D plotting library for python. It generates HTML files as output, which contain an interactive 3D plots based on WebGL and Three.js. Reasons to use threeplot:

- *Installation is easy*. It has no dependencies whatsoever. There is no need to install Qt, wx, or any other GUI toolkit.

- *Collaboration is easy*. Output is a single HTML file, which is easy to share and publish.

### Installation:

```bash
$ pip install threeplot
```

### Usage:

Although this example uses numpy, threeplot itself does not depend on numpy.

```python
import numpy as np
import threeplot

axes = threeplot.Axes()

# Generate some sinusoids in the XY plane
xs = np.linspace(-10, 10, 10)
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

# Generate a point cloud
pts = np.random.randn(20, 3)
axes.add_series(vertices=pts,
                marker_size=5,
                marker_color='0x0000ff')

threeplot.dump(axes, 'out.html')
```

[View output of this example](https://rawgit.com/alexflint/threeplot/master/examples/output/draw_example.html)

