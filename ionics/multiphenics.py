from dolfin import MeshFunction, facets, cells, entities
from multiphenics import MeshRestriction


def create_interface_restriction(subdomains, subdomain_ids):
	assert isinstance(subdomain_ids, set)
	assert len(subdomain_ids) == 2
	mesh = subdomains.mesh()
	dim = mesh.topology().dim()
	restriction = MeshRestriction(mesh, None)
	for d in range(dim + 1):
		mesh_function_d = MeshFunction("bool", mesh, d)
		mesh_function_d.set_all(False)
		restriction.append(mesh_function_d)
	for f in facets(mesh):
		subdomains_ids_f = set(subdomains[c] for c in cells(f))
		assert len(subdomains_ids_f) in (1, 2)
		if subdomains_ids_f == subdomain_ids:
			restriction[dim - 1][f] = True
			for d in range(dim - 1):
				for e in entities(f, d):
					restriction[d][e] = True
	return restriction


def create_boundaries_restriction(boundaries, boundary_id):
	mesh = boundaries.mesh()
	dim = mesh.topology().dim()
	restriction = MeshRestriction(mesh, None)
	for d in range(dim + 1):
		mesh_function_d = MeshFunction("bool", mesh, d)
		mesh_function_d.set_all(False)
		restriction.append(mesh_function_d)
	for f in facets(mesh):
		if boundaries[f] == boundary_id:
			restriction[dim - 1][f] = True
			for d in range(dim - 1):
				for e in entities(f, d):
					restriction[d][e] = True
	return restriction


def create_subdomains_restriction(subdomains, subdomain_id):
	mesh = subdomains.mesh()
	dim = mesh.topology().dim()
	restriction = MeshRestriction(mesh, None)
	for d in range(dim + 1):
		mesh_function_d = MeshFunction("bool", mesh, d)
		mesh_function_d.set_all(False)
		restriction.append(mesh_function_d)
	for c in cells(mesh):
		if subdomains[c] == subdomain_id:
			restriction[dim][c] = True
			for d in range(dim):
				for e in entities(c, d):
					restriction[d][e] = True
	return restriction