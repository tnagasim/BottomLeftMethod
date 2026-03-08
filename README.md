# BottomLeftMethod

ボトムレフト法 (Bottom-Left Method) による多次元矩形パッキングアルゴリズムの実装。

## 概要

ボトムレフト法とは、矩形を収納箱（ケース）に詰める際に、可能な限り「左下（低次元方向）」に配置しようとするヒューリスティックアルゴリズムです。2次元だけでなく、3次元以上にも対応しています。

## 使用方法

```python
from bottom_left2 import Case, BottomLeftMethod

# 10x10 のケースに矩形を詰める
case = Case.create([10, 10])
method = BottomLeftMethod(case)

# 矩形を順番に配置
case.stack([3, 4], method)  # 3x4 の矩形を配置
case.stack([5, 2], method)  # 5x2 の矩形を配置

print(case.stacked)  # 配置済み矩形の座標を出力
```

## クラス構成

| クラス             | 説明                               |
| ------------------ | ---------------------------------- |
| `Rect`             | 矩形（配置候補・配置済み矩形を表す） |
| `Case`             | 収納箱（ケース）を表す             |
| `BottomLeftMethod` | ボトムレフト法の配置アルゴリズム   |

詳細な設計は [design.md](design.md) を参照してください。

## インストール

```bash
pip install -r requirements.txt
```

## 依存ライブラリ

- `numpy` - 多次元配列による座標・矩形演算
- `itertools` - 順列生成（標準ライブラリ）
- `dataclasses` - データクラスの定義（標準ライブラリ）

## テスト

```bash
pytest
```
