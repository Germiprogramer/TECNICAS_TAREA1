from archive import *

if __name__ == "__main__":
    if status == pywraplp.Solver.OPTIMAL:

        print('Solución:')
        print('Cantidad de espadachines =', x1.solution_value())
        print('Cantidad de arqueros =', x2.solution_value())
        print('Cantidad de jinetes =', x3.solution_value())
        print('Fuerza óptima de la armada =', solver.Objective().Value())

    else:
        
        print('El problema no tiene solución óptima.')