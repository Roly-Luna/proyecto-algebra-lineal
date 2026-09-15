from typing import List, Optional, Literal
from pydantic import BaseModel, Field

# Clase restriccion
class ConstraintIn(BaseModel):
    # ... imdica que es un campo obligatorio
    a: float = Field(...,description="Coeficiente de X1") 
    b: float = Field(...,description="Coeficiente de X2")
    operator = Literal["<=",">=","="] # opciones
    c: float = Field(..., description="Lado derecho (recursos disponibles, demanda, etc.)")
    label: Optional[str] = Field(None, description="Nombre descriptivo, ej. 'Horas de mano de abora'")

# Clase Funcion Objetivo
class ObjectiveIn(BaseModel):
    a: float = Field(..., description="Coeficiente de x1 en la función objetivo")
    b: float = Field(..., description="Coeficiente de x2 en la función objetivo")
    mode: Literal["max", "min"] # opciones
    label: Optional[str] = Field("Z", description="Nombre de la función objetivo, ej. 'Ganancia'")

# Clase de Solicitod de Linear Program
#       Si non_negative es False, se quita esa 
#       condición automática; las restricciones 
#       ingresadas todavía podrían exigir valores no negativos.
class LPRquest(BaseModel):
    objective: ObjectiveIn
    constraints: List[ConstraintIn]
    non_negative: bool = True
    var_names: List[str] = ["x1","x2"]

# clase de un vértice y su evaluación
class VertexOut(BaseModel):
    x: float
    y: float
    z: float

# clase de puntos para dibujar una recta
class LineSegment(BaseModel):
    label: str
    x: List[float]
    y: List[float]

# clase del Resultado de linear Program

# optimal: se encontró óptimo,
# infeasible: no hay solución factible,
# unbounded: el objetivo puede mejorar sin límite

class LPResponse(BaseModel):
    status: Literal["optimal", "infeasible", "unbounded"]
    message: Optional[str] = None
    vertices: List[VertexOut] = []
    optimal_point: Optional[dict] = None
    optimal_value: Optional[float] = None
    constraint_lines: List[LineSegment] = []
    plot_range: float = 10.0