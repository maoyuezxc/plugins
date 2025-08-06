import pcbnew
from pcbnew import VECTOR2I


def place():
    board = pcbnew.GetBoard()
    col_num = 52
    x_step = 5  # in mm
    y_step = 5  # in mm

    # ref_footprint = board.FindFootprintByReference("D1")

    for i in range(1, 2681):
        print(f"D{i}")
        fp = board.FindFootprintByReference(f"D{i}")
        if fp is None:
            continue

        if i % col_num == 0:
            m = i // col_num
            if m % 2 == 1:
                fp.SetOrientation(pcbnew.ANGLE_180)
            else:
                fp.SetOrientation(pcbnew.ANGLE_0)
            continue

        if i // col_num % 2 == 0:
            fp.SetOrientation(pcbnew.ANGLE_180)
        else:
            fp.SetOrientation(pcbnew.ANGLE_0)

    pcbnew.Refresh()
