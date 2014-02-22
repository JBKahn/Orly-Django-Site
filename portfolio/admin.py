from django.contrib import admin
from portfolio.models import BridalPortfolio


class BridalPortfolioAdmin(admin.ModelAdmin):

    class Media:
        js = (
            'js/admin_list_reorder.js',
        )

    list_display = ('format_thumbnail', 'title', 'position')
    list_editable = ('position',)


admin.site.register(BridalPortfolio, BridalPortfolioAdmin)
