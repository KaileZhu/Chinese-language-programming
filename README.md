# 汉语言编程 — 海克斯棋（Hex）下棋机器人

> **课程**：汉语言编程 | **课题**：机器人下棋——海克斯棋  
> **成员**：张硕、张欣宇、姜滔 | **班级**：自动化 2003 班

## 项目简介

使用**汉语言编程工具**（Unity 可视化编程环境）与 **Python（AlphaZero 算法）** 混合编程，实现海克斯棋（Hex）对弈系统，支持人人对战和人机对战。

### 游戏规则

- 红蓝双方在 11×11 六边形棋盘交替落子
- 红方连通上下边界（纵向）即获胜
- 蓝方连通左右边界（横向）即获胜

---

## 项目结构

```
Chinese-language-programming/
├── README.md
├── .gitignore
│
├── src/                         # 源代码
│   ├── azalea/                  # AlphaZero Hex AI（Python）
│   │   ├── azalea/              # Python 包
│   │   │   ├── game/hex.py      # 游戏引擎（棋盘、规则、胜负判定）
│   │   │   ├── mcts.py          # 蒙特卡洛树搜索
│   │   │   ├── network.py       # ResNet 残差卷积网络
│   │   │   ├── policy.py        # 策略网络
│   │   │   ├── azalea_agent.py  # AI 智能体封装
│   │   │   └── ...
│   │   ├── config/              # 训练配置 + 预训练模型
│   │   ├── models/              # 训练好的策略权重
│   │   ├── tests/               # 单元测试
│   │   ├── setup.py
│   │   ├── train.py             # 训练入口
│   │   └── play.py              # 对弈入口
│   │
│   └── hanlang/                 # 汉语言程序（.han 源码）
│       ├── intro/               # 自我介绍程序
│       ├── demos/               # 功能测试程序（~35个）
│       └── hex/                 # 海克斯棋教学测程序
│
├── runtime/                     # 汉语言编程工具运行环境
│   ├── 汉语言编程.exe           # 编程编辑器
│   ├── 汉语言运行.exe           # 程序播放器
│   ├── ComInfo.exe              # 主程序
│   ├── Plugins/                 # 插件（大数运算、内存表）
│   └── ...
│
├── docs/                        # 文档与展示材料
│   ├── 综述.pptx
│   ├── 汇报演讲稿.txt
│   ├── videos/                  # 演示视频
│   ├── papers/                  # 程序文档
│   └── algorithm/               # AlphaZero 算法文档
│
└── deliverables/                # 最终提交物
    ├── PPT/                     # 小组汇报 PPT
    ├── 分享视频.mp4
    ├── 文档.pdf
    └── 代码-Python.zip
```

---

## 技术架构

### 汉语言部分（张欣宇）
- 棋盘 UI、棋子图片元件显示、鼠标交互
- 集合存储红/蓝/空三种棋子状态
- 深度优先搜索（DFS）检测连通胜利
- 全局变量控制玩家轮换

### Python AI 部分（张硕）
- 基于 **AlphaZero** 强化学习算法
- 状态空间：11×11×(2n+1) 张量表示
- **蒙特卡洛树搜索（MCTS）** 决策
- **ResNet** 残差网络（价值网络 + 策略网络）
- PyTorch + Numba JIT 加速
- 原作者：[Jarno Seppänen](https://github.com/jseppanen/azalea) (Apache-2.0)

### 教学测部分（姜滔）
- **教**：Hex 棋起源、规则、策略、算法
- **学**：汉语言小程序使用演示
- **测**：程序编写题目 + 人机对战体验

---

## 运行方式

### 汉语言程序
1. 打开 `runtime/汉语言编程.exe`（编辑器）或 `runtime/汉语言运行.exe`（播放器）
2. 通过文件菜单加载 `src/hanlang/` 下的 `.han` 文件

### Python AI
```bash
cd src/azalea

# 安装依赖
pip install -e .

# 人机对战（使用预训练模型）
python play.py

# 训练新模型
python train.py
```

---

## 致谢

- 课程老师 — 汉语言编程工具与教学指导
- [azalea](https://github.com/jseppanen/azalea) — AlphaZero Hex 参考实现
