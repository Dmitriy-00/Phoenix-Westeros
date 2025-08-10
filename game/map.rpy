# map.rpy
# Логика и экран карты города

screen city_map():
    tag menu
    modal True
    add "map_bg"
    imagebutton:
        idle Solid("#00000000")
        hover Solid("#ffffff20")
        xysize (200,80)
        xpos 300
        ypos 300
        text "Площадь"
        action Return("square")
    imagebutton:
        idle Solid("#00000000")
        hover Solid("#ffffff20")
        xysize (200,80)
        xpos 700
        ypos 300
        text "Таверна"
        action Return("tavern")
    imagebutton:
        idle Solid("#00000000")
        hover Solid("#ffffff20")
        xysize (200,80)
        xpos 1100
        ypos 300
        text "Гавань"
        action Return("harbor")
    imagebutton:
        idle Solid("#00000000")
        hover Solid("#ffffff20")
        xysize (200,80)
        xpos 1500
        ypos 300
        text "Переулок"
        action Return("alley")
    key "m" action Return(None)
