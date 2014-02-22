from django.contrib import admin
from special_effects.models import SpecialEffects


class SpecialEffectsAdmin(admin.ModelAdmin):

    class Media:
        js = (
            'js/admin_list_reorder.js',
        )

    list_display = ('format_thumbnail', 'title', 'position')
    list_editable = ('position',)


admin.site.register(SpecialEffects, SpecialEffectsAdmin)
