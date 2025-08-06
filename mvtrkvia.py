import pcbnew

board = pcbnew.GetBoard()

# 获取 GND 的 NetCode
target_net_name = "GND"
gnd_netcode = board.GetNetcodeFromNetname(target_net_name)

# 准备列表收集要删除的对象
to_remove = []

for item in board.GetTracks():
    netcode = item.GetNetCode()
    if netcode == gnd_netcode or netcode == 0:
        to_remove.append(item)

# 删除
for item in to_remove:
    board.Remove(item)

pcbnew.Refresh()
print(f"已删除 {len(to_remove)} 条 GND 或无网络的走线和过孔。")
