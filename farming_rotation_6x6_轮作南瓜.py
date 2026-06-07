# ============================================================
# 编程农场 - 6x6 轮作种植
# 目标：草（干草）、木材（树）、胡萝卜、南瓜
# 策略：基础三区模式积累资源 → 全南瓜模式爆发 → 循环
# ============================================================

WORLD_SIZE = get_world_size()

# 南瓜阶段阈值：胡萝卜高于此数时切换到南瓜模式
CARROT_THRESHOLD = 150
# 预留胡萝卜：低于此数时回到基础模式积累
PUMPKIN_RESERVE = 50


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
# 基础模式：三区种植（树 + 胡萝卜 + 草）
# ============================================================

def farm_basic():
    def tile(x, y):
        zone = (x + y) % 3
        entity = get_entity_type()

        # 先收成熟的
        if entity != None and can_harvest():
            harvest()

        if zone == 0:
            # 树区 — 草地
            if entity != Entities.Tree:
                if get_ground_type() == Grounds.Soil:
                    till()
                plant(Entities.Tree)

        elif zone == 1:
            # 胡萝卜区 — 耕地
            if get_ground_type() != Grounds.Soil:
                till()
            if entity != Entities.Carrot:
                plant(Entities.Carrot)

        else:
            # 草区 — 保持草地，不种东西
            if get_ground_type() == Grounds.Soil:
                till()

        # 浇水
        if get_water() < 0.5:
            use_item(Items.Water)

    for_each_tile(tile)


# ============================================================
# 南瓜模式：全 6x6 巨型南瓜
# ============================================================

def setup_pumpkins():
    def tile(x, y):
        entity = get_entity_type()
        if entity != None and can_harvest():
            harvest()

        if get_ground_type() != Grounds.Soil:
            till()

        if get_entity_type() != Entities.Pumpkin:
            plant(Entities.Pumpkin)

        if get_water() < 0.5:
            use_item(Items.Water)

    for_each_tile(tile)


def maintain_pumpkins():
    # 维护南瓜田，返回 True 表示巨型南瓜已收获
    # 用列表包装避免 nonlocal
    withered = [0]

    def tile(x, y):
        entity = get_entity_type()

        if entity == Entities.Pumpkin:
            if can_harvest():
                # 成熟且健康，等待合并
                pass
            else:
                # 枯萎了，补种
                withered[0] = withered[0] + 1
                if get_ground_type() != Grounds.Soil:
                    till()
                plant(Entities.Pumpkin)

        elif entity == None:
            # 空位，补种
            withered[0] = withered[0] + 1
            if get_ground_type() != Grounds.Soil:
                till()
            plant(Entities.Pumpkin)

        else:
            # 其他植物，清除后补种
            if can_harvest():
                harvest()
            if get_ground_type() != Grounds.Soil:
                till()
            plant(Entities.Pumpkin)
            withered[0] = withered[0] + 1

        if get_water() < 0.5:
            use_item(Items.Water)

    for_each_tile(tile)

    # 全部健康且成熟 → 巨型南瓜已合并
    if withered[0] == 0:
        if can_harvest():
            harvest()
            return True

    return False


# ============================================================
# 主循环
# ============================================================

mode = "basic"

while True:
    carrot = num_items(Items.Carrot)

    if mode == "basic":
        if carrot >= CARROT_THRESHOLD:
            mode = "pumpkin"
            setup_pumpkins()
        else:
            farm_basic()

    else:
        done = maintain_pumpkins()

        if done:
            mode = "basic"

        # 重新读取胡萝卜数量（maintain 过程中有消耗）
        carrot = num_items(Items.Carrot)
        if carrot < PUMPKIN_RESERVE:
            mode = "basic"
