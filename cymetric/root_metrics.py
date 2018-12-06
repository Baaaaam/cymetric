from __future__ import print_function, unicode_literals

from cymetric.evaluator import register_metric

def _genrootclass(name):
    """Creates a new root metric class."""
    class Cls(object):
        dependencies = ()

        @property
        def schema(self):
            """Defines schema for root metric if provided."""
            if self._schema is not None:
                return self._schema
            # fill in schema code

        @property
        def name(self):
            """Assigns a name to root metric object."""
            return self.__class__.__name__

        def __init__(self, db):
            """Constructor for root metric object in database."""
            self._schema = None
            self.db = db

        def __call__(self, conds=None, *args, **kwargs):
            """Retrieves a root metric with given input conditions."""
            if self.name not in self.db.tables:
                return None
            return self.db.query(self.name, conds=conds)

    Cls.__name__ = str(name)
    register_metric(Cls)
    return Cls


def root_metric(obj=None, name=None, schema=None, *args, **kwargs):
    """Decorator that creates a root metric from a function or class."""
    if obj is not None:
        raise RuntimeError
    if name is None:
        raise RuntimeError
    return _genrootclass(name=name)
