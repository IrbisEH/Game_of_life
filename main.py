import pygame
import sys

from pygame.locals import *

from functions import draw_text, draw_text_center
from functions import field_generator, check_and_change_cell
from functions import randomize_status_1, start_mode, change_mode
from functions import mode_1, mode_2, mode_3

FONT_NAME = pygame.font.match_font('gothampro_black')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 170, 6)

FPS = 40

GAME_STATUS_MODE = {
    'large': {
        'sum_edge_cells': 62,
        'first_pos': [129, 97],
        'render_step': 12,
        'render_img': 'image_10x10'
    },
    'future_mode': {}
}

GAME_MODE = 'large'

SUM_EDGE = GAME_STATUS_MODE[GAME_MODE]['sum_edge_cells']

CELLS_STATUS_MODES = {
    'start_mode': start_mode,
    '1_mode': mode_1,
    '2_mode': mode_2,
    '3_mode': mode_3,
    'random_mode': randomize_status_1,
}

CELLS_STATUS_MENU = [
    'start_mode',
    '1_mode',
    '2_mode',
    '3_mode',
    'random_mode',
]


class Cell(pygame.sprite.Sprite):
    """Объект ячейки"""

    image_star_10x10 = ['img/dead_star_10x10.png', 'img/life_star_10x10.png']

    def __init__(self, x_pos, y_pos, x_cor, y_cor):
        super().__init__()
        self.image_dead = pygame.image.load(self.image_star_10x10[0])
        self.image_life = pygame.image.load(self.image_star_10x10[1])
        self.status = 0
        self.image = self.image_dead
        self.position = [x_pos, y_pos]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_cor, y_cor)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def change_status(self, status):
        self.status = status
        if self.status == 1:
            self.image = self.image_life
        elif self.status == 0:
            self.image = self.image_dead

    def update_status(self, ):
        if self.status == 1:
            self.status = 0
            self.image = self.image_dead
        elif self.status == 0:
            self.status = 1
            self.image = self.image_life


def main():
    pygame.init()
    displaysurf = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption('LIFE')
    framepersec = pygame.time.Clock()

    # создаем таблицу с координатами отрисовки
    game_field = field_generator(
        GAME_STATUS_MODE[GAME_MODE]['sum_edge_cells'],
        GAME_STATUS_MODE[GAME_MODE]['first_pos'],
        GAME_STATUS_MODE[GAME_MODE]['render_step']
    )

    # создаем объекты ячеек и помещаем их в словарь
    cells_dict = {}
    for values in game_field:
        for position, coordinate in values:
            cells_dict[f'{position[0]}, {position[1]}'] = Cell(position[0],
                                                               position[1],
                                                               coordinate[0],
                                                               coordinate[1])

    # задаем стартовые статусы ячеек
    INDEX_MENU_MODE = 0
    CUR_MODE = CELLS_STATUS_MENU[INDEX_MENU_MODE]
    status_mode = change_mode(CUR_MODE, CELLS_STATUS_MODES)
    status_mode(cells_dict)

    # флаги для режимов игры
    FLAG_PLAY = False
    FLAG_RESTART = False
    FLAG_RESULT = False

    GENERETION = 0

    last_changes = []
    last_changes_2 = []
    last_changes_3 = []
    last_changes_4 = []

    """ Основной цикл игры """
    while True:
        # обрабатываем события клавиатуры
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_SPACE:
                    if not FLAG_PLAY:
                        FLAG_PLAY = True
                    else:
                        FLAG_PLAY = False
                elif event.key == K_r:
                    FLAG_RESTART = True
                elif event.key == K_LEFT and INDEX_MENU_MODE > 0:
                    INDEX_MENU_MODE -= 1
                    FLAG_RESTART = True
                elif event.key == K_RIGHT and INDEX_MENU_MODE < len(
                        CELLS_STATUS_MENU) - 1:
                    INDEX_MENU_MODE += 1
                    FLAG_RESTART = True

        # отрисовывка экрана
        displaysurf.fill(BLACK)
        # отрисовка ячеек
        for obj in cells_dict.values():
            obj.draw(displaysurf)

        # отрисовка текстов
        if FLAG_RESULT:
            result_text = f'result - {GENERETION} generations'
            draw_text_center(
                displaysurf,
                FONT_NAME,
                YELLOW,
                result_text,
                45, 500, 50
            )
        else:
            text = f'Generation: {GENERETION}'
            draw_text(displaysurf, FONT_NAME, YELLOW, text, 30, 390, 50)

        text = f'press SPACE - play/pause'
        draw_text(displaysurf, FONT_NAME, YELLOW, text, 20, 129, 920)

        text = f'press R - restart'
        draw_text(displaysurf, FONT_NAME, YELLOW, text, 20, 129, 950)

        pygame.draw.lines(
            displaysurf,
            YELLOW,
            False,
            [(645, 958), (625, 948), (645, 938)], 5)

        pygame.draw.lines(
            displaysurf,
            YELLOW,
            False,
            [(665, 958), (685, 948), (665, 938)], 5)

        text = CELLS_STATUS_MENU[INDEX_MENU_MODE]
        draw_text(displaysurf, FONT_NAME, YELLOW, text, 20, 700, 950)

        # обновление экрана
        pygame.display.update()
        # задаем FPS
        framepersec.tick(FPS)

        # перезапуск игры
        if FLAG_RESTART:
            GENERETION = 0

            for obj in cells_dict.values():
                obj.change_status(0)

            CUR_MODE = CELLS_STATUS_MENU[INDEX_MENU_MODE]
            status_mode = change_mode(CUR_MODE, CELLS_STATUS_MODES)
            if CUR_MODE == 'random_mode':
                status_mode(cells_dict, SUM_EDGE)
            else:
                status_mode(cells_dict)

            FLAG_RESTART = False
            FLAG_PLAY = False
            FLAG_RESULT = False

        # запуск игры
        if FLAG_PLAY:
            print(f'GENERETION - {GENERETION}')
            # проверяем и применяем изменения
            cur_changes = check_and_change_cell(
                cells_dict,
                GAME_STATUS_MODE[GAME_MODE]['sum_edge_cells']
            )

            if (cur_changes == last_changes or
                    cur_changes == last_changes_2 or
                    cur_changes == last_changes_3 or
                    cur_changes == last_changes_4):
                FLAG_PLAY = False
                FLAG_RESULT = True

            last_changes_4 = last_changes_3
            last_changes_3 = last_changes_2
            last_changes_2 = last_changes
            last_changes = cur_changes

            if FLAG_PLAY:
                GENERETION += 1


if '__main__' == __name__:
    main()
