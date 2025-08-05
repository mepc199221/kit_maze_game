# Miguel Perez - El Reino Frutal 🍊🥭

### 💼 KIT DE DESARROLLO DE JUEGOS

<br/>

## ⚡️ Tutorial: Crear un Juego de Laberinto Multi-Nivel en Python ⚡️

Este tutorial está diseñado para principiantes y desarrolladores intermedios que quieran aprender a programar un juego completo basado en una cuadrícula (tile-based game) usando Python. El juego incluye múltiples niveles, sistema de audio, menús interactivos y mecánicas de juego avanzadas.

En este juego, un jugador se mueve por diferentes mapas para recoger frutas específicas mientras evita obstáculos peligrosos. Utilizamos las bibliotecas `keyboard` para capturar las teclas, `pygame` para el audio y la consola para mostrar el juego.

### 📋 Requisitos Previos

- Conocimientos básicos de Python (variables, bucles, funciones, diccionarios)
- Python 3.7+ instalado en tu sistema
- Bibliotecas requeridas:
  - `keyboard` (pip install keyboard)
  - `pygame` (pip install pygame)

> **Nota:** La biblioteca `keyboard` puede requerir permisos de administrador en algunos sistemas.

<br/>

## 🎵 Sistema de Audio

El juego incluye un sistema completo de audio usando Pygame Mixer:

```python
import pygame
pygame.mixer.init()

MUSIC = {
    "main_menu": "intro_music.ogg",
    "game_over": "lose_music.ogg", 
    "victory": "win_music.ogg",
    "level_1": "level_1_theme.ogg",
    "level_2": "level_2_theme.ogg",
    "level_3": "level_3_theme.ogg",
}
```

### Funciones de Audio:
- **`play_music(music_name)`**: Reproduce música de fondo en bucle
- **`stop_music()`**: Detiene la música actual

<br/>

## 🗺️ Sistema de Mapas Multi-Nivel

El juego utiliza un diccionario `MAPS` que define múltiples niveles con diferentes configuraciones:

### Elementos del Mapa:
1. **"."** → Espacios vacíos (⬜)
2. **"#"** → Paredes (🧱) 
3. **"f"** → Cerezas (🍒)
4. **"@"** → Jugador (😃/😥/🥲/🥵)
5. **"e"** → Manzanas (🍎)
6. **"c"** → Naranjas (🍊)
7. **"p"** → Piñas (🍍)
8. **"b"** → Bombas (💣)
9. **"t"** → Árboles (🌳)

### Estructura de Niveles:

```python
MAPS = {
    1: {
        "map": [...],           # Matriz del mapa
        "size_rows": 6,         # Filas del mapa
        "size_cols": 6,         # Columnas del mapa
        "start_avatar_y": 2,    # Posición inicial Y
        "start_avatar_x": 1,    # Posición inicial X
        "required_fruits": {"f": 3, "e": 3, "c": 3, "p": 3},  # Frutas requeridas
        "limit": 20,            # Límite de movimientos
        "music": "level_1_theme.ogg"  # Música del nivel
    }
}
```

<br/>

## 🎮 Sistema de Menús

### Menú Principal
El juego incluye un menú principal estilizado con opciones:
- **[S]** - Iniciar juego
- **[Q]** - Salir del juego

### Pantallas Especiales
- **Pantalla de Inicio de Nivel**: Se muestra al comenzar cada nivel
- **Pantalla de Victoria**: Arte ASCII cuando completas todos los niveles
- **Pantalla de Game Over**: Se muestra cuando pierdes

<br/>

## 🎯 Mecánicas de Juego Avanzadas

### Sistema de Emociones del Avatar
El avatar cambia de expresión según el progreso:
- **😃** → Estado normal
- **😥** → Al llegar a la mitad del límite de movimientos
- **🥲** → Cerca del límite de movimientos
- **🥵** → Al recoger una fruta

### Condiciones de Victoria y Derrota
- **Victoria**: Recolectar todas las frutas requeridas en cada nivel
- **Derrota**: Exceder el límite de movimientos o pisar una bomba (💣)

### Sistema de Progresión
- 3 niveles con dificultad creciente
- Mapas más grandes y complejos
- Mayor cantidad de frutas requeridas
- Límites de movimientos más generosos

<br/>

## 🔧 Funciones Principales

### `initialize_level()`
Inicializa todas las variables para el nivel actual:
- Carga el mapa correspondiente
- Establece posición inicial del jugador
- Resetea contadores de frutas
- Reproduce música del nivel

### `fn_render_map()`
Renderiza el mapa y las estadísticas:
- Convierte símbolos en emojis
- Muestra información del nivel actual
- Muestra progreso de recolección de frutas
- Actualiza expresión del avatar

### `fn_move_avatar()`
Maneja toda la lógica de movimiento:
- Captura eventos de teclado
- Valida movimientos legales
- Procesa interacciones con elementos del mapa
- Verifica condiciones de victoria/derrota

### `check_level_complete()`
Verifica si se han recolectado todas las frutas requeridas para completar el nivel.

<br/>

## 🎮 Controles del Juego

### En el Menú:
- **S** → Iniciar juego
- **Q** → Salir

### Durante el Juego:
- **W** → Mover arriba
- **A** → Mover izquierda  
- **S** → Mover abajo
- **D** → Mover derecha
- **Q** → Volver al menú principal

### En Pantallas de Final:
- **R** → Volver al menú principal
- **Q** → Salir del juego

<br/>

## 📁 Estructura de Archivos

```
proyecto/
├── main.py                 # Archivo principal del juego
└── assets/
    └── music/
        ├── intro_music.ogg
        ├── level_1_theme.ogg
        ├── level_2_theme.ogg
        ├── level_3_theme.ogg
        ├── win_music.ogg
        └── lose_music.ogg
```

<br/>

## 🎯 Cómo Jugar

1. **Ejecuta el script** en un entorno Python con las bibliotecas instaladas
2. **Navega por el menú** usando las teclas indicadas
3. **Mueve tu avatar** (😃) usando W, A, S, D
4. **Recolecta todas las frutas** requeridas en cada nivel:
   - 🍒 Cerezas
   - 🍎 Manzanas  
   - 🍊 Naranjas
   - 🍍 Piñas
5. **Evita obstáculos**:
   - 🧱 Paredes (bloquean el paso)
   - 🌳 Árboles (bloquean el paso)
   - 💣 Bombas (terminan el juego)
6. **Gestiona tus movimientos** - cada nivel tiene un límite
7. **Completa los 3 niveles** para ganar el juego

<br/>

## 📊 Información de Niveles

| Nivel | Tamaño | Límite Movimientos | Frutas Requeridas | Dificultad |
|-------|--------|-------------------|-------------------|------------|
| 1     | 6x6    | 20                | 3 de cada tipo    | Fácil      |
| 2     | 8x8    | 30                | 4 de cada tipo    | Medio      |
| 3     | 10x10  | 40                | 5 de cada tipo    | Difícil    |

<br/>

## 💡 Características Técnicas

### Gestión de Estados
- Sistema de variables globales para el estado del juego
- Manejo de transiciones entre niveles
- Control de flujo del menú principal

### Optimizaciones
- Carga dinámica de assets de audio
- Validación de archivos antes de cargar
- Manejo de errores para archivos faltantes

### Interfaz de Usuario
- Limpieza automática de consola
- Renderizado en tiempo real
- Feedback visual del progreso

<br/>

## 📜 Código Completo

```python
import os
import keyboard
import pygame
import time

# --- Inicializar Pygame Mixer ---
pygame.mixer.init()

# --- Definición de Mapas ---
MAPS = {
    1: {
        "map": [
            [".", ".", "#", ".", ".", "p"],
            ["#", ".", ".", "#", "f", "p"],
            ["b", ".", ".", ".", "t", "p"],
            [".", "e", "#", ".", "#", "c"],
            ["#", "e", "f", ".", "f", "c"],
            ["#", "e", ".", ".", ".", "c"],
        ],
        "size_rows": 6,
        "size_cols": 6,
        "start_avatar_y": 2,
        "start_avatar_x": 1,
        "required_fruits": {"f": 3, "e": 3, "c": 3, "p": 3},
        "limit": 20,
        "music": "level_1_theme.ogg"
    },
    2: {
        "map": [
            ["f", "f", "#", ".", ".", ".", ".", "."],
            ["#", "f", "f", "#", ".", ".", ".", "."],
            ["b", ".", "f", ".", "t", ".", "#", "."],
            [".", "e", "#", ".", "#", ".", ".", "."],
            ["#", "e", "e", ".", ".", ".", ".", "."],
            ["#", "e", "c", "c", ".", ".", "#", "."],
            ["p", "p", "c", "c", ".", ".", ".", "."],
            ["p", "p", ".", ".", "#", "t", ".", "."],
        ],
        "size_rows": 8,
        "size_cols": 8,
        "start_avatar_y": 0,
        "start_avatar_x": 0,
        "required_fruits": {"f": 4, "e": 4, "c": 4, "p": 4},
        "limit": 30,
        "music": "level_2_theme.ogg"
    },
    3: {
        "map": [
            [".", ".", "#", ".", ".", ".", ".", ".", ".", "."],
            ["#", ".", ".", "#", ".", ".", ".", ".", ".", "."],
            ["b", ".", ".", ".", "t", ".", "#", ".", ".", "."],
            [".", "e", "e", "e", "#", ".", ".", ".", ".", "."],
            ["#", "#", "f", "f", "#", ".", ".", ".", ".", "."],
            ["#", "e", ".", ".", "#", ".", "#", ".", ".", "."],
            ["p", "p", "f", "f", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "c", "#", "t", ".", ".", ".", "."],
            [".", "t", ".", "c", "e", "c", ".", ".", ".", "."],
            ["f", ".", ".", "c", "#", "c", ".", "#", "t", "."],
        ],
        "size_rows": 10,
        "size_cols": 10,
        "start_avatar_y": 4,
        "start_avatar_x": 4,
        "required_fruits": {"f": 5, "e": 5, "c": 5, "p": 5},
        "limit": 40,
        "music": "level_3_theme.ogg"
    }
}

# --- Variables Globales y de Audio ---
current_level = 1
game_over = False
game_running = False
current_map = []
size_rows = 0
size_cols = 0
avatar_y = 0
avatar_x = 0
counting_fruits = {}
move_limit = 0
level_limit = 0
avatar_icon = "😃"  # Icono por defecto del avatar

LEVEL_START_WAIT_TIME = 3

MUSIC = {
    "main_menu": "intro_music.ogg",
    "game_over": "lose_music.ogg",
    "victory": "win_music.ogg",
    "level_1": "level_1_theme.ogg",
    "level_2": "level_2_theme.ogg",
    "level_3": "level_3_theme.ogg",
}

# --- Obtener la ruta base del script para cargar assets ---
script_dir = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(script_dir, "assets")

def play_music(music_name):
    """Carga y reproduce la música de fondo."""
    music_file = MUSIC.get(music_name)
    if not music_file:
        print(f"Advertencia: No se encontró la música '{music_name}' en la lista.")
        return
    
    music_file_path = os.path.join(ASSETS_DIR, "music", music_file)
    if os.path.exists(music_file_path):
        try:
            pygame.mixer.music.load(music_file_path)
            pygame.mixer.music.play(-1)  # -1 para reproducción en bucle
        except pygame.error as e:
            print(f"Error al cargar/reproducir música '{music_file_path}': {e}")
    else:
        print(f"Advertencia: No se encontró el archivo de música '{music_file_path}'")

def stop_music():
    """Detiene la música si está sonando."""
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()

def initialize_level():
    """Inicializa las variables del juego para el nivel actual."""
    global current_map, size_rows, size_cols, avatar_y, avatar_x, counting_fruits, move_limit, level_limit, game_over, avatar_icon
    
    if current_level > len(MAPS):
        game_over = True
        return
    
    level_data = MAPS[current_level]
    current_map = [row[:] for row in level_data["map"]]
    size_rows = level_data["size_rows"]
    size_cols = level_data["size_cols"]
    avatar_y = level_data["start_avatar_y"]
    avatar_x = level_data["start_avatar_x"]
    counting_fruits = {fruit_type: 0 for fruit_type in level_data["required_fruits"].keys()}
    move_limit = 0
    level_limit = level_data["limit"]
    game_over = False
    avatar_icon = "😃"
    
    current_map[avatar_y][avatar_x] = "@"
    
    stop_music()
    play_music(f"level_{current_level}")

def fn_clear_map():
    """Limpia la consola."""
    os.system("cls" if os.name == "nt" else "clear")

def fn_render_map():
    """Renderiza el mapa y la estadística en la consola."""
    global avatar_icon, move_limit, level_limit
    
    if move_limit >= level_limit / 2 and avatar_icon == "😃":
        avatar_icon = "😥"
    if move_limit >= level_limit - 2 and avatar_icon == "😥":
        avatar_icon = "🥲"
    
    fn_clear_map()
    for rows in current_map:
        tiles = []
        for cols in rows:
            if cols == ".":
                tiles.append("⬜")
            elif cols == "#":
                tiles.append("🧱")
            elif cols == "t":
                tiles.append("🌳")
            elif cols == "@":
                tiles.append(avatar_icon)
            elif cols == "f":
                tiles.append("🍒")
            elif cols == "e":
                tiles.append("🍎")
            elif cols == "c":
                tiles.append("🍊")
            elif cols == "p":
                tiles.append("🍍")
            elif cols == "b":
                tiles.append("💣")
        print(" ".join(tiles))
    
    print("---")
    print(f"🌏 Nivel: {current_level}")
    print(f"👣 Movimientos: {move_limit}/{level_limit}")
    print("--- Frutas recolectadas ---")
    
    if current_level <= len(MAPS):
        for fruit_type, count in counting_fruits.items():
            fruit_icon = ""
            fruit_name = ""
            if fruit_type == "f": 
                fruit_name = "Cerezas"
                fruit_icon = "🍒"
            elif fruit_type == "e": 
                fruit_name = "Manzanas"
                fruit_icon = "🍎"
            elif fruit_type == "c": 
                fruit_name = "Naranjas"
                fruit_icon = "🍊"
            elif fruit_type == "p": 
                fruit_name = "Piñas"
                fruit_icon = "🍍"
            
            required_fruits = MAPS.get(current_level, {}).get("required_fruits", {})
            total_fruits = required_fruits.get(fruit_type, 0)
            
            collected_icons = " ".join([fruit_icon] * count)
            empty_icons = " ".join(["_"] * (total_fruits - count))
            
            print(f"{fruit_name}: {collected_icons} {empty_icons} / {total_fruits}")
    else:
        print("¡Todos los niveles completados!")
    print("---")

def check_level_complete():
    """Verifica si todas las frutas requeridas han sido recolectadas."""
    if current_level > len(MAPS):
        return True
    
    required = MAPS[current_level]["required_fruits"]
    for fruit_type, count_needed in required.items():
        if counting_fruits.get(fruit_type, 0) < count_needed:
            return False
    return True

def fn_move_avatar():
    """Maneja el movimiento del avatar y la interacción con el mapa."""
    global avatar_x, avatar_y, counting_fruits, move_limit, game_over, current_level, game_running, avatar_icon
    
    while not game_over and game_running:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            new_x = avatar_x
            new_y = avatar_y
            
            if event.name in ["w", "s", "a", "d"]:
                move_limit += 1
                if event.name == "w":
                    new_y -= 1
                elif event.name == "s":
                    new_y += 1
                elif event.name == "a":
                    new_x -= 1
                elif event.name == "d":
                    new_x += 1
            elif event.name == "q":
                print("Juego terminado. Volviendo al menú...")
                game_running = False
                stop_music()
                break
            
            if move_limit > level_limit:
                print("¡Has excedido el límite de movimientos!")
                game_over = True
                game_running = False
                stop_music()
                play_music("game_over")
                display_game_over_screen()
                break
            
            if (0 <= new_x < size_cols and 0 <= new_y < size_rows and
                current_map[new_y][new_x] != "#" and current_map[new_y][new_x] != "t"):
                
                tile_content = current_map[new_y][new_x]
                current_map[avatar_y][avatar_x] = "."
                
                avatar_x = new_x
                avatar_y = new_y
                
                if tile_content in ["f", "e", "c", "p"]:
                    counting_fruits[tile_content] = counting_fruits.get(tile_content, 0) + 1
                    avatar_icon = "🥵"
                elif tile_content == "b":
                    print("¡Has pisado una bomba!")
                    game_over = True
                    game_running = False
                    stop_music()
                    play_music("game_over")
                    display_game_over_screen()
                    break
                else:
                    avatar_icon = "😃"
                
                current_map[avatar_y][avatar_x] = "@"
                
                if check_level_complete():
                    fn_render_map()
                    print(f"¡Nivel {current_level} completado! 🎉")
                    current_level += 1
                    
                    if current_level > len(MAPS):
                        game_over = True
                        game_running = False
                        stop_music()
                        play_music("victory")
                        display_winner_screen()
                        break
                    else:
                        print(f"Cargando Nivel {current_level}...")
                        display_level_start_screen(current_level)
                        time.sleep(LEVEL_START_WAIT_TIME)
                        initialize_level()
                        fn_render_map()
                        continue
            
            fn_render_map()

def display_level_start_screen(level):
    """Muestra la pantalla de inicio de nivel."""
    fn_clear_map()
    print("*************************************")
    print(f"      BIENVENIDO A TU NUEVO NIVEL {level}!      ")
    print("           ¡Buena suerte! 🍀          ")
    print("*************************************")

def display_winner_screen():
    """Muestra la pantalla de victoria del juego."""
    fn_clear_map()
    winner_lines = [
        "**********************************",
        "        ¡JUEGO COMPLETADO!        ",
        "                                  ",
        "              \\O/                 ",
        "               |                  ",
        "              / \\                 ",
        "      _________|_|_______          ",
        "     /                \\           ",
        "     | V I C T O R Y ! |           ",
        "     |       1         |           ",
        "     \\________________/            ",
        "      \\______________/             ",
        "       \\____________/              ",
        "        \\__________/               ",
        "         \\________/                ",
        "         /________\\                ",
        "        /__________\\               ",
        "       /____________\\              ",
        "",
        "¡Felicitaciones! Has completado todos los niveles. 🏆✨",
        "",
        "Presiona R para volver al menú principal",
        "Presiona Q para salir del juego"
    ]
    for line in winner_lines:
        print(line)

def display_game_over_screen():
    """Muestra la pantalla de Game Over con arte ASCII."""
    fn_clear_map()
    
    game_over_lines = [
        "*************************************",
        "        ¡FIN DE LA PARTIDA!        ",
        "                                     ",
        "              _..._              ",
        "          .-'''''-.            ",
        "         /   .-.   .-. \\         ",
        "         |   |'|   |'| |         ",
        "         |   `|'   `|' |         ",
        "         \\      `-'   /          ",
        "          '._ `---' _.'          ",
        "              `''''`              ",
        "                                     ",
        "      ¡No te rindas! ¡Inténtalo de nuevo! 💔",
        "      Has caído en la aventura.",
        "",
        "Presiona R para volver al menú principal",
        "Presiona Q para salir del juego"
    ]
    
    for line in game_over_lines:
        print(line)

def main_menu():
    """Muestra el menú principal y espera la entrada del usuario."""
    global game_running, current_level, game_over
    
    stop_music()
    play_music("main_menu")
    
    menu_lines = [
        "╔═══════════════════════════════════╗",
        "║  🍊 ¡El Reino Frutal Te Llama! 🥭 ║",
        "╚═══════════════════════════════════╝",
        "",
        "  💥 Inicia la Gran Aventura       [S]",
        "  💨 Desiste y Abandona el Camino  [Q]",
        "",
        "------------------------------------",
        "      © 2025 Miguel Pérez",
        "   Todos los derechos reservados.",
    ]
    
    fn_clear_map()
    for line in menu_lines:
        print(line)
    
    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "s":
                print("\nIniciando juego...")
                current_level = 1
                game_over = False
                game_running = True
                return True
            elif event.name == "q":
                print("\nSaliendo del juego. ¡Hasta pronto!")
                game_running = False
                return False

if __name__ == "__main__":
    while True:
        if main_menu():
            while game_running:
                display_level_start_screen(current_level)
                time.sleep(LEVEL_START_WAIT_TIME)
                
                initialize_level()
                if not game_over:
                    fn_render_map()
                    fn_move_avatar()
                
                if not game_running and (current_level > len(MAPS) or not game_over):
                    pass
                elif not game_running and game_over:
                    pass
                    
                while not game_running:
                    event = keyboard.read_event(suppress=True)
                    if event.event_type == keyboard.KEY_DOWN:
                        if event.name == "r":
                            print("Volviendo al menú...")
                            break
                        elif event.name == "q":
                            print("Saliendo del juego. ¡Hasta pronto!")
                            exit()
        else:
            exit()
```

<br/>

---

<h3 align="center">🎮 EL REINO FRUTAL - AVENTURA MULTI-NIVEL 🎮</h3>
<h3 align="center">Desarrollado por: Miguel Pérez</h3>
<h3 align="center">© 2025 - Todos los derechos reservados</h3>
