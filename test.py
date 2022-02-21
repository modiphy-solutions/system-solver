
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
    'y': 3.275862068965518,
    'c': 2.202734839476814,
    'i': 1.073127229488705,
    'k': 10.731272294887045,
    'r': 1.052631578947368,
    'beta': 0.95,
    'gamma': 0.50,
    'delta': 0.10,
    'rho': 0.8,
    'ss_a': 1,
})

x = m.create_steady_vector()
f, f_string = m.steady_evaluator

rhs_minus_lhs = f(x)
print(rhs_minus_lhs)

