import pcbnew

board = pcbnew.GetBoard()
count = 0

for drawing in board.GetDrawings():
    if isinstance(drawing, pcbnew.PCB_TEXT) and drawing.IsVisible():
        drawing.SetVisible(False)
        count += 1

pcbnew.Refresh()
print(f"已隐藏 {count} 个自由文本对象（如 D155）。")
