import pcbnew


def hide_ref():
    board = pcbnew.GetBoard()

    count = 0

    for footprint in board.GetFootprints():
        ref_text = footprint.Reference()
        if ref_text.IsVisible():
            ref_text.SetVisible(False)
            count += 1

    pcbnew.Refresh()
    print(f"已隐藏 {count} 个 footprint 的位号。")
