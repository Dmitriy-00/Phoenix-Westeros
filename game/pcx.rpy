# pcx.rpy
# Экран локации и обработчики хотспотов

init python:
    def item_by_id(id):
        if id == "letter":
            return Item("letter", "Письмо", "letter", "Письмо для стражника")
        if id == "coin":
            return Item("coin", "Монета", "coin", "Золотая монета")
        return None

    def pickup_item(hs):
        item = item_by_id(hs.data["item"])
        if item and not has_item(item.id):
            add_item(item)
            renpy.say(None, "Вы подняли %s." % item.name)
            locations[current_location].hotspots.remove(hs)

    def use_hotspot(hs):
        global harbor_unlocked, selected_item
        req = hs.data.get("required_item")
        if selected_item == req:
            renpy.say(None, hs.data.get("success_text", "Предмет использован."))
            if req == "letter":
                harbor_unlocked = True
                remove_item("letter")
            selected_item = None
        else:
            renpy.say(None, "Не подходит.")
            selected_item = None

    def move_to(target):
        if target == "harbor" and not harbor_unlocked:
            renpy.say(None, "Страж не пускает.")
        else:
            renpy.return_statement(target)

# экран локации
screen location_screen(loc_id):
    modal True
    default tooltip = ""
    $ loc = locations[loc_id]
    add loc.bg

    # хотспоты
    for hs in loc.hotspots:
        imagebutton:
            idle Solid("#0000")
            hover Solid("#ffffff20")
            xysize (hs.rect[2], hs.rect[3])
            xpos hs.rect[0]
            ypos hs.rect[1]
            if hs.kind == "pickup":
                action Function(pickup_item, hs)
            elif hs.kind == "use":
                action Function(use_hotspot, hs)
            elif hs.kind == "move":
                action Function(move_to, hs.data.get("target"))
            hovered SetScreenVariable("tooltip", hs.id)
            unhovered SetScreenVariable("tooltip", "")

    # переходы по краям
    if loc.neighbors.get("left"):
        imagebutton:
            idle Solid("#0000")
            hover Solid("#ffffff20")
            xysize (100,1080)
            xpos 0
            ypos 0
            action Function(move_to, loc.neighbors["left"])
    if loc.neighbors.get("right"):
        imagebutton:
            idle Solid("#0000")
            hover Solid("#ffffff20")
            xysize (100,1080)
            xpos 1820
            ypos 0
            action Function(move_to, loc.neighbors["right"])
    if loc.neighbors.get("up"):
        imagebutton:
            idle Solid("#0000")
            hover Solid("#ffffff20")
            xysize (1920,100)
            xpos 0
            ypos 0
            action Function(move_to, loc.neighbors["up"])
    if loc.neighbors.get("down"):
        imagebutton:
            idle Solid("#0000")
            hover Solid("#ffffff20")
            xysize (1920,100)
            xpos 0
            ypos 980
            action Function(move_to, loc.neighbors["down"])

    # HUD
    imagebutton:
        idle "icon_map"
        hover "icon_map"
        xpos 1820
        ypos 20
        action Return("map")
    textbutton "Инв" xpos 20 ypos 20 action Show("inventory_screen")

    if tooltip:
        text tooltip xalign 0.5 yalign 0.95

    key "i" action Show("inventory_screen")
    key "m" action Return("map")
