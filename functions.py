import random
import pygame


def draw_text(surf, font_name, color, text, size, x, y):
    """ Отрисовка текста, позиция середина-лево. """
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midleft = (x, y)
    surf.blit(text_surface, text_rect)


def draw_text_center(surf, font_name, color, text, size, x, y):
    """ Отрисовка текста, позиция середина. """
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surf.blit(text_surface, text_rect)


def check_status(checking_obj, count):
    """ Проверка соседних ячеек. """
    if checking_obj.status == 0:
        if count == 3:
            return True
        else:
            return False
    elif checking_obj.status == 1:
        if count == 2:
            return False
        elif count == 3:
            return False
        else:
            return True


def check_and_change_cell(obj_dict, sum_edge_cells):
    """
    Функция проверяет каждую ячейку и меняет её статус,
    возвращает список координатами изменений.
    """
    # список изменений
    change_list = []

    for y in range(sum_edge_cells):
        # проверяем самый верхний ряд
        if y == 0:
            for x in range(sum_edge_cells):
                # проверяем самую верхнюю левую ячейку
                if x == 0:
                    cheking_obj = obj_dict[f'{x}, {y}']
                    obj_right = obj_dict[f'{x + 1}, {y}']
                    obj_rightdown = obj_dict[f'{x + 1}, {y + 1}']
                    obj_down = obj_dict[f'{x}, {y + 1}']

                    count = 0
                    if obj_right.status != 0:
                        count += 1
                    if obj_rightdown.status != 0:
                        count += 1
                    if obj_down.status != 0:
                        count += 1

                    if check_status(cheking_obj, count):
                        change_list.append(cheking_obj)

                # проверяем самую верхнюю правую ячейку
                elif x == sum_edge_cells - 1:
                    cheking_obj = obj_dict[f'{x}, {y}']
                    obj_down = obj_dict[f'{x}, {y + 1}']
                    obj_leftdown = obj_dict[f'{x - 1}, {y + 1}']
                    obj_left = obj_dict[f'{x - 1}, {y}']

                    count = 0
                    if obj_down.status == 1:
                        count += 1
                    if obj_leftdown.status == 1:
                        count += 1
                    if obj_left.status == 1:
                        count += 1

                    if check_status(cheking_obj, count):
                        change_list.append(cheking_obj)

                # проверяем все отальные в верхнем ряду
                else:
                    cheking_obj = obj_dict[f'{x}, {y}']
                    obj_right = obj_dict[f'{x + 1}, {y}']
                    obj_rightdown = obj_dict[f'{x + 1}, {y + 1}']
                    obj_down = obj_dict[f'{x}, {y + 1}']
                    obj_leftdown = obj_dict[f'{x - 1}, {y + 1}']
                    obj_left = obj_dict[f'{x - 1}, {y}']

                    count = 0
                    if obj_right.status == 1:
                        count += 1
                    if obj_rightdown.status == 1:
                        count += 1
                    if obj_down.status == 1:
                        count += 1
                    if obj_leftdown.status == 1:
                        count += 1
                    if obj_left.status == 1:
                        count += 1

                    if check_status(cheking_obj, count):
                        change_list.append(cheking_obj)

        # проверяем самый нижний ряд
        elif y == sum_edge_cells - 1:
            for x in range(sum_edge_cells):
                # проверяем самую нижнюю левую ячейку
                if x == 0:
                    cheking_obj = obj_dict[f'{x}, {y}']
                    obj_top = obj_dict[f'{x}, {y - 1}']
                    obj_righttop = obj_dict[f'{x + 1}, {y - 1}']
                    obj_right = obj_dict[f'{x + 1}, {y}']

                    count = 0
                    if obj_top.status == 1:
                        count += 1
                    if obj_righttop.status == 1:
                        count += 1
                    if obj_right.status == 1:
                        count += 1

                    if check_status(cheking_obj, count):
                        change_list.append(cheking_obj)

                # проверяем самую нижнюю правую ячейку
                elif x == sum_edge_cells - 1:
                    cheking_obj = obj_dict[f'{x}, {y}']
                    obj_top = obj_dict[f'{x}, {y - 1}']
                    obj_left = obj_dict[f'{x - 1}, {y}']
                    obj_lefttop = obj_dict[f'{x - 1}, {y - 1}']

                    count = 0
                    if obj_top.status == 1:
                        count += 1
                    if obj_left.status == 1:
                        count += 1
                    if obj_lefttop.status == 1:
                        count += 1

                    if check_status(cheking_obj, count):
                        change_list.append(cheking_obj)

                # проверяем все сотальные в нижнем ряду
                else:
                    cheking_obj = obj_dict[f'{x}, {y}']
                    obj_top = obj_dict[f'{x}, {y - 1}']
                    obj_righttop = obj_dict[f'{x + 1}, {y - 1}']
                    obj_right = obj_dict[f'{x + 1}, {y}']
                    obj_left = obj_dict[f'{x - 1}, {y}']
                    obj_lefttop = obj_dict[f'{x - 1}, {y - 1}']

                    count = 0
                    if obj_top.status == 1:
                        count += 1
                    if obj_righttop.status == 1:
                        count += 1
                    if obj_right.status == 1:
                        count += 1
                    if obj_left.status == 1:
                        count += 1
                    if obj_lefttop.status == 1:
                        count += 1

                    if check_status(cheking_obj, count):
                        change_list.append(cheking_obj)

        # проверяем все остальные ряды
        else:
            for x in range(sum_edge_cells):
                # проверяем самую левую ячейку
                if x == 0:
                    cheking_obj = obj_dict[f'{x}, {y}']
                    obj_top = obj_dict[f'{x}, {y - 1}']
                    obj_righttop = obj_dict[f'{x + 1}, {y - 1}']
                    obj_right = obj_dict[f'{x + 1}, {y}']
                    obj_rightdown = obj_dict[f'{x + 1}, {y + 1}']
                    obj_down = obj_dict[f'{x}, {y + 1}']

                    count = 0
                    if obj_top.status == 1:
                        count += 1
                    if obj_righttop.status == 1:
                        count += 1
                    if obj_right.status == 1:
                        count += 1
                    if obj_rightdown.status == 1:
                        count += 1
                    if obj_down.status == 1:
                        count += 1

                    if check_status(cheking_obj, count):
                        change_list.append(cheking_obj)

                # проверяем самую правую ячейку
                elif x == sum_edge_cells - 1:
                    cheking_obj = obj_dict[f'{x}, {y}']
                    obj_top = obj_dict[f'{x}, {y - 1}']
                    obj_down = obj_dict[f'{x}, {y + 1}']
                    obj_leftdown = obj_dict[f'{x - 1}, {y + 1}']
                    obj_left = obj_dict[f'{x - 1}, {y}']
                    obj_lefttop = obj_dict[f'{x - 1}, {y - 1}']

                    count = 0
                    if obj_top.status == 1:
                        count += 1
                    if obj_down.status == 1:
                        count += 1
                    if obj_leftdown.status == 1:
                        count += 1
                    if obj_left.status == 1:
                        count += 1
                    if obj_lefttop.status == 1:
                        count += 1

                    if check_status(cheking_obj, count):
                        change_list.append(cheking_obj)

                # проверяем все сотальные в тукущем ряду
                else:
                    cheking_obj = obj_dict[f'{x}, {y}']
                    obj_top = obj_dict[f'{x}, {y - 1}']
                    obj_righttop = obj_dict[f'{x + 1}, {y - 1}']
                    obj_right = obj_dict[f'{x + 1}, {y}']
                    obj_rightdown = obj_dict[f'{x + 1}, {y + 1}']
                    obj_down = obj_dict[f'{x}, {y + 1}']
                    obj_leftdown = obj_dict[f'{x - 1}, {y + 1}']
                    obj_left = obj_dict[f'{x - 1}, {y}']
                    obj_lefttop = obj_dict[f'{x - 1}, {y - 1}']

                    count = 0
                    if obj_top.status == 1:
                        count += 1
                    if obj_righttop.status == 1:
                        count += 1
                    if obj_right.status == 1:
                        count += 1
                    if obj_rightdown.status == 1:
                        count += 1
                    if obj_down.status == 1:
                        count += 1
                    if obj_leftdown.status == 1:
                        count += 1
                    if obj_left.status == 1:
                        count += 1
                    if obj_lefttop.status == 1:
                        count += 1

                    if check_status(cheking_obj, count):
                        change_list.append(cheking_obj)
    # применяем изменения
    for obj in change_list:
        obj.update_status()

    return change_list


def parse_status_mode(positions, obj_dict):
    """ Меняет статусы ячеек по переданному списку """
    for char in positions:
        for lines in char:
            for y in range(lines[0], lines[1]):
                for x in range(lines[2], lines[3]):
                    obj = obj_dict[f'{x}, {y}']
                    obj.update_status()


def start_mode(obj_dict):
    """ Статусы ячеек - слово LIFE. """
    text_life = [
        [[20, 41, 4, 6], [41, 43, 4, 14]],
        [[22, 41, 22, 24], [41, 43, 18, 28], [20, 22, 18, 28]],
        [[20, 43, 34, 36], [20, 22, 36, 44], [29, 31, 36, 43]],
        [[20, 43, 49, 51], [20, 22, 51, 58], [29, 31, 51, 58],
         [41, 43, 51, 58]]
    ]
    parse_status_mode(text_life, obj_dict)


def randomize_status_1(obj_dict, sum_edge):
    """ Рандомные статусы ячеек. """
    for y in range(sum_edge):
        for x in range(sum_edge):
            obj = obj_dict[f'{x}, {y}']
            r = random.randint(0, 1)
            if r == 1:
                obj.update_status()

    return obj_dict


def mode_1(obj_dict):
    """ Статусы ячеек - прямоугольник. """
    rectangle = [
        [[21, 42, 30, 32]],
    ]
    parse_status_mode(rectangle, obj_dict)


def mode_2(obj_dict):
    gun = [
        [[27, 28, 26, 28]],
        [[28, 29, 25, 26]],
        [[29, 30, 24, 25], [29, 30, 38, 39]],
        [[30, 31, 15, 16], [30, 31, 24, 25], [30, 31, 37, 39]],
        [[31, 32, 14, 16], [31, 32, 24, 25], [31, 32, 40, 42]],
        [[32, 33, 25, 26], [32, 33, 40, 43], [32, 33, 49, 50]],
        [[33, 34, 26, 28], [33, 34, 40, 42], [33, 34, 48, 50]],
        [[34, 35, 37, 39]],
        [[35, 36, 38, 39]],
        [[31, 32, 31, 32]]

    ]
    parse_status_mode(gun, obj_dict)


def mode_3(obj_dict):
    random_list = []
    cikle = 50
    while cikle > 0:
        y1 = random.randint(0, 62)
        y2 = random.randint(y1, 62)
        x1 = random.randint(0, 62)
        x2 = random.randint(x1, 62)
        random_list.append([[y1, y2, x1, x2]])

        cikle -= 1

    parse_status_mode(random_list, obj_dict)


def mode_4(obj_dict):
    pass


def mode_5(obj_dict):
    pass


def field_generator(sum_edge_cells, first_pos, render_step):
    """Создает списки с позицией в таблице и координатами ячеек"""
    field = []
    y_cor = first_pos[1]
    for y_pos in range(sum_edge_cells):
        x_cor = first_pos[0]
        row = []
        for x_pos in range(sum_edge_cells):
            row.append([[x_pos, y_pos], [x_cor, y_cor]])
            x_cor += render_step
        field.append(row)
        y_cor += render_step
    return field


def change_mode(cur_mode, cells_status_mode):
    """
    Принимет текущий режим статусов и отдает функцию,
    которая формирует статусы этого режимаю
    """
    for key, value in cells_status_mode.items():
        if key == cur_mode:
            return value
