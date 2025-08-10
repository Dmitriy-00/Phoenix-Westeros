# locations.rpy
# Описание локаций и хотспотов

init python:
    class Hotspot:
        def __init__(self, id, rect, kind, data):
            self.id = id
            self.rect = rect  # (x, y, w, h)
            self.kind = kind
            self.data = data

    class Location:
        def __init__(self, id, name, bg, neighbors, hotspots):
            self.id = id
            self.name = name
            self.bg = bg
            self.neighbors = neighbors  # dict с направлениями
            self.hotspots = hotspots

# словарь всех локаций
default locations = {}

init python:
    locations = {
        "square": Location(
            "square", "Площадь", "square_bg",
            {"right": "tavern", "down": "alley"},
            [
                Hotspot("letter", (900, 500, 120, 120), "pickup", {"item": "letter"}),
            ]
        ),
        "tavern": Location(
            "tavern", "Таверна", "tavern_bg",
            {"left": "square", "right": "harbor"},
            [
                Hotspot("guard", (1500, 400, 200, 300), "use", {"required_item": "letter", "success_text": "Страж пропустил."}),
            ]
        ),
        "harbor": Location(
            "harbor", "Гавань", "harbor_bg",
            {"left": "tavern"},
            [
                Hotspot("coin", (900, 500, 120, 120), "pickup", {"item": "coin"}),
            ]
        ),
        "alley": Location(
            "alley", "Переулок", "alley_bg",
            {"up": "square"},
            [
                Hotspot("coin", (800, 500, 120, 120), "pickup", {"item": "coin"}),
            ]
        ),
    }
