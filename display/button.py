class Button:
    def __init__(self, text, font, pos_center, text_color, bg_color,padding=(20,10)):
        self.text_surf = font.render(text, True, text_color)
        self.text = text
        self.font = font
        self.rect = self.text_surf.get_rect(center=pos_center)
        # Agrandir le rectangle pour le fond

        self.bg_rect = self.rect.inflate(padding[0] * 2, padding[1] * 2)
        self.bg_color = bg_color
        self.text_color = text_color
        self.hover = False

