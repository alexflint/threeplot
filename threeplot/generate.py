import os
import json
import math
import string

TEMPLATE_DIR = 'templates'
VIEWER_TEMPLATE_FILENAME = 'viewer.html'


def min_axis0(xs):
    """We want to avoid a strict dependency on numpy but we still want to use efficient
    numpy array funcs when an ndarray is given to us."""
    if hasattr(xs, 'min'):
        return xs.min(axis=0)
    else:
        return [min(x[i] for x in xs) for i in range(3)]


def max_axis0(xs):
    """We want to avoid a strict dependency on numpy but we still want to use efficient
    numpy array funcs when an ndarray is given to us."""
    if hasattr(xs, 'min'):
        return xs.max(axis=0)
    else:
        return [max(x[i] for x in xs) for i in range(3)]


class Axes(object):
    def __init__(self):
        self._objects = []

    @property
    def objects(self):
        return self._objects

    def add(self, obj):
        self._objects.append(obj)

    def add_series(self, *args, **kwargs):
        self._objects.append(Series(*args, **kwargs))

    def spec(self):
        lo, hi = self.compute_bounds()
        lo = map(math.floor, lo)
        hi = map(math.ceil, hi)
        grid_spec = dict(xmin=lo[0],
                         ymin=lo[1],
                         xmax=hi[0],
                         ymax=hi[1],
                         xspacing=1,
                         yspacing=1)
        return dict(grid=grid_spec,
                    objects=[obj.spec() for obj in self.objects])

    def compute_bounds(self):
        lo = min_axis0([min_axis0(obj.vertices) for obj in self.objects])
        hi = max_axis0([max_axis0(obj.vertices) for obj in self.objects])
        return lo, hi


class Series(object):
    def __init__(self,
                 vertices=None,
                 line_width=None,
                 line_color='0xff0000',
                 line_style='solid',
                 marker_size=None,
                 marker_color='0xff0000'):
        self.vertices = vertices
        self.line_width = line_width
        self.line_color = line_color
        self.line_style = line_style
        self.marker_size = marker_size
        self.marker_color = marker_color

    def spec(self):
        return dict(type='series',
                    vertices=map(list, self.vertices),
                    line_width=self.line_width,
                    line_color=self.line_color,
                    line_style=self.line_style,
                    marker_size=self.marker_size,
                    marker_color=self.marker_color)


def load_template(name):
    path = os.path.join(os.path.dirname(__file__), TEMPLATE_DIR, name)
    with open(path, 'r') as fd:
        return string.Template(fd.read())


def dumps(axes):
    viewer_tpl = load_template(VIEWER_TEMPLATE_FILENAME)
    spec = json.dumps(axes.spec(), indent=4, separators=(',', ': '))
    return viewer_tpl.substitute(spec=spec)


def dump(axes, path_or_file):
    html = dumps(axes)
    fd = open(path_or_file, 'w') if isinstance(path_or_file, basestring) else path_or_file
    fd.write(html)


def foo():
    print __package__
    print type(__package__)
