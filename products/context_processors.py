from .models import Microcontroller, Family


def global_microcontroller_context(request):
    families = Family.objects.all()

    family_microcontrollers = {}

    for family in families:
        microcontrollers = Microcontroller.objects.filter(category=family)
        family_microcontrollers[family.name] = microcontrollers
    return {
        "family_microcontrollers": family_microcontrollers,
    }
