import os
import json
import string
import argparse

TEMPLATE_DIR = 'templates'
VIEWER_TEMPLATE_FILENAME = 'viewer.html'


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
        return dict(objects=[obj.spec() for obj in self.objects])


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
