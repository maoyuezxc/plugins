import pcbnew


def find_edge(y_target: int, board: pcbnew.BOARD):
    """
    find edge cuts in specified y value according to a footprint of reference
    """

    edge_cuts = board.GetDrawings()
    intersections = []

    for d in edge_cuts:
        if d.GetLayer() != pcbnew.Edge_Cuts:
            continue
        shape = d.GetShape()
        if shape == pcbnew.SHAPE_T_SEGMENT:
            start = d.GetStart()
            end = d.GetEnd()
            y1, y2 = start.y, end.y

            # 排除水平线段
            if y1 == y2:
                continue

            if min(y1, y2) <= y_target <= max(y1, y2):
                x1, x2 = start.x, end.x
                t = (y_target - y1) / (y2 - y1)
                x_intersect = x1 + t * (x2 - x1)
                intersections.append(pcbnew.ToMM(x_intersect))

    intersections.sort()
    print("交点 X 坐标 (mm):", intersections)
    return intersections


def is_out_of_boundary(position_X: int, boundary: list[int]):

    return position_X < boundary[0] or position_X > boundary[1]
