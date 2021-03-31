import subprocess
import sys


if __name__ == "__main__":
	if "--remove" in sys.argv:
		subprocess.call(['rm', '-rf', '~/.local/lib/python3.8/site-packages/IOniCS*'])
	else:
		try:
			import dolfin
		except ImportError:
			subprocess.call(['pip3', 'install', 'mpi4py', '--upgrade'])
			subprocess.call(['pip3', 'install', 'petsc4py', '--upgrade'])
			subprocess.call(['pip3', 'install', 'slepc4py', '--upgrade'])
			subprocess.call(['pip3', 'install', 'mshr', '--upgrade'])
			subprocess.call(['pip3', 'install', 'sympy', '--upgrade'])
			subprocess.call(['sudo', 'apt-get', 'install', '-y', '-qq', 'software-properties-common'])
			subprocess.call(['sudo', 'add-apt-repository', '-y', 'ppa:fenics-packages/fenics'])
			subprocess.call(['sudo', 'apt-get', 'update'])
			subprocess.call(['sudo', 'apt', 'install', '-y', '--no-install-recommends', 'fenics'])
		try:
			import multiphenics
		except ImportError:
			subprocess.call(['git', 'clone', 'https://github.com/mathLab/multiphenics'])
			subprocess.call(['cd', 'multiphenics'])
			subprocess.call(['python3', 'setup.py', 'install', '--user'])
			subprocess.call(['cd', '..'])
		subprocess.call(['pip3', 'install', 'matplotlib==3.1.2'])
		subprocess.call(['pip3', 'install', 'numpy==1.17.4'])
		subprocess.call(['python3', 'setup.py', 'install', '--user'])
		subprocess.call(['rm', '-rf', 'multiphenics'])
		subprocess.call(['rm', '-rf', 'build'])
		subprocess.call(['rm', '-rf', 'dist'])
		subprocess.call(['rm', '-rf', 'IOniCS.egg-info'])