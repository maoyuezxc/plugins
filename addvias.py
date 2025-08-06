import pcbnew
from pcbnew import VECTOR2I


def display():
    print("add vias")


def addvias():
    board = pcbnew.GetBoard()
    offset = VECTOR2I(pcbnew.FromMM(0.425), pcbnew.FromMM(0))
    col_num = 52

    # for i in range(2, 158):
    #     fp = board.FindFootprintByReference(f"C{i}")
    #     if fp is None:
    #         continue
    #     pad = fp.FindPadByNumber("2")

    for i in range(1, 2682):

        fp1 = board.FindFootprintByReference(f"D{i}")
        if fp1 is None:
            continue

        pad = fp1.FindPadByNumber("3")

        pos_pad = pad.GetPosition()

        if i % col_num == 0:
            m = i // col_num
            if m % 2 == 1:
                pos_via = pos_pad + offset
            elif m % 2 == 0:
                pos_via = pos_pad - offset

        else:

            if i // col_num % 2 == 0:
                pos_via = pos_pad + offset
                pass
            else:
                pos_via = pos_pad - offset
                pass

        via = pcbnew.PCB_VIA(board)
        via.SetPosition(pos_via)
        via.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
        net_name = "GND"
        net = board.FindNet(net_name)
        via.SetNet(net)
        via.SetDrill(pcbnew.FromMM(0.3))
        via.SetWidth(pcbnew.FromMM(0.41))
        board.Add(via)

        track = pcbnew.PCB_TRACK(board)
        track.SetStart(pos_pad)
        track.SetEnd(pos_via)
        track.SetLayer(pcbnew.F_Cu)
        track.SetWidth(pcbnew.FromMils(15))
        board.Add(track)
        print(f"D{i}")

    pcbnew.Refresh()

    # for footprint in board.GetFootprints():
    #     if "C" in footprint.GetReference():
    #         pass
    #     elif "D" in footprint.GetReference():

    #         # set position
    #         pad = footprint.FindPadByNumber("2")
    #         pos_pad = pad.GetPosition()
    #         pos_via = pos_pad + offset
    #         via = pcbnew.PCB_VIA(board)
    #         via.SetPosition(pos_via)

    #         # set layer
    #         via.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)

    #         # set net
    #         net_name = "GND"
    #         net = board.FindNet(net_name)
    #         via.SetNet(net)

    #         # set hole size and diameter
    #         via.SetDrill(pcbnew.FromMM(0.3))
    #         via.SetWidth(pcbnew.FromMM(0.41))
    #         board.Add(via)

    #         # # connect gnd pin and  gnd via
    #         # track = pcbnew.PCB_TRACK(board)
    #         # track.SetStart(pos_pad)
    #         # track.SetEnd(pos_via)
    #         # track.SetLayer(pcbnew.F_Cu)
    #         # track.SetWidth(pcbnew.FromMils(10))
    #         # board.Add(track)


def vias4cap():
    board = pcbnew.GetBoard()
    offset = VECTOR2I(pcbnew.FromMM(0.425), pcbnew.FromMM(0))
    step = 6
    for i in range(18, 145, step):
        fp = board.FindFootprintByReference(f"C{i}")

        pad = fp.FindPadByNumber("2")

        pos_pad = pad.GetPosition()
        pos_via = pos_pad + offset

        via = pcbnew.PCB_VIA(board)
        via.SetPosition(pos_via)
        via.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
        net_name = "GND"
        net = board.FindNet(net_name)
        via.SetNet(net)
        via.SetDrill(pcbnew.FromMM(0.15))
        via.SetWidth(pcbnew.FromMM(0.35))
        board.Add(via)

        track = pcbnew.PCB_TRACK(board)
        track.SetStart(pos_pad)
        track.SetEnd(pos_via)
        track.SetLayer(pcbnew.F_Cu)
        track.SetWidth(pcbnew.FromMils(15))
        board.Add(track)
    pcbnew.Refresh()
