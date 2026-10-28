# TPS分析

## TPS与FPS的本质区别

- 镜头位置的区别
- 进而视野大小、关卡尺寸、动画特效等一系列具体的感观区别
- 从而带来大量的做法上的差异

## 视角

- TPP（Third Person Perspective）
  - TPP腰射
  - TPP肩射（OTS：Over-the-Shoulder 越肩视角瞄准）
- FPP（First Person Perspective）

**关键设计：TPP与FPP之间的切换**

- 向前推进镜头，某一帧切换FPP

## 表现

### TPP腰射

- 武器动画（抖动）与镜头抖动
- 动作与射击的结合

### TPP肩射

- 拉近镜头
  - 增加角色与枪械在镜头中的比例
  - 让出视野中心给予射击目标
  - 避免瞬切
- 对武器动画、角色动画、特效有更高要求
- 移动与射击状态切换的频率
  - 从关卡、怪物、战斗节奏上需要避免过频繁地切换
  - 移动与射击都可以保持较长的持续周期（遗迹2的节奏挺舒适）

### FPP

- 同FPS

需要设计游戏不同射击的比例，从而确定资源投入重心。

以遗迹2为例，取消了TPP腰射，点击射击自动切换到肩射模式。

### TPP与FPP的表现差异

#### FPP

- 关注武器本身的表现，至多增加弹出子弹与手部动画
- 枪械击发时，武器本身结构变化以及反作用到镜头的变化

#### TPP

- 核心参数：武器占屏幕的像素比
  - TPP腰射武器占屏幕的像素比：
  - TPP肩射武器占屏幕的像素比：
- 枪械操作时：
  - 武器本身结构变化占比变小
  - 后座力作用到镜头效果变弱
  - 需要重点强调后座力作用到角色模型的动画
  - 枪械相关的动作，需要结合视角、突出角色原则重新设计
  - 强化以下特效：
    - 开火特效
    - 弹道线
    - 命中特效
  - 纯写实的中规中矩的武器效果，可能天生不适配TPS游戏
- 镜头跟随
  - 绑定程度

### 关卡

- 关卡尺寸：
  - 等比放大
  - 会带来比例认识偏差，因此更多偏向于室外开阔场景，或大型室内空间
  - 因此题材上非绝对写实会更加适配

### 其他问题

- 枪口出的枪线，与镜头到准心连线的夹角问题
  - 遮挡标识
  - 弹道偏转
- 作为PvP的视角，存在信息不对称的情况，不适宜作为竞技PvP主视角（PUBG的赛事也多采用FPP）
  - 因此TPP下可能更多向娱乐化发展，而不是严肃竞技会好一些

### 总结

- TPP = 射击 + 动作
  - 需要同时做好枪械射击

## 参考作品

- 血猎：
- 全境封锁2全武器：https://youtu.be/FaAZPqJZuTg?si=jlPKtJQDy8fZiGsq
- What Rifle Foregrip is Best? Angled? Vertical? Handstop?：https://youtu.be/Jc3q8TjJp0c?si=Xh_rfIZzuDgs3jME
  - T.REX ARMS：是美国田纳西的战术装备公司旗下媒体频道，目前订阅约 **170 万**，风格：**偏理性工程派**，不是单纯爽拍射击；喜欢做长期、量化测试，拆解装备设计逻辑，很重视 "平民自卫" 而不是竞技射击。视频质感精良，制作水平在油管战术频道里属于第一梯队。
- OUTRIDERS - All Weapons [PC, 1440P]：https://youtu.be/qLoL1_h6UwQ?si=6za_NXaIuNPE45sw
- 【【WARFRAME/全B站最快最极限神速力高斯】速度的极致！！！神速力！！！】 https://www.bilibili.com/video/BV1dK411c7Bx/?share_source=copy_web&vd_source=9f961463c9a01b757af4c797623b7a52
- Firing All guns in Red Dead Redemption 2 (1st and 3rd person RDR2)：https://youtu.be/4vNDLbBHRKo?si=sSBsgumRlPuyyT-q
- Grand Theft Auto 5 - All Weapons in 3rd Person: https://youtu.be/UlzU3CEU9uk?si=Zt8kRY5iXdUKriKn
- Death Stranding - All Weapons & Equipment Showcase：https://youtu.be/_b4KFrsT2kM?si=sS9kz4kv9pubPbDO
- All Returnal Guns Ranked *One Weapon Is BY FAR The Best*：https://youtu.be/r6M70-3gjus?si=alAYTsNgn8SfGzUE
