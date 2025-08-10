# screens.rpy
# Экран быстрого меню

screen quick_menu():
    zorder 100
    hbox:
        style_prefix "quick"
        xalign 0.5
        yalign 1.0
        spacing 20
        textbutton _("Назад") action Rollback()
        textbutton _("Карта") action Return("map")
        textbutton _("Инвентарь") action Show("inventory_screen")
        textbutton _("Пропуск") action Skip()
        textbutton _("Авто") action Preference("auto-forward", "toggle")
        textbutton _("Опции") action ShowMenu("preferences")
