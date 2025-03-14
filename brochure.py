import re

class Brochure:
    def __init__(self, brochure):
        self.brochure = brochure

    def get_thumbnail(self):
        img = self.brochure.find('img')
        return img.get('src') if img and img.get('src') else img.get('data-src', "N/A")

    def get_title(self):
        title = self.brochure.find('strong')
        return title.text if title else "N/A"

    def get_shop(self):
        shop_data = self.brochure.find('a').get('title').split(',')[0].split()
        shop_i = shop_data.index('Geschäftes')
        shop = ' '.join(shop_data[shop_i + 1:])
        return shop if shop is not None else "N/A"

    def get_dates(self):
        date_pattern = r'\d{2}.\d{2}.\d{4}'
        dates = re.findall(date_pattern, self.brochure.find('small').text)
        formatted_dates = []
        for d in dates:
            d_list = d.split('.')
            d_list.reverse()
            formatted_dates.append('-'.join(d_list))
        valid_from = formatted_dates[0] if formatted_dates else 'N/A'
        valid_to = formatted_dates[1] if len(formatted_dates) > 1 else 'N/A'
        return valid_from, valid_to

    def to_dict(self):
        valid_from, valid_to = self.get_dates()
        return {
            "title": self.get_title(),
            "thumbnail": self.get_thumbnail(),
            "shop_name": self.get_shop(),
            "valid_from": valid_from,
            "valid_to": valid_to,
            "parsed_time": valid_from + ' 00:00:00'
        }