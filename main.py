# Importar OR-Tools para programación lineal
from ortools.linear_solver import pywraplp
# Crear un solucionador usando el backend GLOP
solver = pywraplp.Solver('Maximize army power', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

#Variables (x,y,z)

x = solver.IntVar(0, solver.infinity(), 'espadachin')
y = solver.IntVar(0, solver.infinity(), 'arquero')
z = solver.IntVar(0, solver.infinity(), 'jinete')

#Restricciones

solver.Add(60*x + 80*y + 140*z <= 1200)
solver.Add(20*x + 10*y <= 800)
solver.Add(40*y + 100*z <= 600)

#Maximizar la función objetivo

solver.Maximize(70*x + 95*y + 230*z)

#Resolver el sistema

status = solver.Solve()

#Imprimir la solución

if status == pywraplp.Solver.OPTIMAL:

    print('Solución:')
    print('Cantidad de espadachines =', x.solution_value())
    print('Cantidad de arqueros =', y.solution_value())
    print('Cantidad de jinetes =', z.solution_value())
    print('Fuerza óptima de la armada =', solver.Objective().Value())

else:
    
    print('El problema no tiene solución óptima.')