import argparse
import produce_results

parser = argparse.ArgumentParser(
    description='Run a the simulations',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

params = parser.add_argument_group('simulation parameters')
params.add_argument('-Nx',
    type=float,
    default=1.0,
    help='10^Nx is the number of integration points'
)
params.add_argument('-Nt',
    type=float,
    default=1.0,
    help='10^Nt is the number of time steps'
)
params.add_argument('-dt',
    type=float,
    default=0.0,
    help='10^(-dt) is the timestep'
)
params.add_argument('-m',
    type=str,
    choices=["ForwardEuler", "BackwardEuler", "CrankNicolson", "all"],
    default=1,
    help='The method you want to use.'
)

args = parser.parse_args()


if args.m == 'all':
    m_list = ['ForwardEuler', 'BackwardEuler', 'CrankNicolson']
    for method in m_list:
        params = produce_results.Parameters(
            args.Nx,
            args.Nt,
            args.dt,
            method
        )
        produce_results.run_simulation(params, params.create_filename())
        produce_results.plot_solution(params.create_filename(), method)
else:
    params = produce_results.Parameters(
        args.Nx,
        args.Nt,
        args.dt,
        args.m
    )
    produce_results.run_simulation(params, params.create_filename())
    produce_results.plot_solution(params.create_filename(), args.m)