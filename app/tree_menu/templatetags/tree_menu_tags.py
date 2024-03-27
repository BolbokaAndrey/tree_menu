from django import template
from ..models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    cur_menu = context.request.GET.get("menu_name") or menu_name
    cur_item = context.request.GET.get("menu_item") or menu_name

    items = Menu.objects.get(name=cur_menu).items.filter(url=cur_item).select_related('parent')
    list_needed_items = _create_list_of_need_menu_item(items.first())

    return {
        "cur_menu": cur_menu,
        "menu_name": menu_name,
        "list": list_needed_items
    }


def _create_list_of_need_menu_item(item):
    need_menu_item = [item]
    while item.parent:
        item = item.parent
        need_menu_item.append(item)
    return need_menu_item
