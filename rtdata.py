import pcbnew
from pcbnew import VECTOR2I


def create_track(
    pad1: pcbnew.PAD,
    pad2: pcbnew.PAD,
    board: pcbnew.BOARD,
    layer=pcbnew.F_Cu,
    width=0.15,
):
    """
    Connect two pads with a track on the specified layer.

    Args:
        pad1: First pad to connect
        pad2: Second pad to connect
        layer: Board layer to place the track on (default: F.Cu)
        width: Track width in milimeter (default: 0.2mm)
    """

    pad_distance_x = int(1.69 * 1000000)
    pad_distance_y = int(0.85 * 1000000)

    delta_len = int(1.868 * 1000000)

    start = pad1.GetPosition()
    end = pad2.GetPosition()

    # create  tracks

    track0 = pcbnew.PCB_TRACK(board)
    track0.SetStart(start)
    track0.SetEnd(start + VECTOR2I(int((pad_distance_x - pad_distance_y) / 2), 0))
    track0.SetLayer(layer)
    track0.SetWidth(pcbnew.FromMM(width))

    track1 = pcbnew.PCB_TRACK(board)
    track1.SetStart(track0.GetEnd())
    track1.SetEnd(track0.GetEnd() + VECTOR2I(pad_distance_y, -pad_distance_y))
    track1.SetLayer(layer)
    track1.SetWidth(pcbnew.FromMM(width))

    track2 = pcbnew.PCB_TRACK(board)
    track2.SetStart(track1.GetEnd())
    track2.SetEnd(end)
    track2.SetLayer(layer)
    track2.SetWidth(pcbnew.FromMM(width))

    board.Add(track0)
    board.Add(track1)
    board.Add(track2)


def create_track_row_end(
    pad1: pcbnew.PAD,
    pad2: pcbnew.PAD,
    board: pcbnew.BOARD,
    layer=pcbnew.F_Cu,
    width=0.2,
):
    """
    Connect two pads with a track on the specified layer.

    Args:
        pad1: First pad to connect
        pad2: Second pad to connect
        layer: Board layer to place the track on (default: F.Cu)
        width: Track width in milimeter (default: 0.2mm)
    """

    deltax = int(1.2 * 1000000)
    deltay = int(1.2 * 1000000)

    start = pad1.GetPosition()
    end = pad2.GetPosition()

    # create  tracks

    track0 = pcbnew.PCB_TRACK(board)
    track0.SetStart(start)
    track0.SetEnd(start + VECTOR2I(deltax, deltay))
    track0.SetLayer(layer)
    track0.SetWidth(pcbnew.FromMM(width))
    track0.SetNet(pad1.GetNet())

    track1 = pcbnew.PCB_TRACK(board)
    track1.SetStart(track0.GetEnd())
    track1.SetEnd(track0.GetEnd() + VECTOR2I(0, 5000000 - 2 * deltax))
    track1.SetLayer(layer)
    track1.SetWidth(pcbnew.FromMM(width))
    track1.SetNet(pad1.GetNet())

    track2 = pcbnew.PCB_TRACK(board)
    track2.SetStart(track1.GetEnd())
    track2.SetEnd(end)
    track2.SetLayer(layer)
    track2.SetWidth(pcbnew.FromMM(width))
    track2.SetNet(pad1.GetNet())

    board.Add(track0)
    board.Add(track1)
    board.Add(track2)


def create_track_row_start(
    pad1: pcbnew.PAD,
    pad2: pcbnew.PAD,
    board: pcbnew.BOARD,
    layer=pcbnew.F_Cu,
    width=0.2,
):

    deltax = int(1.2 * 1000000)
    deltay = int(1.2 * 1000000)

    delta_len = int(1.868 * 1000000)

    start = pad1.GetPosition()
    end = pad2.GetPosition()

    # create  tracks

    track0 = pcbnew.PCB_TRACK(board)
    track0.SetStart(start)
    track0.SetEnd(start + VECTOR2I(-deltax, deltay))
    track0.SetLayer(layer)
    track0.SetWidth(pcbnew.FromMM(width))

    track1 = pcbnew.PCB_TRACK(board)
    track1.SetStart(track0.GetEnd())
    track1.SetEnd(track0.GetEnd() + VECTOR2I(0, 5000000 - 2 * deltax))
    track1.SetLayer(layer)
    track1.SetWidth(pcbnew.FromMM(width))

    track2 = pcbnew.PCB_TRACK(board)
    track2.SetStart(track1.GetEnd())
    track2.SetEnd(end)
    track2.SetLayer(layer)
    track2.SetWidth(pcbnew.FromMM(width))

    board.Add(track0)
    board.Add(track1)
    board.Add(track2)


def route():
    board = pcbnew.GetBoard()

    col_num = 52
    for i in range(1, 2682):
        if i % col_num == 0:
            continue
        fp1 = board.FindFootprintByReference(f"D{i}")
        fp2 = board.FindFootprintByReference(f"D{i+1}")
        if fp1 is None or fp2 is None:
            continue
        if i // col_num % 2 == 0:
            pad1 = fp1.FindPadByNumber("1")
            pad2 = fp2.FindPadByNumber("4")
        else:
            pad1 = fp1.FindPadByNumber("4")
            pad2 = fp2.FindPadByNumber("1")
        create_track(pad1, pad2, board)

    pcbnew.Refresh()
    # pcbnew.SaveBoard("your_board_modified.kicad_pcb", board)
