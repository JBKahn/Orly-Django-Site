from django.views.generic import TemplateView


class PortfolioView(TemplateView):
    template_name = 'portfolio.html'

    def get_context_data(self, **kwargs):
        return {"current_page_name": "Bridal Portfolio", "images": self.get_images()}

    def get_images(self):
        return [
            {"big_path": "img/1big.png", "small_path": "img/1.png", "title": "test_title"},
            {"big_path": "img/2big.jpeg", "small_path": "img/2.jpeg", "title": "test_title"},
            {"big_path": "img/3big.png", "small_path": "img/3.png", "title": "test_title"},
            {"big_path": "img/4big.jpeg", "small_path": "img/4.jpeg", "title": "test_title"},
            {"big_path": "img/5big.jpeg", "small_path": "img/5.jpeg", "title": "test_title"},
            {"big_path": "img/6big.jpeg", "small_path": "img/6.jpeg", "title": "test_title"},
            {"big_path": "img/7big.png", "small_path": "img/7.png", "title": "test_title"},
            {"big_path": "img/8big.png", "small_path": "img/8.png", "title": "test_title"},
            {"big_path": "img/9big.png", "small_path": "img/9.png", "title": "test_title"},
            {"big_path": "img/10big.png", "small_path": "img/10.png", "title": "test_title"},
            {"big_path": "img/11big.jpeg", "small_path": "img/11.jpeg", "title": "test_title"},
            {"big_path": "img/12big.jpeg", "small_path": "img/12.jpeg", "title": "test_title"},
            {"big_path": "img/13big.jpeg", "small_path": "img/13.jpeg", "title": "test_title"},
            {"big_path": "img/14big.jpeg", "small_path": "img/14.jpeg", "title": "test_title"},
            {"big_path": "img/15big.png", "small_path": "img/15.png", "title": "test_title"},
            {"big_path": "img/16big.jpeg", "small_path": "img/16.jpeg", "title": "test_title"},
            {"big_path": "img/17big.png", "small_path": "img/17.png", "title": "test_title"},
            {"big_path": "img/18big.jpeg", "small_path": "img/18.jpeg", "title": "test_title"},
            {"big_path": "img/19big.jpeg", "small_path": "img/19.jpeg", "title": "test_title"},
            {"big_path": "img/20big.png", "small_path": "img/20.png", "title": "test_title"},
            {"big_path": "img/21big.jpeg", "small_path": "img/21.jpeg", "title": "test_title"},
            {"big_path": "img/22big.jpeg", "small_path": "img/22.jpeg", "title": "test_title"},
            {"big_path": "img/23big.png", "small_path": "img/23.png", "title": "test_title"},
            {"big_path": "img/24big.png", "small_path": "img/24.png", "title": "test_title"},
            {"big_path": "img/25big.png", "small_path": "img/25.png", "title": "test_title"},
            {"big_path": "img/26big.png", "small_path": "img/26.png", "title": "test_title"},
        ]
