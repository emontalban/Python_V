# Python
## 1.Condicionales
Un condicional es una estructura de control que permite que el programa tome decisiones en funcion si  una o varias condiciones se cumplen( es decir, si no True o False).En Python, estos bloque de codigo deben ir siempre indentados(con sangria), ya que python usa la indentacion para saber cuando empieza y termina un bloque, puedes usar 2 o 4 espacions, pero tiene que ser consistente en  todo el codigo, si eliges 2 todo el codigo a 2 y si eliges 4 pues todo a 4. Ademas, cada condicion debe de llevar dos puntos (:) al final de la linea.

### &#8226; IF

La forma mas basica de un condicional es el if, que ejecuta un bloque de codigo solo cuando la condicion que evalua es verdadera (True). 
Su sintaxis es: 
```
if condicion:
    accion
```
Si la condicion se cumple (devuelve True) la accion se ejecuta si por el contrario devuelve (false) la accion no se ejecuta.

Ejemplo
```
lenguaje = "Python"

if lenguaje == "Python":
    print("Estás aprendiendo un lenguaje muy versátil")
```

### &#8226; ELIF
Permite evaluar multiples  condiciones sin repetir if. Es una mezcla de else e if y se utiliza par comprobar condiciones cuando la condicion if no se cumple. Las condiciones se evualuan en orden, de arriba a abajo, y en cuanto una es verdadera(True), se ejecuta el bloque de codigo y se deja de evaluar el resto. 

Su sintaxis es:
```
if condicion1:
    accion1
elif condicion2:
    accion2
```
Ejemplo:

```
lenguaje = "JavaScript"

if lenguaje == "Python":
    print("Backend, IA, automatización")
elif lenguaje == "JavaScript":
    print("Frontend y web")
```
El codigo se evalua de arriba abajo y en cuanto encuentra una condicion verdadera ejecuta el bloque y deja de evaluar el resto en esta caso la concidion verdadera la encuentra en elif asi que ejecuta ese codigo.

### &#8226; ELSE
Se ejecuta cuando ninguna condicion anterior es verdadera. Siempre debe de ir acompañado de un if, y opcionalmente puede haber elif. Se utiliza como caso por defecto, es decir, para ejecutar un bloque de codigo  cuando no se cumplen ninguna de las anteriores. A diferencia de if y elif, else no lleva condicion.

Su sintaxis es:
```
# sintaxis basica
if condicion:
    accion
else:
    accion_alternativa

# sintaxis con elif
if condicion:
    accion
elif condicion:
    accion
else:
    accion_alternativa

```
Ejemplo
```
lenguaje = "C++"

if lenguaje == "Python":
    print("Muy usado en IA")
elif lenguaje == "JavaScript":
    print("Muy usado en web")
else:
    print("Lenguaje no reconocido en esta lista")
```
En este caso como no se cumplen ninguna de las condiciones se ejecuta el codigo de else.
