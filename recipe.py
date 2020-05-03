class Recipe():
    """
    This class represents an recipe.
    """

    def __init__(self, name, servings, time, rating, url):
        self.name = name
        self.servings = servings
        self.time = time
        self.rating = rating
        self.url = url

        self.categories = []
        self.ingredients = []
        self.utensils = []
        self.steps = []
        self.notes = []
        self.tips = []
        self.variations = []
        self.ratings = []

    def add_category(self, category):
        self.categories.append(category)

    def add_ingredient(self, amount, ingredient):
        self.ingredients.append((amount, ingredient))

    def add_utensil(self, utensil):
        self.utensils.append(utensil)

    def add_step(self, step):
        self.steps.append(step)

    def add_note(self, note):
        self.notes.append(note)

    def add_tip(self, tip):
        self.tips.append(tip)

    def add_variation(self, variation):
        self.variations.append(variation)

    def add_rating(self, rating):
        self.ratings.append(rating)

    def wikicode(self, writer):
        # Define table styles
        style_titletable = 'tablestyle="margin-right:auto;margin-left:auto; width: 100%;text-align:center;"'
        style_title_title = '#BF31C3 height="75px" style="font-size:35px;font-weight:bold;border: 3px solid #BF31C3;color:#ffffff"'
        style_title_image = 'height="200pt" style="border:none;"'
        style_title_info = 'height="50pt" style="font-size:20px;font-weight:bold;border: 3px solid #BF31C3;color:#BF31C3"'

        style_infotable = 'tablestyle="margin-right:auto;margin-left:auto; width: 100%;text-align:center;" height="50pt" #BF31C3'
        style_info_headingrow = 'rowstyle="font-size:20px;font-weight:bold;color:#ffffff"'
        style_info_heading = '25% #BF31C3 style="border: none; border-right: 3px solid #fff;"'
        style_info_contentrow = 'height="40pt" rowstyle="font-size:20px;font-weight:bold;"'
        style_info_content = '25% style="border: none; border-bottom:3px solid #BF31C3"'

        style_ingredientstable = 'tablestyle="margin-right:auto;margin-left:auto; width: 100%;text-align:center;font-size:15px;"'
        style_ingredients_heading = '#BF31C3 height="50px" style="color:#ffffff;font-size:20px;font-weight:bold;border: 3px solid #BF31C3;"'
        style_ingredients_heading_2_left = '20% style="text-align:right;border:none;border-right:3px solid #BF31C3;border-bottom:3px solid #BF31C3"'
        style_ingredients_heading_2_right = '80% style="text-align:left;border:none;border-bottom:3px solid #BF31C3"'
        style_ingredients_subheading = '#BF31C3 style="color:#ffffff"'
        style_ingredients_left = '20% style="text-align:right;border:none;border-right:3px solid #BF31C3;"'
        style_ingredients_right = '80% style="text-align:left;border:none;"'

        style_heading = 'tablestyle="margin-right:auto;margin-left:auto; width: 100%;text-align:center;font-size:20px" #BF31C3 height="50px" style="font-size:20px;font-weight:bold;border: 3px solid #BF31C3;color:#ffffff;"'

        # Array holding the complete code
        code = []

        # Title table (title, image and Info header
        code.append(writer.table_cell(""))
        code.append(writer.table_cell(""))
        code.append(writer.table_cell(""))
        code.append(writer.table_cell(self.name, f"{style_titletable} {style_title_title}"))
        code.append(writer.table_row_end())
        code.append(writer.table_cell(""))
        code.append(writer.table_cell(""))
        code.append(writer.table_cell(""))
        code.append(writer.table_cell(writer.link(self.name, "attachment:rezept.jpg", "width=30%", display=True), style_title_image))
        code.append(writer.table_row_end())
        code.append(writer.table_cell(""))
        code.append(writer.table_cell(""))
        code.append(writer.table_cell(""))
        code.append(writer.table_cell("I  N  F  O", style_title_info))
        code.append(writer.table_row_end())
        code.append(writer.newline())

        # Basic information table
        code.append(writer.table_cell("Portionen", f"{style_infotable} {style_info_headingrow} {style_info_heading}"))
        code.append(writer.table_cell("Zeit", style_info_heading))
        code.append(writer.table_cell("Bewertung", style_info_heading))
        code.append(writer.table_cell("Link", style_info_heading))
        code.append(writer.table_row_end())
        code.append(writer.table_cell(self.servings, f"{style_info_contentrow} {style_info_content}"))
        code.append(writer.table_cell(self.time, style_info_content))
        code.append(writer.table_cell("🟢" * self.rating + "⚪" * (5 - self.rating), style_info_content))
        code.append(writer.table_cell(writer.link("Quelle", self.url), style_info_content))
        code.append(writer.table_row_end())
        code.append(writer.newline())
        code.append(writer.linebreak())
        code.append(writer.newline())

        # Ingredients table
        code.append(writer.table_cell(""))
        code.append(writer.table_cell("Zutaten", f"{style_ingredientstable} {style_ingredients_heading}"))
        code.append(writer.table_row_end())
        code.append(writer.table_cell("Menge", style_ingredients_heading_2_left))
        code.append(writer.table_cell("Zutat", style_ingredients_heading_2_right))
        code.append(writer.table_row_end())

        for ingredient in self.ingredients:
            if ingredient[0] == "----------":
                code.append(writer.table_cell(""))
                code.append(writer.table_cell(ingredient[1], style_ingredients_subheading))
            else:
                code.append(writer.table_cell(ingredient[0], style_ingredients_left))
                code.append(writer.table_cell(ingredient[1], style_ingredients_right))
            code.append(writer.table_row_end())

        # Sections
        sections = [(self.utensils, "Küchenutensilien"),
                    (self.steps, "Zubereitung"),
                    (self.notes, "Notizen"),
                    (self.tips, "Tipps"),
                    (self.variations, "Variationen"),
                    (self.ratings, "Bewertung")]

        for section in sections:
            code = code + self.wikicode_section(section[1], section[0], writer, style_heading)

        code.append(writer.newline())
        code.append(writer.newline())

        # Categories
        code.append(writer.hrule())

        for category in self.categories:
            code.append(f"{category} ")

        code.append(writer.newline())

        return ''.join(code)

    def wikicode_section(self, name, items, writer, style_heading):
        """
        Get the standard wiki code for a section with a unorderd list.
        """
        code = []

        if items:
            code.append(writer.newline())
            code.append(writer.linebreak())
            code.append(writer.newline())

            code.append(writer.table_cell(name, style_heading))
            code.append(writer.table_row_end())

            for item in items:
                code.append(writer.olitem(item))
                code.append(writer.newline())

        return code
