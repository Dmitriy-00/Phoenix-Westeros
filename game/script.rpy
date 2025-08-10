
# script.rpy
# Основной сценарий

# Заглушки изображений
image map_bg = Solid("#223344")
image inv_bg = Solid("#111111")
image inv_slot = Solid("#444444")
image icon_map = Solid("#8888ff")

image square_bg = Solid("#666666")
image tavern_bg = Solid("#774422")
image harbor_bg = Solid("#225577")
image alley_bg = Solid("#555555")

image coin = Solid("#ffd700")
image letter = Solid("#ffffff")

default current_location = "square"

label start:
    $ current_location = renpy.call_screen("city_map") or "square"
    while True:
        $ result = renpy.call_screen("location_screen", current_location)
        if result == "map":
            $ dest = renpy.call_screen("city_map")
            if dest:
                $ current_location = dest
        else:
            $ current_location = result
