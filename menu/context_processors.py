from .models import MenuItem

def menu_context(request):
    menu_items = MenuItem.objects.filter(parent__isnull=True)
    return {'menu_items': menu_items}
