from core.models import Portfolio


class SpecialEffects(Portfolio):
    def get_thumbnail_sprite(self):
        return 'special_effects'
