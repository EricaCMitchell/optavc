import optavc

options_kwargs = {
  'template_file_path': "template.dat",
  'energy_regex'      : r"@DF-RHF Final Energy:\s+(-\d+\.\d+)",
  'success_regex'     : r"\*\*\* P[Ss][Ii]4 exiting successfully." ,
  'queue'             : "gen4.q",
  'program'           : "psi4@master",
  'input_name'        : "input.dat",
  'output_name'       : "output.dat",
  'submitter'         : submit,
  'maxiter'           : 20,
  'job_array'         : True,
  'g_convergence'     : "gau_verytight",
  'findif'            : {'points': 5}
}

optavc.run_optavc("OPT", options_kwargs, restart_iteration=0)
