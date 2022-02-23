
import modiphy as md
import numpy as np

m = md.Model.from_lists(
    transition_variables=["a", "y", "c", "i", "k", "r", "c_to_y", "i_to_y"],
    parameters=["ss_a", "rho", "beta", "gamma", "delta"],
    transition_shocks=["shock_a"],
    transition_equations=[
        "c = beta*r*c{+1}",
        "k = (1 - delta)*k{-1} + i",
        "y = a^(1-gamma) * k{-1}^gamma",
        "gamma*y = k{-1} * (r - 1 + delta)",
        "y = i + c",
        "log(a) = rho*log(a{-1}) + (1 - rho)*log(ss_a) + shock_a",
        "c_to_y = c / y",
        "i_to_y = i / y",
    ],
)

m.assign({
    'a': 1,
    'y': 3.275862068965518,
    'c': 2.202734839476814,
    'i': 1.073127229488705,
    'k': 10.731272294887045,
    'r': 1.052631578947368,
    'c_to_y': 2.202734839476814/3.275862068965518,
    'i_to_y': 1.073127229488705/3.275862068965518,
    'beta': 0.95,
    'gamma': 0.50,
    'delta': 0.10,
    'rho': 0.8,
    'ss_a': 1,
})

steady = m.steady_evaluator


x = steady.init
x[1] = x[1] * 1.10
print(np.hstack((steady.init, x)))
print() 

print(np.hstack((steady.eval(), steady.eval(x))))

print(steady.incidence_matrix)

print(steady.quantities_solved)
print(steady.equations_solved)


