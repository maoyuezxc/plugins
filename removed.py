import pcbnew


def remove_diodes():

    brd = pcbnew.GetBoard()
    for i in range(25, 134, 6):
        fp = brd.FindFootprintByReference(f"D{i}")
        brd.Remove(fp)

    pcbnew.Refresh()
