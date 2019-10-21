
class Arrow:
    up_arrow = {'img': 'https://icon-library.net/images/row-icon/row-icon-4.jpg', 'type': 9, 'deg': 0,
                'value': 'up'}
    down_arrow = {'img': 'https://icon-library.net/images/row-icon/row-icon-4.jpg', 'type': 9, 'deg': 180,
                  'value': 'down'}
    right_arrow = {'img': 'https://icon-library.net/images/row-icon/row-icon-4.jpg', 'type': 9, 'deg': 90,
                   'value': 'right'}
    left_arrow = {'img': 'https://icon-library.net/images/row-icon/row-icon-4.jpg', 'type': 9, 'deg': 270,
                  'value': 'left'}

    def all(self, map_row, unit):
        for row in map_row:
            if unit in row:
                row_len, map_row_len = len(row)-1, len(map_row)-1
                row_index, unit_index = map_row.index(row), row.index(unit)
                if row_index > 0:
                    map_row[row_index - 1][unit_index] = self.up_arrow
                if row_index < map_row_len:
                    map_row[row_index + 1][unit_index] = self.down_arrow
                if unit_index > 0:
                    map_row[row_index][unit_index - 1] = self.left_arrow
                if unit_index < row_len:
                    map_row[row_index][unit_index + 1] = self.right_arrow
        return map_row

    def clear(self, map_row):
        for row in map_row:
            row_index = map_row.index(row)
            if self.up_arrow in row:
                map_row[row_index][row.index(self.up_arrow)] = 0
            if self.down_arrow in row:
                map_row[row_index][row.index(self.down_arrow)] = 0
            if self.right_arrow in row:
                map_row[row_index][row.index(self.right_arrow)] = 0
            if self.left_arrow in row:
                map_row[row_index][row.index(self.left_arrow)] = 0
        return map_row


class Hero:
    unit_dict = {'img': 'https://pbs.twimg.com/media/DR1VUv5UMAAWsyC.png', 'type': 1, 'deg': 0, 'value': 'hero'}

    def move(self, way, map_row):
        for row in map_row:
            if self.unit_dict in row:
                row_index, unit_index = map_row.index(row), row.index(self.unit_dict)
                map_row[row_index][unit_index] = 0
                if way == 'up':
                    map_row[row_index - 1][unit_index] = self.unit_dict
                if way == 'down':
                    map_row[row_index + 1][unit_index] = self.unit_dict
                    break
                if way == 'left':
                    map_row[row_index][unit_index - 1] = self.unit_dict
                if way == 'right':
                    map_row[row_index][unit_index + 1] = self.unit_dict
        return map_row
