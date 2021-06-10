from dolfin import Mesh, XDMFFile, MeshValueCollection, MeshFunction, Function
from matplotlib import pyplot
from mpi4py import MPI


def read_mesh(file):
	msh = Mesh(MPI.COMM_WORLD)
	with XDMFFile('{}.xdmf'.format(file)) as infile:
		infile.read(msh)
	return msh


def read_boundaries(msh, file, name_to_read='boundaries'):
	dim = msh.topology().dim()
	mvc = MeshValueCollection('size_t', msh, dim=dim-1)
	with XDMFFile('{}.xdmf'.format(file)) as infile:
		infile.read(mvc, name_to_read)
	boundaries = MeshFunction('size_t', msh, mvc)
	return boundaries


def read_subdomains(msh, file, name_to_read='subdomains'):
	dim = msh.topology().dim()
	mvc = MeshValueCollection('size_t', msh, dim=dim)
	with XDMFFile('{}.xdmf'.format(file)) as infile:
		infile.read(mvc, name_to_read)
	subdomains = MeshFunction('size_t', msh, mvc)
	return subdomains


def read_function(V, filename, name_to_read):
	v = Function(V)
	with XDMFFile('{}.xdmf'.format(filename)) as infile:
		infile.read_checkpoint(v, name_to_read)
	return v


class XDMFWriter(object):
	def __init__(self, file):
		self.outputFile = XDMFFile("{}.xdmf".format(file))
		self.outputFile.parameters["rewrite_function_mesh"] = False
		self.outputFile.parameters["functions_share_mesh"] = True

	def write(self, solution, time=0.0):
		if isinstance(solution, list):
			for s in solution:
				self.outputFile.write(s, time)
		else:
			self.outputFile.write(solution, time)

	def close(self):
		self.outputFile.close()


def save_matrix(A, figname):
	A.mat().convert('dense')
	_ , ax = pyplot.subplots(nrows=1, ncols=1, figsize=(10,8))
	ax.spy(A.mat().getDenseArray(), markersize=5)
	pyplot.tight_layout()
	pyplot.savefig(figname)