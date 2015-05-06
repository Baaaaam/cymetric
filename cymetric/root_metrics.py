"""A collection of basic metrics coming from the database that are 
generated by Cyclus itself.
"""
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


resources = root_metric(name='Resources')
compositions = root_metric(name='Compositions')
recipes = root_metric(name='Recipes')
products = root_metric(name='Products')
res_creators = root_metric(name='ResCreators')
agent_entry = root_metric(name='AgentEntry')
agent_exit = root_metric(name='AgentExit')
transactions = root_metric(name='Transactions')
info = root_metric(name='Info')
finish = root_metric(name='Finish')
input_files = root_metric(name='InputFiles')
decom_schedule = root_metric(name='DecomSchedule')
build_schedule = root_metric(name='BuildSchedule')
snapshots = root_metric(name='Snapshots')
debug_requests = root_metric(name='DebugRequests')
debug_bids = root_metric(name='DebugBids')
time_series_power = root_metric(name='TimeSeriesPower')

# Archetype-dependent custom tables that we know about
agentstate_agent = root_metric(name='AgentStateAgent')
agentstate_inventories = root_metric(name='AgentStateInventories')
agentstate_brightlite_fuelfabfacilityinfo = root_metric(
    name='AgentState_Brightlite_FuelfabFacilityInfo')
agentstate_brightlite_reactorfacilityinfo = root_metric(
    name='AgentState_Brightlite_ReactorFacilityInfo')
agentstate_brightlite_reprocessfacilityinfo = root_metric(
    name='AgentState_Brightlite_ReprocessFacilityInfo')
agentstate_agent_sinkinfo = root_metric(name='AgentState_agents_SinkInfo')
agentstate_agent_sourceinfo = root_metric(name='AgentState_agents_SourceInfo')
agentstate_cycamore_reactorinfo = root_metric(
    name='AgentState_cycamore_ReactorInfo')
brightlite_reactor_data = root_metric(name='BrightLite_Reactor_Data')
