import optavc
# This is an example of a CCSD(T) correction to a mp2/[TQ]Z hessian
# Note that programs, energy_regex, success_regex etc are blank
# xtpl_ counterparts should be filled in instead

# Two templates are required.
# For tempaltes there are two options:
# if the low correlation method can be grabbed from the output of the higher correlation method:
# xtpl_input_style should be [2, 2]. template2.dat should peform the MP2/TZ and QZ calculations
# see template2.dat for printing

# if this is not possible or desirable (looking at you SAPELO) need to do all three calculations
# with our low correlation method in template 2.dat xtpl_input_style should be [1, 3]

# To use we need 5 energy_regexes
# 1 or 2 programs strings are required
# 1 or 2 success strings are required. If just using psi4 use psi4's driver_cbs not xtpl
# The two above keywords must match

# need two adjacent basis sets zeta levels for xtpl_basis_sets
# can do a correction to the highest correlation method
# This was designed with (T) corrections in mind

options_kwargs = {
    'queue'              : "gen4.q,gen6.q",
    'input_name'         : "input.dat",
    'output_name'        : "output.dat",
    'maxiter'            : 100,
    'job_array'          : True,
    'print'              : 3,
    'max_force_g_convergence': 1e-6,
    'ensure_bt_convergence': True,
    'xtpl_templates'     : ["template1.dat", "template2.dat"],
    'xtpl_programs'      : ["molpro@2010.1.67+mpi", "psi4@master"],
    'xtpl_energy'        : [r"UCCSD\s*correlation\s*energy\s+(-?\d+\.\d+)",
                            r"\s*MP2\/QZ\scorrelation\senergy\s*(-\d*.\d*)",
                            r"\s*MP2\/TZ\scorrelation\senergy\s*(-\d*.\d*)",
                            r"\s+RHF-RMP2\scorrelation\senergy\s+(-\d*.\d*)",
                            r"\s*SCF\/QZ\s+reference\senergy\s*(-\d*.\d*)"],
    'xtpl_corrections'   : r"\s*Triples\s*\(T\)\s*contribution\s+(-\d*.\d*)", 
    'xtpl_success'       : [r"Variable\smemory\sreleased", r"beer"],
    'xtpl_basis_sets'    : [4, 3],
    "xtpl_input_style"   : [2, 2]
}

optavc.run_optavc("HESS", options_kwargs, sow=True)
