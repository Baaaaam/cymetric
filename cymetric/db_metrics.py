"""A collection of metrics that come stock with cymetric.
"""
import pandas as pd
try:
    from pyne import data
    import pyne.enrichment as enr
    HAVE_PYNE = True
except ImportError:
    HAVE_PYNE = False
from cyclus import typesystem as ts

from cymetric import metric
from cymetric import tools


#####################
## General Metrics ##
#####################

_matdeps = []

_matschema = [
    ('SimId', ts.UUID),
    ('Table', ts.STRING),
    ('Units', ts.STRING)
    ]

@metric(name='Normalisation', depends=_matdeps, schema=_matschema)
def normalisation():
    normal = pd.DataFrame(columns=['SimId', 'Table', 'Units'])

    return normal


del _matdeps, _matschema


