from django.contrib import admin
from reviews.models import ClientReview


class ClientReviewAdmin(admin.ModelAdmin):

    class Media:
        js = (
            'js/admin_list_reorder.js',
        )

    list_display = ('active', 'name', 'text', 'position')
    list_editable = ('position',)


admin.site.register(ClientReview, ClientReviewAdmin)
