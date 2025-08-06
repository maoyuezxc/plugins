import pcbnew
from pcbnew import VECTOR2I

def place():
    board = pcbnew.GetBoard()
    col_num = 36
    x_step = 5 # in mm
    y_step = 5 # in mm

    ref_footprint = board.FindFootprintByReference("C1")

    for i in range(2,91):
        print(f"C{i}")
        fp = board.FindFootprintByReference(f"C{i}")
        
        offset = pcbnew.VECTOR2I_MM(x_step*35*((i-1)%2),y_step*(i-1))

        target_pos = ref_footprint.GetPosition() + offset
        fp.SetPosition(target_pos)

    pcbnew.Refresh()
    board.Save(board.GetFileName())
