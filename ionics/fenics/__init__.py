from dolfin import cells, facets, vertices, dof_to_vertex_map, FunctionSpace, Function
import numpy


def assign_scalar_to_cells(f, f_values, tag, subdomains):
	vec = f.vector()
	values = vec.get_local()
	for cell in cells(subdomains.mesh()):
		subdomain = subdomains.array()[cell.index()]
		if subdomain == tag:
			values[cell.index()] = f_values
	f.vector().set_local(values)
	f.vector().apply('insert')
	return f
	

def assign_scalar_to_facets(f, f_values, tag, boundaries):
	vec = f.vector()
	values = vec.get_local()
	for cell in cells(boundaries.mesh()):
		for facet in facets(cell):
			boundary = boundaries.array()[facet.index()]
			if boundary == tag:
				values[cell.index()] = f_values
	f.vector().set_local(values)
	f.vector().apply('insert')
	return f


def assign_tensor_to_cells(t, t_values, tag, subdomains, dim):
	vec = t.vector()
	values = vec.get_local()
	for cell in cells(subdomains.mesh()):
		subdomain = subdomains.array()[cell.index()]
		if subdomain == tag:
			j = 0
			for i in range(cell.index()*numpy.power(dim, 2), cell.index()*numpy.power(dim, 2) + numpy.power(dim, 2)):
				values[i] = t_values[j]
				j += 1
	t.vector().set_local(values)
	t.vector().apply('insert')
	return t


def assign_tensor_to_facets(t, t_values, tag, boundaries, dim):
	vec = t.vector()
	values = vec.get_local()
	for facet in facets(boundaries.mesh()):
		boundary = boundaries.array()[facet.index()]
		if boundary == tag:
			j = 0
			for i in range(facet.index()*numpy.power(dim, 2), facet.index()*numpy.power(dim, 2) + numpy.power(dim, 2)):
				values[i] = t_values[j]
				j += 1
	t.vector().set_local(values)
	t.vector().apply('insert')
	return t


def interpolate_function_to_mesh(u, mesh, space='CG', degree=1, pointwise=True):
	V = FunctionSpace(mesh, space, degree)
	v = Function(V)
	data_vector = v.vector().get_local()
	if pointwise:
		for vertex in vertices(mesh):
			data_vector[vertex.index()] = u(vertex.point())
	else:
		for cell in cells(mesh):
			data_vector[cell.index()] = u(cell.midpoint())
	v.vector().set_local(data_vector)
	v.vector().apply('insert')
	return v