# Importar OR-Tools para programación lineal
from ortools.linear_solver import pywraplp
# Crear un solucionador usando el backend GLOP
solver = pywraplp.Solver('Maximize army power', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

#Variables (x,y,z)

x1 = solver.IntVar(0, solver.infinity(), 'espadachin')
x2 = solver.IntVar(0, solver.infinity(), 'arquero')
x3 = solver.IntVar(0, solver.infinity(), 'jinete')

#Restricciones

solver.Add(60*x1 + 80*x2 + 140*x3 <= 1200)
solver.Add(20*x1 + 10*x2 <= 800)
solver.Add(40*x2 + 100*x3 <= 600)

#Maximizar la función objetivo

solver.Maximize(70*x1 + 95*x2 + 230*x3)

#Resolver el sistema

status = solver.Solve()


