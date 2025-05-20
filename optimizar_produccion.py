from pulp import LpProblem, LpVariable, LpMaximize, value

modelo = LpProblem("Maximizar_beneficio", LpMaximize)

A = LpVariable("Producto_A", lowBound=0, cat="Integer")
B = LpVariable("Producto_B", lowBound=0, cat="Integer")

modelo += 40 * A + 30 * B, "Beneficio_Total"
modelo += 2 * A + 1 * B <= 100, "Horas_maquina"
modelo += 1 * A + 2 * B <= 80, "Horas_operario"

modelo.solve()

print("Unidades óptimas:")
print(f"Producto A: {A.varValue}")
print(f"Producto B: {B.varValue}")
print(f"Beneficio total: {value(modelo.objective)} €")
