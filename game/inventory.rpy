
# inventory.rpy
# Логика и экран инвентаря

default inventory = []
default selected_item = None
default inv_selected_index = None

init python:
    class Item:
        def __init__(self, id, name, icon, description):
            self.id = id
            self.name = name
            self.icon = icon
            self.description = description

    def has_item(id):
        return any(i.id == id for i in inventory)

    def add_item(item):
        if not has_item(item.id):
            inventory.append(item)

    def remove_item(id):
        for i in inventory:
            if i.id == id:
                inventory.remove(i)
                return

# экран инвентаря
screen inventory_screen():
    tag menu
    modal True
    add "inv_bg"
    grid 4 2:
        xalign 0.5
        yalign 0.5
        spacing 20
        for i in range(8):
            if i < len(inventory):
                $ it = inventory[i]
                imagebutton:
                    idle it.icon
                    hover it.icon
                    xysize (100,100)
                    action SetVariable("inv_selected_index", i)
            else:
                add "inv_slot"
    if inv_selected_index is not None:
        $ it = inventory[inv_selected_index]
        frame:
            xalign 0.5
            yalign 0.9
            vbox:
                text it.name
                text it.description
                textbutton "Использовать" action [SetVariable("selected_item", it.id), SetVariable("inv_selected_index", None), Hide("inventory_screen")]
    key "i" action Hide("inventory_screen")
