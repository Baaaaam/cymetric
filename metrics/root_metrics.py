"""A collection of basic metrics coming from the database that are
generated by Cyclus itself.
"""
from cymetric.root_metrics import root_metric


#core tables
resources = root_metric(name='Resources')
compositions = root_metric(name='Compositions')
recipes = root_metric(name='Recipes')
products = root_metric(name='Products')
res_creators = root_metric(name='ResCreators')
transactions = root_metric(name='Transactions')
info = root_metric(name='Info')
time_step_dur = root_metric(name='TimeStepDur')
finish = root_metric(name='Finish')
input_files = root_metric(name='InputFiles')
decom_schedule = root_metric(name='DecomSchedule')
build_schedule = root_metric(name='BuildSchedule')
snapshots = root_metric(name='Snapshots')
debug_requests = root_metric(name='DebugRequests')
debug_bids = root_metric(name='DebugBids')
explicit_inventory = root_metric(name='ExplicitInventory')
explicit_inventory_compact = root_metric(name='ExplicitInventoryCompact')

#where do these tables come from?
commod_priority = root_metric(name='CommodPriority')
decay_mode = root_metric(name='DecayMode')
field_types = root_metric(name='FieldTypes')
material_info = root_metric(name='MaterialInfo')
next_ids = root_metric(name='NextIds')
prototypes = root_metric(name='Prototypes')
xmlpp_info = root_metric(name='XMLPPInfo')

#general agent state tables
agent_entry = root_metric(name='AgentEntry')
agent_exit = root_metric(name='AgentExit')
agent_versions = root_metric(name='AgentVersions')
agentstate_agent = root_metric(name='AgentStateAgent')
agentstate_inventories = root_metric(name='AgentStateInventories')

#tables about solvers
greedy_solver_info = root_metric(name='GreedySolverInfo')
exchange_solver_info = root_metric(name='ExchangeSolverInfo')
prog_solver_info = root_metric(name='ProgSolverInfo')
solver_info = root_metric(name='SolverInfo')

#cyclus archetype tables
agentstate_agents_nullinstinfo = root_metric(
    name='AgentState_agents_NullInstInfo')
agentstate_agents_nullregioninfo = root_metric(
    name='AgentState_agents_NullRegionInfo')
agentstate_agent_sinkinfo = root_metric(
    name='AgentState_agents_SinkInfo')
agentstate_agent_sourceinfo = root_metric(
    name='AgentState_agents_SourceInfo')

#toolkit-enabled tables
time_series_power = root_metric(name='TimeSeriesPower')
time_series_enrichmentfeed = root_metric(name='TimeSeriesEnrichmentFeed')
time_series_enrichmentswu = root_metric(name='TimeSeriesEnrichmentSWU')
