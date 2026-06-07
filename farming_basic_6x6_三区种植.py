# ============================================================
# 编程农场 - 6x6 三区种植
# 目标：草（干草）、木材（树）、胡萝卜
# 布局：(x+y)%3 分区 -> 树12格 / 胡萝卜12格 / 草12格
# ============================================================

WORLD_SIZE = get_world_size()


# ============================================================
# 移动
# ============================================================

def move_to(x, y):
    # 移动到 (x, y)，走最短路径
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
    # 遍历所有格子
    for x in range(WORLD_SIZE):
        for y in range(WORLD_SIZE):
            move_to(x, y)
            action(x, y)


# ============================================================
# 种植与收获
# ============================================================

def farm():
    # 遍历所有格子：按分区管理
    def tile(x, y):
        zone = (x + y) % 3
        entity = get_entity_type()

        # 先收成熟的
        if entity != None and can_harvest():
            harvest()

        if zone == 0:
            # 树区 — 草地，棋盘格天然无相邻
            if entity != Entities.Tree:
                if get_ground_type() == Grounds.Soil:
                    till()  # 切回草地
                plant(Entities.Tree)

        elif zone == 1:
            # 胡萝卜区 — 耕地
            if get_ground_type() != Grounds.Soil:
                till()
            if entity != Entities.Carrot:
                plant(Entities.Carrot)

        else:
            # 草区 — 保持草地，不种东西，让草自然生长
            if get_ground_type() == Grounds.Soil:
                till()  # 切回草地
            # 不种植，草会自动长出来

        # 浇水
        if get_water() < 0.5:
            use_item(Items.Water)

    for_each_tile(tile)


# ============================================================
# 主循环
# ============================================================

while True:
    farm()
