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