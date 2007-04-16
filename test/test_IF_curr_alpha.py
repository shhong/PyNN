"""
Simple test to compare iaf_neuron in NEST with IFAlphaI in NEURON.

Andrew Davison, UNIC, CNRS
May 2006

$Id$
"""

import sys

if hasattr(sys,"argv"):     # run using python
    simulator = sys.argv[1]
else:
    simulator = "neuron"       # run using nrngui -python


exec("from pyNN.%s import *" % simulator)

try:
    setup(timestep=0.025)

    ifcell = create('IF_curr_alpha',{'i_offset':0.1,'tau_refrac':5.0,'v_thresh':-51.0,'tau_syn':2.0})
    
    spike_source = create('SpikeSourceArray',{'spike_times': [float(i) for i in range(5,105,10)]})
     
    conn = connect(spike_source,ifcell,weight=1.5)
    #for item in pynest.getDict([spike_source])[0].items():
    #    print "%-20s %s" % item
        
    record_v(ifcell,"test_IF_curr_alpha_%s.v" % simulator)
    run(100.0)
    
finally:
    end()
