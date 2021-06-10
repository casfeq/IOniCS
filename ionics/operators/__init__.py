from ufl import grad, inner, sym, tr


def gradt(u, n):
	return grad(u) - inner(grad(u), n)*n


def divt(u, n):
	return tr(sym(gradt(u, n)))


def grads(u):
	return sym(grad(u))