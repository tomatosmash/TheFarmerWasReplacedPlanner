"""
编程农场 - 6×6 简单种植
目标：收草（干草）、木材（树）、胡萝卜
"""

WORLD_SIZE = get_world_size()


# ============================================================
# 移动
# ============================================================

def move_to(x, y):
    """移动到 (x, y)，走最短路径"""
    cx, cy = get_pos_x(), get_pos_y()
    dx = (x - cx) % WORLD_SIZE
    if dx > WORLD_SIZE // 2:
        for _ in range(WORLD_SIZE - dx):
            move(West)
    else:
        for _ in range(dx):
            move(East)
    dy = (y - cy) % WORLD_SIZE
    if dy > WORLD_SIZE // 2:
        for _ in range(WORLD_SIZE - dy):
            move(South)
    else:
        for _ in range(dy):
            move(North)


def for_each_tile(action):
    """遍历所有格子"""
    for x in range(WORLD_SIZE):
        for y in range(WORLD_SIZE):
            move_to(x, y)
            action(x, y)


# ============================================================
# 种植与收获
# ============================================================

def farm():
    """遍历所有格子：收获成熟作物并重新种植"""
    def tile(x, y):
        entity = get_entity_type()

        # 如果有成熟作物就收获
        if entity != None and can_harvest():
            harvest()

        # 棋盘格：偶数位种树（木材），奇数位种胡萝卜
        if (x + y) % 2 == 0:
            # 树 — 需要草地（树在耕地上也能种，但草地更好管理）
            if get_entity_type() == None or get_entity_type() != Entities.Tree:
                if get_ground_type() == Grounds.Soil:
                    till()  # 切回草地
                plant(Entities.Tree)
        else:
            # 胡萝卜 — 需要耕地
            if get_ground_type() != Grounds.Soil:
                till()  # 耕地
            if get_entity_type() == None or get_entity_type() != Entities.Carrot:
                plant(Entities.Carrot)

        # 浇水
        if get_water() < 0.5:
            use_item(Items.Water)

    for_each_tile(tile)


# ============================================================
# 主循环
# ============================================================

while True:
    farm()
