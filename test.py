
from modiphy import Model

m = Model.from_lists(
    transition_variables=["a", "y", "c", "i", "k", "r"],
    parameters=["ss_a", "rho", "beta", "gamma", "delta"],
    transition_shocks=["shock_a"],
    transition_equations=[
        "c = beta*r*c{+1}",
        "k = (1 - delta)*k{-1} + i",
        "y = a^(1-gamma) * k{-1}^gamma",
        "gamma*y = k{-1} * (r - 1 + delta)",
        "y = i + c",
        "log(a) = rho*log(a{-1}) + (1 - rho)*log(ss_a) + shock_a",
    ],
)


m.assign({
    'a': 1,
    'y': 1,
    'c': 1,
    'i': 1,
    'k': 1,
    'r': 1,
    'beta': 0.95,
    'gamma': 0.50,
    'delta': 0.10,
    'rho': 0.8,
    'ss_a': 1,
})


x = m.create_steady_vector()
f, f_string = m.steady_evaluator

