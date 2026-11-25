# Rebuttal-Skills

[English](README.md) · **简体中文**  
[![MIT License](https://img.shields.io/badge/License-MIT-28613c)](LICENSE) [![GitHub Stars](https://img.shields.io/github/stars/Jurio0304/Rebuttal-Skills?style=social)](https://github.com/Jurio0304/Rebuttal-Skills/stargazers)

我把自己在 ICML、NeurIPS 和 ICLR 写 rebuttal 的亲身经验整理成了这个 Skill。这三次投稿在讨论后的审稿总分分别提高了 **4 分、4 分和 3 分**。为了让它也能用在其他研究方向上，我又参考了 **330 篇 ICLR 高提分投稿**的公开讨论。

我拿到评审意见后，一般先弄清楚每个人对论文的哪一点还有疑虑。同样一句“请补一个 baseline”，有人关心比较是否公平，有人想知道这个方法在真实使用中值不值得。我把从读评审、选实验到动笔回复的这段过程也放进了 Skill 里。

[我的投稿经历](#我的-rebuttal-经历) · [八个阶段](#八个阶段) · [安装](#安装) · [使用示例](#使用示例) · [完整演示](examples/sorting/README.md)

## 这个 Skill 是做什么的？

它可以在 Codex 或 Claude Code 里陪你走完一次 rebuttal。把投稿版论文、评审意见和当届会议的回复要求放在论文工作区，先让它逐人梳理问题，和你一起定实验，再拿实际结果写回复。如果已经写好了，也可以直接让它做一次模拟复审。

我自己尤其看重两件事。第一，回复要有作者的判断。主结果站得住，就把结论和比较条件写清楚；某个次要条件下没有提升，就在那一问里如实交代。没必要让一篇有贡献的工作读起来像是在反复为自己辩解。第二，交稿前值得站到对面读一遍。我会为每位审稿人单独开一个子代理，只给它本人的原评和对应回复，看它读完以后究竟还有哪一问没得到回答。[写作指南](skills/rebuttal/references/writing.md) · [三位模拟审稿人的实际回复](examples/sorting/04-panel.md)

## 我的 Rebuttal 经历

| 投稿 | 初评 | Rebuttal 后 | 总分变化 | 均分变化 | 结果与去向 |
| --- | --- | --- | ---: | ---: | --- |
| ICML | ${\color{#C73746}2} / {\color{#C73746}3} / {\color{#C73746}3} / {\color{#C73746}3}$ | ${\color{#C73746}3} / {\color{#C73746}3} / {\color{#168348}4} / {\color{#168348}5}$ | ${\color{#168348}+4}$ | 2.75 → 3.75 (${\color{#168348}+1.00}$) | 拒稿后修订，转投 NeurIPS |
| NeurIPS | ${\color{#C73746}2} / {\color{#C73746}3} / {\color{#C73746}3}$ | ${\color{#168348}4} / {\color{#168348}4} / {\color{#168348}4}$ | ${\color{#168348}+4}$ | 2.67 → 4.00 (${\color{#168348}+1.33}$) | **录用为 Poster** |
| ICLR | ${\color{#C73746}2} / {\color{#C73746}2} / {\color{#168348}3}$ | ${\color{#168348}3} / {\color{#168348}3} / {\color{#168348}4}$ | ${\color{#168348}+3}$ | 2.33 → 3.33 (${\color{#168348}+1.00}$) | Submission，Top 0.7~3.5% |

<sub>评分按各会当届量表着色：红色表示倾向拒稿，绿色表示倾向接收。ICML 和 NeurIPS 的 3 分偏拒，ICLR 的 3 分偏收。均分保留两位小数。</sub>

前两行是同一项工作：ICML 那一轮，有位审稿人从 3 分改到 5 分，也有一位读完回复后维持 3 分，虽然平均分提高一分但仍处于borderline，最终被拒😮‍💨；后来修订、转投 NeurIPS，三位审稿人最终总分提高4分录取，最难说服的2分审稿人完整re了三轮；ICLR首次投稿初分223，Rebuttal后一位2分审稿人直接提高至4分🤩，虽然ICLR可以叠楼，但对于3位审稿人本次Rebuttal均只回复了一轮5k字符以内，在我看来叠楼虽然看起来丰富工作量大，但简要地回应审稿人最核心的疑虑或许更高效且审稿友好。

## 八个阶段

仓库里只有一个需要安装的技能 `rebuttal`。下面是它内部的八个阶段，每一步都可以单独用。如果你只想讨论实验方案，可以停在第 2 步；如果刚收到二轮追问，从第 6 步开始就行。

| 阶段 | 什么时候用 | 具体能拿到什么 |
| --- | --- | --- |
| [1. 读稿与分析初评](skills/rebuttal/references/stages/01-intake.md) | 刚收到 reviews | 按原问题编号列出每个人认可什么、质疑什么，以及论文里已经有哪些证据。 |
| [2. 安排实验和回复](skills/rebuttal/references/stages/02-plan.md) | 需要决定先做什么 | 一份按优先级排列的方案，说明哪些问题可直接澄清，哪些值得补对照，一次实验能回答哪几位审稿人。 |
| [3. 整合结果](skills/rebuttal/references/stages/03-results.md) | 自己或合作者交回结果 | 核对协议、数值和比较对象，决定哪些主张可以写得更明确，哪些需要限定条件。 |
| [4. 写逐点回复](skills/rebuttal/references/stages/04-response.md) | 证据基本齐了 | 按 reviewer 的原顺序组织可直接粘贴的正文，兼顾本届会议的篇幅、链接和改稿要求。 |
| [5. 模拟审稿与返工](skills/rebuttal/references/stages/05-simulation.md) | 已经有一版草稿 | 每位模拟 reviewer 独立给出跟帖、未解决的问题和改分意愿。作者补充说明后，可以只请对应的 reviewer 再读一次。 |
| [6. 跟进真实讨论](skills/rebuttal/references/stages/06-discussion.md) | 收到 reviewer 或 AC 的新消息 | 围绕对方这一次还在问的问题回复，分别记录已经认可的内容、改分意向和平台实际评分。 |
| [7. 写全局回复](skills/rebuttal/references/stages/07-global.md) | 讨论临近结束 | 给 AC 一份便于判断的总结：几个共性问题、最重要的新证据、审稿人的真实反馈，以及仍有分歧的地方。 |
| [8. 修改论文](skills/rebuttal/references/stages/08-revision.md) | 讨论期允许改稿，或准备终稿 | 把承诺逐条对应到正文、表格或附录的位置，按你的要求给出修改建议或实际改稿。 |

## 安装

### 方式一：在 Codex 里用

先把这个仓库克隆到本机。下面统一放在用户主目录；如果你已经克隆过，后面的命令换成你自己的路径即可。

```sh
git clone https://github.com/Jurio0304/Rebuttal-Skills.git "$HOME/Rebuttal-Skills"
```

接下来**进入你的论文工作区**，在该目录执行下面的命令。

```sh
src="$HOME/Rebuttal-Skills/skills/rebuttal"
dest=".agents/skills/rebuttal"
mkdir -p .agents/skills
if [ -f "$src/SKILL.md" ] && [ ! -e "$dest" ] && [ ! -L "$dest" ]; then
  ln -s "$src" "$dest"
fi
```

在这个论文工作区新开 Codex 会话，输入 `$rebuttal` 和你的任务。安装的是包含 `SKILL.md` 的 `skills/rebuttal` 子目录。上面的命令会保留已有安装。

### 方式二：在 Claude Code 里用

使用同一份本地克隆。**在论文工作区**执行下面的命令。

```sh
src="$HOME/Rebuttal-Skills/skills/rebuttal"
dest=".claude/skills/rebuttal"
mkdir -p .claude/skills
if [ -f "$src/SKILL.md" ] && [ ! -e "$dest" ] && [ ! -L "$dest" ]; then
  ln -s "$src" "$dest"
fi
```

新开 Claude Code 会话，输入 `/rebuttal` 和你的任务。以上两种方式使用符号链接，以后更新本地克隆，论文工作区会读到同一份新版技能。当前已实测 Codex 的技能发现和独立模拟复审；Claude Code 提供项目级安装说明。[验证记录](evals/README.md#local-verification)

### 方式三：请本地助手代装

在论文工作区打开 Codex 或 Claude Code，把下面这句话发给它，填上你实际用的客户端就行。

> 帮我安装 https://github.com/Jurio0304/Rebuttal-Skills 里的 rebuttal 技能。我用的是 Codex。请在当前项目对应的技能目录下安装仓库的 skills/rebuttal 子目录。如果已经安装，告诉我现有位置；完成后给我一条调用示例。

### 方式四：先在普通聊天里试用

把[技能入口](skills/rebuttal/SKILL.md)和你需要的阶段指南贴给助手，再提供该任务用得到的稿件节选或评审意见。想试模拟复审的话，为每位 reviewer 单独新开一个对话。也可以直接用仓库里的[虚构排序论文](examples/sorting/README.md)走一遍，看看这个流程适不适合自己。

## 使用示例

下面这些指令可以直接改成你自己的。Codex 用 `$rebuttal` 开头，Claude Code 用 `/rebuttal`。用中文讨论策略、最后输出英文回复也可以。

**1. 刚收到评审，先读懂问题。**

> $rebuttal 先读投稿版、附录和三份 review。按每个人的原问题顺序，告诉我哪些问题原稿里已经答过、哪些地方确实缺证据。把 AC 最可能需要权衡的两处分歧指出来。先不要写英文回复。

**2. 算力只够做一组对照。**

> R1 怀疑提升来自更长的训练，R2 觉得我们的基线偏弱。结合现有日志和这两份评审，帮我选一个最值得跑的对照。写清楚哪些条件要固定、这个结果各能回答他们什么，以及跑不完时还能用哪些已有证据回复。

**3. 有好结果，也有持平的条件。**

> 这张表是我们刚做完的匹配实验。请帮我写给 R2 的英文回复。先把主设置下相对基线的收益讲清楚，再用一句话交代小数据设置持平。保留原来的 Q2 编号和表里的不确定性，正文控制在我贴出的字符上限内。

**4. 把自己写好的草稿交给模拟审稿人。**

> 三份草稿都写好了。请为三位 reviewer 分别开独立子代理，各自只读自己的原评和对应回复。先像真人一样回一个跟帖，再告诉我哪一点已被说服、还想追问什么、是否愿意改分，以及理由。把最值得我改的段落标出来。

**5. 二轮追问，只回新增的部分。**

> 接着 R1 的真实跟帖往下写。他已经认可训练预算匹配，只对表里均值的计算方式有疑问。根据我提供的统计口径，给他一段简短英文回复。上一轮已经讲清的实验设计就不用再展开了。

**6. 写给 AC，并兑现修稿承诺。**

> 请根据已发回复和真实跟帖，起草一段给 AC 的 Global Response。R2 说愿意提分，但页面分数还没变，请准确转述。另给我一份修稿清单，标出该改哪一段、哪张表，以及哪些地方已经改好。模拟审稿的意见留在内部。

## 依据与来源

**我的投稿复盘。** 整理时我把初评、当时的实验计划、正式回复、后续讨论和稿件修改放在一起看。这样能保留下来的，除了最后怎么写，还有当时为什么值得做这个实验，或者为什么用原稿里的一段说明就足以回答问题。公开教程用的是另行构造的示例。[完整教程](examples/sorting/README.md)

**ICLR 的公开讨论。** 我以讨论期审稿总分净增至少 3 分为条件，核对了 330 篇 ICLR 投稿。在采用的时间窗口里，275 篇能读到作者回复，共 2,295 条。另外从 266 篇各取一段，借助模型逐段归纳写法。例如，有的回复把效果持平和运行时间改善放在一起报告，让读者一下就看懂改善发生在哪个指标上。这些观察用来打磨技能里的写作建议；项目对照效果另有留出题评测。[讨论研究与统计口径](skills/rebuttal/references/discussion-patterns.md) · [评测记录](evals/README.md)

**当届会议规则和公开项目。** 字符上限、是否允许附链接、讨论期能否修稿，都按年份和 track 查。首版整理了 ICML 2026、NeurIPS 2026 主会、ICLR 2027 和 AAAI-27；我参考过的开源项目及具体版本也保留在来源文件中。[会议规则卡](skills/rebuttal/references/venues) · [来源与许可](SOURCES.md)

## 更新记录（Changelog）

**2026-11-25 · 初版。** 完成八阶段技能、四份会议规则卡和中英文使用说明。加入一位 reviewer 对应一个子代理的模拟复审，以及一套从三份初评、作者返工到 AC 总结和修改论文的完整示例。[示例入口](examples/sorting/README.md)

欢迎把它用在你自己的 rebuttal 上。如果哪一步特别有用，可以给项目点个 Star。如果生成的某段回复读起来还是不像你自己写的，也欢迎带一个虚构例子开 issue 告诉我。[提交反馈](https://github.com/Jurio0304/Rebuttal-Skills/issues) · [贡献指南](CONTRIBUTING.md)

## 许可证（License）

项目原创内容采用 [MIT License](LICENSE)。

## 鸣谢

特别感谢研究者 [@956961](https://github.com/956961)。

也感谢以下开源项目。 [Awesome Rebuttal](https://github.com/xiongqi123123/awesome-rebuttal) · [ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) · [CCFA-Skills](https://github.com/mikubaka88/CCFA-Skills) · [CCF-A-Skills](https://github.com/kay-kuo/CCF-A-Skills) · [Rebuttal-Skill](https://github.com/TobiasLee/Rebuttal-Skill) · [Review2Rebuttal](https://github.com/Henryhe09/Review2Rebuttal)
