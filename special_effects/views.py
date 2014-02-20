from django.views.generic import TemplateView


class FXPortfolioView(TemplateView):
    template_name = 'special_effects.html'

    def get_context_data(self, **kwargs):
        return {"current_page_name": "FX Portfolio", "images": self.get_images()}

    def get_images(self):
        return [
            {"big_path": "img/se1big.jpeg", "small_path": "img/se1.jpeg", "title": "test_title"},
            {"big_path": "img/se2big.jpeg", "small_path": "img/se2.jpeg", "title": "test_title"},
            {"big_path": "img/se3big.jpeg", "small_path": "img/se3.jpeg", "title": "test_title"},
            {"big_path": "img/se4big.jpeg", "small_path": "img/se4.jpeg", "title": "test_title"},
            {"big_path": "img/se5big.jpeg", "small_path": "img/se5.jpeg", "title": "test_title"},
            {"big_path": "img/se6big.jpeg", "small_path": "img/se6.jpeg", "title": "test_title"},
        ]
