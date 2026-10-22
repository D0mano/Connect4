import pygame
def create_gradient_circle(radius, center_color, edge_color):
    """
    Crée une surface contenant un cercle avec un dégradé radial.
    """
    # Créer une surface transparente de la taille du cercle
    surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)

    # Dessiner des cercles concentriques du bord vers le centre
    for r in range(radius, 0, -1):
        # Calculer le ratio d'interpolation (1.0 au bord, 0.0 au centre)
        ratio = r / radius

        # Interpoler chaque composante RGB
        r_c = int(center_color[0] + (edge_color[0] - center_color[0]) * ratio)
        g_c = int(center_color[1] + (edge_color[1] - center_color[1]) * ratio)
        b_c = int(center_color[2] + (edge_color[2] - center_color[2]) * ratio)

        current_color = (r_c, g_c, b_c)

        # Dessiner le cercle sur notre surface
        pygame.draw.circle(surface, current_color, (radius, radius), r)

    return surface