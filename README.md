# 🕹️ AI CAT CLAW | 体感猫猫抓娃娃机

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Matter.js](https://img.shields.io/badge/Physics-Matter.js-ff00ff.svg)
![MediaPipe](https://img.shields.io/badge/Vision-MediaPipe-00ffff.svg)

> 一个完全运行在浏览器中的赛博朋克风体感抓娃娃机。不用摇杆，不用按钮，**用你的双手在空中直接掌控全局**。

---

## ✨ 核心亮点 (Features)

* 🖐️ **AI 视觉引擎驱动**：接入 Google MediaPipe 手势识别模型。无需任何额外硬件，只需打开电脑摄像头，通过**食指平移**控制爪子位置，**双指捏合**触发下爪！
* 🐈 **原生几何物理系统**：放弃传统的死板贴图！所有的猫猫全部由 Matter.js 原生几何体（复合多边形）动态生成。它们不仅会翻滚、堆叠，甚至还会互相卡位，为你带来最真实的物理阻力。
* 😈 **真实的“老板黑心算法”**：内置动态抓力系统（可调节的机器良心度 Win Rate）。哪怕你抓得再准，系统也会在半空中进行概率判定。失败？猫猫当场滑落，真实还原街机厅里的心跳骤停！
* 📺 **PiP 画中画监控**：右下角内置实时传感器监控画面，骨骼节点红绿变色反馈，让你随时掌握 AI 的视觉判定状态。
* 🎮 **完整的街机体验**：带有一键暂停、一键重置、计分系统（Drop Zone 传感器）、计时器，并且接入了 `localStorage` 本地最高分持久化记录。

## 📸 游戏截图 (Screenshots)
<img width="1353" height="737" alt="image" src="https://github.com/user-attachments/assets/2070d2b8-df88-4cab-8f3a-1fc50392e96c" />
> 绿色圆点状态下为爪子进行移动。
<img width="1169" height="636" alt="image" src="https://github.com/user-attachments/assets/9bcef087-06ea-42a3-8e30-7f72e35cabbc" />
> 红色圆点状态下为‘下爪’。
<img width="1168" height="638" alt="image" src="https://github.com/user-attachments/assets/3dffe586-dcaf-42ec-89af-7f05a90dae63" />


*(提示：建议在这里放一张你玩游戏时的动图 GIF 或截图)*
![Gameplay Placeholder](https://via.placeholder.com/640x360/1e1e24/ff00ff?text=Upload+Your+Gameplay+GIF+Here)

## 🛠️ 技术栈 (Tech Stack)

* **前端骨架**：HTML5 Canvas + Vanilla JavaScript
* **视觉中枢**：[@mediapipe/tasks-vision](https://developers.google.com/mediapipe) (HandLandmarker)
* **物理引擎**：[Matter.js](https://brm.io/matter-js/) (2D Rigid Body Physics)
* **UI 风格**：Retro Pixel Art Typography (Google Fonts: Press Start 2P)

## 🚀 快速开始 (Quick Start)

由于现代浏览器（如 Chrome）的安全策略机制，调用摄像头 API 必须在安全上下文（HTTPS 或 Localhost）中运行。
