#!/usr/local/bin/python

"""

Illustrate the use of switch to construct and run a very simple model
with a single load zone, one investment period, and two timepoints.
This model neglects local transmission and distribution as well.

For this to work, you need to ensure that the switch_mod package
directory is in your python search path. See the README for more info.

"""

from pyomo.environ import *
from pyomo.opt import SolverFactory
from switch_mod.utilities import define_AbstractModel

switch_model = define_AbstractModel(
    'switch_mod', 'project.no_commit', 'fuel_cost')
switch_instance = switch_model.load_inputs(inputs_dir="inputs")

opt = SolverFactory("cplex")

results = opt.solve(switch_instance, keepfiles=False, tee=False)
switch_instance.load(results)

results.write()
switch_instance.pprint()
