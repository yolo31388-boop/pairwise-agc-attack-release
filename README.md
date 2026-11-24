# pairwise-agc-attack-release

## 领域

游戏、图形与多媒体

## 主题

自动增益攻击释放

## 说明

时间按秒、跨块累积与离线预热。

初始状态下 `media/agc_attack_release.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
