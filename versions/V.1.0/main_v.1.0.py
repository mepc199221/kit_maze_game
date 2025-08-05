import os
import keyboard
import pygame # Importa pygame para el manejo de audio

# --- Inicializar Pygame Mixer ---
# Es importante inicializar mixer antes de usarlo
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
        "music": "level_1_theme.ogg" # Nombre del archivo de música
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
            ["p", "p", "p", ".", "#", "t", ".", "."],
        ],
        "size_rows": 8,
        "size_cols": 8,
        "start_avatar_y": 0,
        "start_avatar_x": 0,
        "required_fruits": {"f": 4, "e": 4, "c": 4, "p": 4},
        "limit": 30,
        "music": "level_2_theme.ogg" # Nombre del archivo de música
    },
    3: {
        "map": [
            [".", ".", "#", ".", ".", ".", ".", ".", ".", "."],
            ["#", ".", ".", "#", ".", ".", ".", ".", ".", "."],
            ["b", ".", ".", ".", "t", ".", "#", ".", ".", "."],
            [".", "e", "e", "e", "#", ".", ".", ".", ".", "."],
            ["#", "e", "f", "f", "f", ".", ".", ".", ".", "."],
            ["#", "e", "f", "f", "f", ".", "#", ".", ".", "."],
            ["p", "p", "f", "f", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "c", "#", "t", ".", ".", ".", "."],
            [".", "t", "p", "c", "e", "c", ".", ".", ".", "."],
            ["f", "p", "p", "c", "c", "c", ".", "#", "t", "."],
        ],
        "size_rows": 10,
        "size_cols": 10,
        "start_avatar_y": 4,
        "start_avatar_x": 4,
        "required_fruits": {"f": 5, "e": 5, "c": 5, "p": 5},
        "limit": 40,
        "music": "level_3_theme.ogg" # Nombre del archivo de música
    }
}

# --- Variables Globales ---
current_level = 1
game_over = False
game_running = False # Controla si el juego está activo o en el menú

# Variables de juego (se inicializarán con cada nivel)
current_map = []
size_rows = 0
size_cols = 0
avatar_y = 0
avatar_x = 0
counting_fruits = {} # Usamos un diccionario para contar las frutas de cada tipo
move_limit = 0
level_limit = 0

# --- Obtener la ruta base del script para cargar assets ---
# Esto es crucial para que las rutas de los archivos de música sean correctas
script_dir = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(script_dir, "GameFruit/assets")

def play_music(level):
    """Carga y reproduce la música de fondo para el nivel dado."""
    if level in MAPS:
        music_filename = MAPS[level]["music"]
        music_file_path = os.path.join(ASSETS_DIR, music_filename)
        
        if os.path.exists(music_file_path):
            try:
                pygame.mixer.music.load(music_file_path)
                pygame.mixer.music.play(-1) # -1 para reproducción en bucle
                print(f"Reproduciendo: {music_file_path}") # Mensaje de depuración
            except pygame.error as e:
                print(f"Error al cargar/reproducir música '{music_file_path}': {e}")
        else:
            print(f"Advertencia: No se encontró el archivo de música '{music_file_path}'")
    else:
        # Detener la música si no hay un nivel válido (ej. al terminar el juego)
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

def initialize_level():
    """Inicializa las variables del juego para el nivel actual."""
    global current_map, size_rows, size_cols, avatar_y, avatar_x, counting_fruits, move_limit, level_limit, game_over

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
    game_over = False # Reinicia game_over para el nuevo nivel

    current_map[avatar_y][avatar_x] = "@"
    
    play_music(current_level)

def fn_clear_map():
    """Limpia la consola."""
    os.system("cls" if os.name == "nt" else "clear")

def fn_render_map():
    """Renderiza el mapa en la consola."""
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
                tiles.append("😃")
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
    print(f"Nivel: {current_level}")
    print(f"Movimientos: {move_limit}/{level_limit}")
    print("--- Frutas recolectadas ---")
    
    if current_level <= len(MAPS):
        for fruit_type, count in counting_fruits.items():
            fruit_name = ""
            if fruit_type == "f": fruit_name = "Cerezas"
            elif fruit_type == "e": fruit_name = "Manzanas"
            elif fruit_type == "c": fruit_name = "Naranjas"
            elif fruit_type == "p": fruit_name = "Piñas"
            print(f"{fruit_name}: {count}/{MAPS[current_level]['required_fruits'][fruit_type]}")
    else:
        print("¡Todos los niveles completados!")
    print("---")


def check_level_complete():
    """Verifica si todas las frutas requeridas PARA EL NIVEL ACTUAL han sido recolectadas."""
    
    if current_level > len(MAPS): 
        return True 

    required = MAPS[current_level]["required_fruits"]
    for fruit_type, count_needed in required.items():
        if counting_fruits.get(fruit_type, 0) < count_needed:
            return False 
    return True 

def fn_move_avatar():
    """Maneja el movimiento del avatar y la interacción con el mapa."""
    global avatar_x, avatar_y, counting_fruits, move_limit, game_over, current_level, game_running

    while not game_over and game_running: 
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            new_x = avatar_x
            new_y = avatar_y
            
            if event.name == "w":
                new_y -= 1
                move_limit += 1
            elif event.name == "s":
                new_y += 1
                move_limit += 1
            elif event.name == "a":
                new_x -= 1
                move_limit += 1
            elif event.name == "d":
                new_x += 1
                move_limit += 1
            elif event.name == "q":
                print("Juego terminado. 😢 Volviendo al menú...")
                game_over = True
                game_running = False 
                pygame.mixer.music.stop() 
                break
            
            if move_limit > level_limit:
                print("¡Has excedido el límite de movimientos! Juego terminado. 😵 Volviendo al menú...")
                game_over = True
                game_running = False 
                pygame.mixer.music.stop() 
                break

            if (0 <= new_x < size_cols and 0 <= new_y < size_rows and 
                current_map[new_y][new_x] != "#" and current_map[new_y][new_x] != "t"):
                
                current_map[avatar_y][avatar_x] = "." 
                
                tile_content = current_map[new_y][new_x]
                if tile_content in ["f", "e", "c", "p"]:
                    counting_fruits[tile_content] = counting_fruits.get(tile_content, 0) + 1
                elif tile_content == "b":
                    print("¡Has pisado una bomba! Juego terminado. 💣💥💥 Volviendo al menú...")
                    game_over = True
                    game_running = False 
                    pygame.mixer.music.stop() 
                    break

                avatar_x = new_x
                avatar_y = new_y
                current_map[avatar_y][avatar_x] = "@" 

                if check_level_complete():
                    print(f"¡Nivel {current_level} completado! 🎉")
                    current_level += 1 
                    
                    if current_level > len(MAPS):
                        print("\n¡Felicitaciones! Has completado todos los niveles y eres el GANADOR. 🏆✨ Volviendo al menú...")
                        game_over = True 
                        game_running = False 
                        pygame.mixer.music.stop() 
                        break 
                    else:
                        print(f"Cargando Nivel {current_level}...")
                        initialize_level() 
                        fn_render_map() 
                        continue 
            else:
                pass 
            
            fn_render_map()

def main_menu():
    """Muestra el menú principal y espera la entrada del usuario."""
    global game_running, current_level, game_over
    
    pygame.mixer.music.stop() 
    fn_clear_map()
    print("===================================")
    print("         FRUIT COLLECTOR           ")
    print("===================================")
    print("\n   Presiona S para Iniciar Juego")
    print("   Presiona Q para Salir")
    print("===================================")

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
                initialize_level()
                if not game_over: 
                    fn_render_map()
                    fn_move_avatar()
                
                if not game_running: 
                    fn_clear_map()
                    print("\n--- Juego Terminado ---")
                    print("Presiona R para volver al menú principal")
                    print("Presiona Q para salir del juego")
                    
                    while True:
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