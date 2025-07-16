# Miguel Perez (modificado agregando las detalles de frutas y limites)
### 💼 KIT
<br/>

## ⚡️ Tutorial: Crear un Juego de Maze en Python ⚡️

Este tutorial está diseñado para principiantes que quieran aprender a programar un juego simple basado en una cuadrícula (tile-based game) usando Python.
En este juego, un jugador se mueve por un mapa para recoger frutas mientras evita paredes. Usaremos la biblioteca keyboard para capturar las teclas y la consola para mostrar el juego.
Requisitos previos

Conocimientos básicos de Python (variables, bucles, funciones). <br>
Python instalado en tu sistema. <br>
La biblioteca keyboard instalada (pip install keyboard). <br>


Nota: La biblioteca keyboard puede requerir permisos de administrador en algunos sistemas.

## Paso 1: Configurar el mapa del juego
El juego usa una lista bidimensional (map) para representar el mundo:

1. "." representa espacios vacíos (⬜).
2. "#" representa paredes (🧱).
3. "f" representa frutas (🍒).
4. "@" representa al jugador (😃).
5. "g" representa regalo (🎁).
6. "e" representa manzanda (🍎).
7. "c" representa naranja (🍊).
8. "p" representa piña (🍍).
9. "b" representa una bomba (💣).
10. "t" representa un arbol (🌳).
<br>

```
map = [
    [".",".","#",".",".","p"],
    ["#",".",".","#","f","p"],
    ["b",".",".",".","t","p"],
    [".","e","#",".","#","c"],
    ["#","e","f",".","f","c"],
    ["#","e",".",".",".","c"],
]
```

Definimos variables para el tamaño del mapa y la posición inicial del jugador:
```
size_rows = 5
size_cols = 5
avatar_y = 2
avatar_x = 1
counting_fruits = 0
counting_apple = 0
counting_orange = 0
counting_pineapple = 0
limit = 0
```

1. size_rows y size_cols establecen los límites del mapa.
2. avatar_x y avatar_y indican la posición del jugador.
3. counting_fruits lleva la cuenta de las frutas recogidas.<br>

## Paso 2: Limpiar la pantalla
La función fn_clear_map limpia la consola para una nueva visualización:<br>
1. Usa os.system para ejecutar cls (Windows) o clear (sistemas basados en Unix).
```
def fn_clear_map():
    os.system("cls" if os.name == "nt" else "clear")
```

## Paso 3: Mostrar el mapa
1. Recorre el mapa y convierte los símbolos en emojis.
2. Muestra la cantidad de frutas recogidas al final.
3. La función fn_render_map muestra el mapa del juego:
```
def fn_render_map():
    fn_clear_map()
    for rows in map:
        tiles = []
        for cols in rows:
            if cols == ".":
               tiles.append("⬜")
            if cols == "#":
               tiles.append("🧱")
            if cols == "t":
               tiles.append("🌳")
            if cols == "@":
               tiles.append("😃")
            if cols == "f":
               tiles.append("🍒")
            if cols == "g":
               tiles.append("🎁")
            if cols == "e":
               tiles.append("🍎")
            if cols == "c":
                tiles.append("🍊")
            if cols == "p":
                tiles.append("🍍")
            if cols == "b":
                tiles.append("💣")
           print(" ".join(tiles))
    print(f"Frutas cerezas: {counting_fruits}")
    print(f"Frutas manzanas: {counting_apple}")
    print(f"Frutas naranja: {counting_orange}")
    print(f"Frutas piña: {counting_pineapple}")
    print(f"Limite de intentos: {limit}/20")
```


## Paso 4: Mover al jugador
La función fn_move_avatar gestiona el movimiento del jugador y la lógica del juego: 
1. Usa keyboard.read_event para detectar teclas (w, s, a, d para moverse; q para salir).
2. Actualiza new_x y new_y según la tecla presionada.<br>
3. ingrementa el limite por cada movimiento.
```
def fn_move_avatar():
    global avatar_x, avatar_y, counting_fruits, counting_apple, counting_orange, counting_pineapple, limit
    new_x = avatar_x
    new_y = avatar_y

    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "w":
               new_y -= 1
               limit += 1
            elif event.name == "s":
               new_y += 1
               limit += 1
            elif event.name == "a":
               new_x -= 1
               limit += 1
            elif event.name == "d":
               new_x += 1
               limit += 1
            elif event.name == "q":
               print("Juego terminado")
               break
            if limit == 20:
                print("Has alcanzado el límite de intentos. Juego terminado. 😵")
                break
```

## Paso 5: Colisiones y recolección de frutas
La función también verifica movimientos válidos y recoge frutas:
1. Verifica si la nueva posición está dentro de los límites y no es una pared (#).
2. Actualiza el mapa moviendo al jugador (@) y limpiando la posición anterior (.).
3. Incrementa counting_fruits al recoger una fruta (f).
4. Termina el juego cuando se recogen 3 frutas.

```
if (new_x >= 0 and new_x <= size_rows and new_y >= 0 and new_y <= size_cols and map[new_y][new_x] != "#" and map[new_y][new_x] != "t"):
                map[avatar_y][avatar_x] = "."
                avatar_x = new_x
                avatar_y = new_y
                if map[avatar_y][avatar_x] == "f":
                    counting_fruits += 1

                if map[avatar_y][avatar_x] == "e":
                    counting_apple += 1
                
                if map[avatar_y][avatar_x] == "c":
                    counting_orange += 1

                if map[avatar_y][avatar_x] == "p":
                    counting_pineapple += 1

                if map[avatar_y][avatar_x] == "b":
                    print("¡Has pisado una bomba! Juego terminado. 💣💥💥")
                    break

                if counting_fruits == 3 and counting_apple == 3 and counting_orange == 3 and counting_pineapple == 3:
                    print("¡Has ganado! 🎉")
                    break
                
                map[avatar_y][avatar_x] = "@"
            else:
                new_x = avatar_x
                new_y = avatar_y
            fn_render_map()
```


## Paso 6: Ejecutar el juego
El bloque principal inicia el juego:
1. Llama a fn_render_map para mostrar el mapa inicial.
2. Llama a fn_move_avatar para iniciar el bucle del juego.
```
if __name__ == "__main__":
    fn_render_map()
    fn_move_avatar()
```

## Cómo jugar  💻🎮🕹️
Ejecuta el script en un entorno Python con keyboard instalado.
1. Usa W, A, S, D para mover al jugador (😃).
2. Recoge todas las frutas (🍒,🍎,🍊,🍍) para ganar (3 frutas en este mapa).
3. Evita las paredes (🧱).
4. Evita los arboles (🌳).
5. Evita las bombas (💣).
6. Tiene un limite de pasos 20
7. Presiona Q para salir.
<br>

## Código completo 📜
```
import os
import keyboard

map = [
    [".",".","#",".",".","p"],
    ["#",".",".","#","f","p"],
    ["b",".",".",".","t","p"],
    [".","e","#",".","#","c"],
    ["#","e","f",".","f","c"],
    ["#","e",".",".",".","c"],
]

size_rows = 5
size_cols = 5
avatar_y = 2
avatar_x = 1
counting_fruits = 0
counting_apple = 0
counting_orange = 0
counting_pineapple = 0
limit = 0

def fn_clear_map():
    os.system("cls" if os.name == "nt" else "clear")

def fn_render_map():
    fn_clear_map()
    for rows in map:
        tiles = []
        for cols in rows:
            if cols == ".":
               tiles.append("⬜")
            if cols == "#":
               tiles.append("🧱")
            if cols == "t":
               tiles.append("🌳")
            if cols == "@":
               tiles.append("😃")
            if cols == "f":
               tiles.append("🍒")
            if cols == "g":
               tiles.append("🎁")
            if cols == "e":
               tiles.append("🍎")
            if cols == "c":
                tiles.append("🍊")
            if cols == "p":
                tiles.append("🍍")
            if cols == "b":
                tiles.append("💣")
        print(" ".join(tiles))
    print(f"Frutas cerezas: {counting_fruits}")
    print(f"Frutas manzanas: {counting_apple}")
    print(f"Frutas naranja: {counting_orange}")
    print(f"Frutas piña: {counting_pineapple}")
    print(f"Limite de intentos: {limit}/20")

def fn_move_avatar():
    global avatar_x, avatar_y, counting_fruits, counting_apple, counting_orange, counting_pineapple, limit
    new_x = avatar_x
    new_y = avatar_y

    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "w":
               new_y -= 1
               limit += 1
            elif event.name == "s":
               new_y += 1
               limit += 1
            elif event.name == "a":
               new_x -= 1
               limit += 1
            elif event.name == "d":
               new_x += 1
               limit += 1
            elif event.name == "q":
               print("Juego terminado")
               break
            if limit > 20:
                print("Has alcanzado el límite de intentos. Juego terminado. 😵")
                break

            if (new_x >= 0 and new_x <= size_rows and new_y >= 0 and new_y <= size_cols and map[new_y][new_x] != "#" and map[new_y][new_x] != "t"):
                map[avatar_y][avatar_x] = "."
                avatar_x = new_x
                avatar_y = new_y
                if map[avatar_y][avatar_x] == "f":
                    counting_fruits += 1

                if map[avatar_y][avatar_x] == "e":
                    counting_apple += 1
                
                if map[avatar_y][avatar_x] == "c":
                    counting_orange += 1

                if map[avatar_y][avatar_x] == "p":
                    counting_pineapple += 1

                if map[avatar_y][avatar_x] == "b":
                    print("¡Has pisado una bomba! Juego terminado. 💣💥💥")
                    break

                if counting_fruits == 3 and counting_apple == 3 and counting_orange == 3 and counting_pineapple == 3:
                    print("¡Has ganado! 🎉")
                    break
                
                map[avatar_y][avatar_x] = "@"
            else:
                new_x = avatar_x
                new_y = avatar_y
            fn_render_map()

if __name__ == "__main__":
    fn_render_map()
    fn_move_avatar()
```
<br>

---
<h3 align="center">SOCIAL OPLESK</h3>
<h3 align="center">Modificado por: Miguel Perez</h3>
