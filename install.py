import os
import subprocess
import sys


if __name__ == "__main__":
	if "--remove" in sys.argv:
		subprocess.call(['rm', '-rf', '~/.local/lib/python3.6/site-packages/IOniCS*'])
		subprocess.call(['rm', '-rf', '~/.local/lib/python3.8/site-packages/IOniCS*'])
	else:
		try:
			import dolfin
		except ImportError:
			subprocess.call(['pip3', 'install', 'mpi4py', '--upgrade', '--user'])
			subprocess.call(['pip3', 'install', 'petsc4py', '--upgrade', '--user'])
			subprocess.call(['pip3', 'install', 'slepc4py', '--upgrade', '--user'])
			subprocess.call(['pip3', 'install', 'mshr', '--upgrade', '--user'])
			subprocess.call(['pip3', 'install', 'sympy', '--upgrade', '--user'])
			subprocess.call(['pip3', 'install', 'fenics-ffc', '--upgrade', '--user'])
		try:
			import multiphenics
		except ImportError:
			subprocess.call(['git', 'clone', 'https://github.com/mathLab/multiphenics'])
			os.chdir('multiphenics')
			subprocess.call(['python3', 'setup.py', 'install', '--user'])
			os.chdir('..')
			subprocess.call(['rm', '-rf', 'multiphenics', '--user'])
		subprocess.call(['pip3', 'install', 'matplotlib', '--user'])
		subprocess.call(['pip3', 'install', 'numpy', '--user'])
		subprocess.call(['python3', 'setup.py', 'install', '--user'])
		subprocess.call(['rm', '-rf', 'build'])
		subprocess.call(['rm', '-rf', 'dist'])
		subprocess.call(['rm', '-rf', 'IOniCS.egg-info'])