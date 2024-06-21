import pygame
import time
import utils
pygame.init()
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
font_size = 36
font = pygame.font.Font(None, font_size)


def draw_text(screen, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


info_display = pygame.display.Info()
screen_width = info_display.current_w
screen_height = info_display.current_h
decalage = (screen_width - screen_height) / 2
while True:
    screen = pygame.display.set_mode((screen_width, screen_height))
    initial_text = "Combien de colonnes souhaitez-vous ? "
    input_text = initial_text
    ClicDepart = 0
    DessinGrille = 0
    Player = 0
    Turn = 0
    Wait = 0
    Colonne = 0
    Alignement = 0
    TailleNombre = 0
    NombreInter1 = 0
    NombreInter2 = 0
    reset = 0
    coup_rouge = []
    coup_bleu = []
    coup_vert = []
    Gagnant = ""
    Game = True
    while Game:
        if ClicDepart == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_BACKSPACE and len(input_text) > 37:
                        # Supprimer le dernier caractère
                        input_text = input_text[:-1]
                        TailleNombre -= 1
                        if TailleNombre == 1:
                            Colonne -= NombreInter2/10
                        if TailleNombre == 0:
                            Colonne -= NombreInter1
                    elif event.key >= pygame.K_0 and event.key <= pygame.K_9 and TailleNombre < 2:
                        try:
                            int(event.unicode)
                            input_text += event.unicode
                            print(input_text)
                            if TailleNombre == 0:
                                NombreInter1 = int(event.unicode)
                                Colonne += NombreInter1
                            if TailleNombre == 1:
                                NombreInter2 = int(event.unicode)
                                Colonne += NombreInter2/10

                            TailleNombre += 1
                            print(Colonne)
                        except:
                            pass
                        # Vous pouvez ajouter d'autres actions ic

                    elif event.key == pygame.K_RETURN:
                        # Action à effectuer lorsque la touche "Entrée" est pressée
                        print(Colonne*(10**(TailleNombre-1)))
                        if Colonne*(10**(TailleNombre-1)) > 2:
                            ClicDepart = 1
                            Colonne = int(Colonne*(10**(TailleNombre-1))+0.1)

            screen.fill(WHITE)

            # Affiche le texte saisi
            draw_text(screen, input_text, font, BLACK, 50, 50)
            pygame.display.flip()
            continue
        if ClicDepart == 1:
            if reset == 0:
                TailleNombre = 0
                NombreInter1 = 0
                NombreInter2 = 0
                reset = 1
                initial_text = "Combien de croix souhaitez vous alignez ? "
                input_text = initial_text
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_BACKSPACE and len(input_text) > 42:
                        # Supprimer le dernier caractère
                        input_text = input_text[:-1]
                        TailleNombre -= 1
                        if TailleNombre == 1:
                            Alignement -= NombreInter2/10
                        if TailleNombre == 0:
                            Alignement -= NombreInter1
                    elif event.key >= pygame.K_0 and event.key <= pygame.K_9 and TailleNombre < 2:
                        try:
                            int(event.unicode)
                            input_text += event.unicode
                            print(input_text)
                            if TailleNombre == 0:
                                NombreInter1 = int(event.unicode)
                                Alignement += NombreInter1
                            if TailleNombre == 1:
                                NombreInter2 = int(event.unicode)
                                Alignement += NombreInter2/10

                            TailleNombre += 1
                            print(Alignement)
                        except:
                            pass
                        # Vous pouvez ajouter d'autres actions ic

                    elif event.key == pygame.K_RETURN:
                        # Action à effectuer lorsque la touche "Entrée" est pressée
                        print(Alignement*(10**(TailleNombre-1)))
                        if Alignement*(10**(TailleNombre-1)) > 2 and Alignement*(10**(TailleNombre-1)) <= Colonne:
                            ClicDepart = 2
                            Alignement = int(Alignement*(10**(TailleNombre-1))+0.1)

            screen.fill(WHITE)

            # Affiche le texte saisi
            draw_text(screen, input_text, font, BLACK, 50, 50)
            pygame.display.flip()
            continue
        if ClicDepart == 2:
            if reset == 1:
                TailleNombre = 0
                NombreInter1 = 0
                NombreInter2 = 0
                reset = 2
                initial_text = "Etes-vous 2 ou 3 joueurs ? "
                input_text = initial_text
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_BACKSPACE and len(input_text) > 27:
                        # Supprimer le dernier caractère
                        input_text = input_text[:-1]
                        TailleNombre -= 1
                        if TailleNombre == 0:
                            Player -= NombreInter1
                    elif event.key >= pygame.K_0 and event.key <= pygame.K_9 and TailleNombre == 0:
                        try:
                            int(event.unicode)
                            input_text += event.unicode
                            print(input_text)
                            if TailleNombre==0:
                                NombreInter1 = int(event.unicode)
                                Player += NombreInter1
                            TailleNombre+=1
                            print(Player)
                        except:
                            pass
                        # Vous pouvez ajouter d'autres actions ic

                    elif event.key == pygame.K_RETURN:
                        # Action à effectuer lorsque la touche "Entrée" est pressé
                        if Player == 2 or Player == 3:
                            ClicDepart = 3
                            Player = int(Player)

            screen.fill(WHITE)

            # Affiche le texte saisi
            draw_text(screen, input_text, font, BLACK, 50, 50)
            pygame.display.flip()
        if ClicDepart == 3:
            if Player == 2:
                if Colonne >= 11:
                    if DessinGrille == 0:
                        screen = pygame.display.set_mode((screen_width, screen_height))
                        for i in range(1, Colonne):
                            pygame.draw.line(screen, WHITE,
                                             ((screen_width - screen_height) / 2, i * screen_height // Colonne), (
                                                 Colonne * screen_height // Colonne + (
                                                         screen_width - screen_height) / 2,
                                                 i * screen_height // Colonne))

                        for i in range(1, Colonne):
                            pygame.draw.line(screen, WHITE,
                                             ((screen_height // Colonne) * i + (screen_width - screen_height) / 2, 0), (
                                                 (screen_height // Colonne) * i + (screen_width - screen_height) / 2,
                                                 (screen_height // Colonne) * Colonne))
                        pygame.display.update()
                    DessinGrille = 1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                mouse_pos = event.pos
                            mouse_pos = pygame.mouse.get_pos()
                            (x, y) = mouse_pos
                            (trace_x, trace_y) = (
                                ((x - ((screen_width - screen_height) / 2)) // (screen_height // Colonne)),
                                y // (screen_height // Colonne))
                            if Colonne * trace_y + trace_x + 1 in coup_bleu or Colonne * trace_y + trace_x + 1 in coup_rouge:
                                continue
                            else:
                                if Turn % 2 == 0:
                                    pygame.draw.line(screen, RED, (
                                        trace_x * (screen_height // Colonne) + (
                                                screen_height // (4 * Colonne)) + decalage,
                                        trace_y * (screen_height // Colonne) + (screen_height // (4 * Colonne))),
                                                     (trace_x * (screen_height // Colonne) + (
                                                             3 * screen_height // (4 * Colonne)) + decalage,
                                                      trace_y * (screen_height // Colonne) + (
                                                              3 * screen_height // (4 * Colonne))))
                                    pygame.draw.line(screen, RED, (
                                        trace_x * (screen_height // Colonne) + (
                                                3 * screen_height // (4 * Colonne)) + decalage,
                                        trace_y * (screen_height // Colonne) + (screen_height // (4 * Colonne))),
                                                     (trace_x * (screen_height // Colonne) + (
                                                             screen_height // (4 * Colonne)) + decalage,
                                                      trace_y * (screen_height // Colonne) + (
                                                              3 * screen_height // (4 * Colonne))))
                                    coup_rouge.append(Colonne * trace_y + trace_x + 1)
                                if Turn % 2 == 1:
                                    pygame.draw.circle(screen, BLUE, (
                                        trace_x * (screen_height // Colonne) + (
                                                screen_height // (2 * Colonne)) + decalage,
                                        trace_y * (screen_height // Colonne) + (screen_height // (2 * Colonne))),
                                                       (screen_height // (4 * Colonne)), 5)
                                    coup_bleu.append(Colonne * trace_y + trace_x + 1)
                                Turn += 1
                    (Game, Gagnant) = utils.isWinner3player(Colonne, coup_rouge, coup_bleu, coup_vert, Alignement)
                    pygame.display.flip()
                else:
                    if DessinGrille == 0:
                        screen = pygame.display.set_mode((100 * Colonne, 100 * Colonne))
                        for i in range(1, Colonne):
                            pygame.draw.line(screen, WHITE, (0, 100 * i), (100 * Colonne, 100 * i))

                        for i in range(1, Colonne):
                            pygame.draw.line(screen, WHITE, (100 * i, 0), (100 * i, 100 * Colonne))
                        pygame.display.update()
                    DessinGrille = 1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                mouse_pos = event.pos
                            mouse_pos = pygame.mouse.get_pos()
                            (x, y) = mouse_pos
                            (trace_x, trace_y) = (x // 100, y // 100)
                            if Colonne * trace_y + trace_x + 1 in coup_bleu or Colonne * trace_y + trace_x + 1 in coup_rouge:
                                continue
                            else:
                                if Turn % 2 == 0:
                                    pygame.draw.line(screen, RED, (trace_x * 100 + 25, trace_y * 100 + 25),
                                                     (trace_x * 100 + 75,
                                                      trace_y * 100 + 75))
                                    pygame.draw.line(screen, RED, (trace_x * 100 + 75, trace_y * 100 + 25),
                                                     (trace_x * 100 + 25, trace_y * 100 + 75))
                                    coup_rouge.append(Colonne * trace_y + trace_x + 1)
                                if Turn % 2 == 1:
                                    pygame.draw.circle(screen, BLUE, (trace_x * 100 + 50, trace_y * 100 + 50), 25, 5)
                                    coup_bleu.append(Colonne * trace_y + trace_x + 1)
                                Turn += 1
                    (Game, Gagnant) = utils.isWinner3player(Colonne, coup_rouge, coup_bleu, coup_vert, Alignement)
                    pygame.display.flip()
            if Player == 3:
                if Colonne >= 11:
                    if DessinGrille == 0:
                        screen = pygame.display.set_mode((screen_width, screen_height))
                        for i in range(1, Colonne):
                            pygame.draw.line(screen, WHITE,
                                             ((screen_width - screen_height) / 2, i * screen_height // Colonne), (
                                                 Colonne * screen_height // Colonne + (
                                                             screen_width - screen_height) / 2,
                                                 i * screen_height // Colonne))

                        for i in range(1, Colonne):
                            pygame.draw.line(screen, WHITE,
                                             ((screen_height // Colonne) * i + (screen_width - screen_height) / 2, 0), (
                                                 (screen_height // Colonne) * i + (screen_width - screen_height) / 2,
                                                 (screen_height // Colonne) * Colonne))
                        pygame.display.update()
                    DessinGrille = 1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                mouse_pos = event.pos
                            mouse_pos = pygame.mouse.get_pos()
                            (x, y) = mouse_pos
                            (trace_x, trace_y) = (
                            ((x - ((screen_width - screen_height) / 2)) // (screen_height // Colonne)),
                            y // (screen_height // Colonne))
                            if Colonne * trace_y + trace_x + 1 in coup_bleu or Colonne * trace_y + trace_x + 1 in coup_rouge:
                                continue
                            else:
                                if Turn % 3 == 0:
                                    pygame.draw.line(screen, RED, (
                                        trace_x * (screen_height // Colonne) + (
                                                    screen_height // (4 * Colonne)) + decalage,
                                        trace_y * (screen_height // Colonne) + (screen_height // (4 * Colonne))),
                                                     (trace_x * (screen_height // Colonne) + (
                                                             3 * screen_height // (4 * Colonne)) + decalage,
                                                      trace_y * (screen_height // Colonne) + (
                                                              3 * screen_height // (4 * Colonne))))
                                    pygame.draw.line(screen, RED, (
                                        trace_x * (screen_height // Colonne) + (
                                                    3 * screen_height // (4 * Colonne)) + decalage,
                                        trace_y * (screen_height // Colonne) + (screen_height // (4 * Colonne))),
                                                     (trace_x * (screen_height // Colonne) + (
                                                             screen_height // (4 * Colonne)) + decalage,
                                                      trace_y * (screen_height // Colonne) + (
                                                              3 * screen_height // (4 * Colonne))))
                                    coup_rouge.append(Colonne * trace_y + trace_x + 1)
                                if Turn % 3 == 1:
                                    pygame.draw.circle(screen, BLUE, (
                                        trace_x * (screen_height // Colonne) + (
                                                    screen_height // (2 * Colonne)) + decalage,
                                        trace_y * (screen_height // Colonne) + (screen_height // (2 * Colonne))),
                                                       (screen_height // (4 * Colonne)), 5)
                                    coup_bleu.append(Colonne * trace_y + trace_x + 1)
                                if Turn % 3 == 2:
                                    pygame.draw.rect(screen, GREEN, (
                                    trace_x * (screen_height // Colonne) + (screen_height // (4 * Colonne)) + decalage,
                                    (screen_height // Colonne) * trace_y + (screen_height // (4 * Colonne)),
                                    (screen_height // (2 * Colonne)), (screen_height // (2 * Colonne))), 5)
                                    coup_vert.append(Colonne * trace_y + trace_x + 1)
                                Turn += 1
                    (Game, Gagnant) = utils.isWinner3player(Colonne, coup_rouge, coup_bleu, coup_vert, Alignement)
                    pygame.display.flip()
                else:
                    if DessinGrille == 0:
                        screen = pygame.display.set_mode((100 * Colonne, 100 * Colonne))
                        for i in range(1, Colonne):
                            pygame.draw.line(screen, WHITE, (0, 100 * i), (100 * Colonne, 100 * i))

                        for i in range(1, Colonne):
                            pygame.draw.line(screen, WHITE, (100 * i, 0), (100 * i, 100 * Colonne))
                        pygame.display.update()
                    DessinGrille = 1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                mouse_pos = event.pos
                            mouse_pos = pygame.mouse.get_pos()
                            (x, y) = mouse_pos
                            (trace_x, trace_y) = (x // 100 ,y // 100)
                            if Colonne * trace_y + trace_x + 1 in coup_bleu or Colonne * trace_y + trace_x + 1 in coup_rouge:
                                continue
                            else:
                                utils.dessin_symbole3player_Moins11(screen, RED, BLUE, GREEN, trace_x, trace_y, Turn, Colonne, coup_rouge, coup_bleu, coup_vert)
                    (Game, Gagnant) = utils.isWinner3player(Colonne, coup_rouge, coup_bleu, coup_vert, Alignement)
                    pygame.display.flip()


    while Wait < 3:
        utils.affichage_gagnant(Gagnant, screen, RED, BLUE, GREEN)
        time.sleep(3)
        Wait+=3