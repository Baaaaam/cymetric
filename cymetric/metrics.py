"""A collection of metrics that come stock with cymetric.
"""
from __future__ import print_function, unicode_literals
import inspect

import numpy as np
import pandas as pd

try:
    from pyne import data
    import pyne.enrichment as enr
    HAVE_PYNE = True
except ImportError:
    HAVE_PYNE = False

from cyclus import lib
from cyclus import typesystem as ts

try:
    from cymetric import schemas
    from cymetric import tools
    from cymetric.evaluator import register_metric
except ImportError:
    # some wacky CI paths prevent absolute importing, try relative
    from . import schemas
    from . import tools
    from .evaluator import register_metric


class Metric(object):
    """Metric class"""
    dependencies = NotImplemented
    schema = NotImplemented

    def __init__(self, db):
        self.db = db

    @property
    def name(self):
        return self.__class__.__name__


def _genmetricclass(f, name, depends, scheme):
    """Creates a new metric class with a given name, dependencies, and schema.

    Parameters
    ----------
    name : str
        Metric name
    depends : list of lists (table name, tuple of indices, column name)
        Dependencies on other database tables (metrics or root metrics)
    scheme : list of tuples (column name, data type)
        Schema for metric
    """
    if not isinstance(scheme, schemas.schema):
        scheme = schemas.schema(scheme)

    class Cls(Metric):
        dependencies = depends
        schema = scheme
        func = staticmethod(f)

        __doc__ = inspect.getdoc(f)

        def __init__(self, db):
            """Constructor for metric object in database."""
            super(Cls, self).__init__(db)

        def __call__(self, frames, conds=None, known_tables=None, *args, **kwargs):
            """Computes metric for given input data and conditions."""
            # FIXME test if I already exist in the db, read in if I do
            if known_tables is None:
                known_tables = self.db.tables()
            if self.name in known_tables:
                return self.db.query(self.name, conds=conds)
            return f(*frames)

    Cls.__name__ = str(name)
    register_metric(Cls)
    return Cls


def metric(name=None, depends=NotImplemented, schema=NotImplemented):
    """Decorator that creates metric class from a function or class."""
    def dec(f):
        clsname = name or f.__name__
        return _genmetricclass(f=f, name=clsname, scheme=schema, depends=depends)
    return dec



