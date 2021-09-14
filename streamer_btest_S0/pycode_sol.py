###############################################################################
" pycode_sol "
###############################################################################
import pylib_hps as hp
#------------------------------------------------------------------------------
"""

This script is used to retrieve the simulation results.

The variable time_moment defines the required data set.

The data are loaded from pydata\time_#, with #=time_moment.

"""
###############################################################################
time_moment=0
###############################################################################

lgn=hp.lg.lgn2d(6,4)
fvs=hp.lg.fvs2d(lgn)
dgs=hp.lg.dgs2d(lgn)
grn=hp.lg.elm2d(lgn)

path="pydata/time_"+str(time_moment)

hps=hp.pickle.load(open(path+"/hps.bin"))

hps.load(path,dgs,fvs,lgn)

hps.getelm()

hps.rib_dgs_fvs()

hps.setpsn(grn)
hps.psndtn(grn)

###############################################################################

hps.step_psn(lgn)

sol=hps.getsol(4,lgn,fvs)

###############################################################################
