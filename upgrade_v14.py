import json
import re

input_file = "/Users/dongchongchao/project/ipm/AI产品经理专业知识系统_v1.3_交互课件.html"
output_file = "/Users/dongchongchao/project/ipm/AI产品经理专业知识系统_v1.4_交互课件.html"

with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

prefix = "const DATA = "
suffix = ";\nconst storageKey="
try:
    data_json_str = content.split(prefix)[1].split(suffix)[0]
    data = json.loads(data_json_str)
except Exception as e:
    print("Failed to parse JSON:", e)
    exit(1)

# --- 1. Update introHtml ---
data["introHtml"] = data.get("introHtml", "").replace("v1.3（进阶优化版）", "v1.4（前沿架构版）")
data["introHtml"] += "\n<blockquote>\n<p><strong>v1.4 前沿更新</strong>：补充 Generative UI 生成式界面、Realtime Multi-modal 实时多模态交互、TTS 音频内容产品化、Data Flywheel (RLHF/DPO) 数据回流闭环，以及 OWASP Guardrails 安全护栏机制。</p>\n</blockquote>\n"

# --- 2. Update Sections ---
section_updates = {
    9: {
        "html": """
<h3>9.6 v1.4 前沿：Generative UI 与流式渲染 (UI-on-the-fly)</h3>
<p>传统 AI 产品多采用 LUI (Language User Interface，即对话框)，但文字的交互效率低于 GUI (图形界面)。</p>
<h4>9.6.1 什么是 Generative UI</h4>
<p>Generative UI 是指模型不仅返回文字 JSON，更是根据用户意图，流式返回一个<strong>完整的、可交互的组件 (如 React/Vue Component)</strong>。例如，问“本月销售数据”，返回的不是一段解释，而是一张动态折线图，甚至图表上的点可以直接拖拽修改。</p>
<h4>9.6.2 产品设计落地点</h4>
<ul>
<li><strong>TTFT 与 TTI 优化</strong>：Time To First Token 只是吐字的延迟，Time To Interactive 才是组件可交互的延迟。需要设计流式加载骨架屏。</li>
<li><strong>混合交互</strong>：将 AI 组件自然地插入传统的 SaaS 仪表盘中，而非跳转到单独的聊天页面。</li>
</ul>
""",
        "plain": "\n\n    9.6 v1.4 前沿：Generative UI 与流式渲染 (UI-on-the-fly)\n\n传统 AI 产品多采用 LUI，但文字的交互效率低于 GUI。\n\n    9.6.1 什么是 Generative UI\n\nGenerative UI 是指模型根据用户意图，流式返回一个完整的、可交互的组件 (如动态图表、审批表单)。\n\n    9.6.2 产品设计落地点\n\n  TTFT 与 TTI 优化：设计流式加载骨架屏以掩盖组件渲染延迟。\n  混合交互：将 AI 组件自然地插入传统的 SaaS 仪表盘。\n"
    },
    11: {
        "html": """
<h3>11.5 v1.4 前沿：Data Flywheel (数据飞轮) 与 DPO 工程化</h3>
<p>顶级的 AI 产品靠数据护城河。如果不把用户在端侧的行为转化为微调资产，产品就永远只是一层套壳。</p>
<ul>
<li><strong>隐式反馈 (Implicit Feedback)</strong>：用户是否复制了答案？是否在生成的代码中删除了某几行？这代表了偏好。</li>
<li><strong>显式反馈 (Explicit Feedback)</strong>：点赞、踩、或者由用户手工订正（例如纠正 RAG 提取错误的金额）。</li>
<li><strong>DPO (直接偏好优化)</strong>：将以上“好答案”与“坏答案”构成一对 Preference Data，回流到后端直接微调模型或 Reranker 排序模型。</li>
</ul>
<h3>11.6 v1.4 前沿：AI Trust & Guardrails (安全护栏)</h3>
<p>企业应用最大的阻碍是不可控。必须基于 OWASP Top 10 标准引入安全护栏：</p>
<ul>
<li><strong>Prompt Injection 防御</strong>：使用单独的小模型 (如 NeMo Guardrails) 在输入端拦截“忽略上述指令”的越狱攻击。</li>
<li><strong>PII 敏感数据脱轨</strong>：把数据发给公有云 LLM 前，通过正则或 NER 将姓名/身份证掩码处理。</li>
</ul>
""",
        "plain": "\n\n    11.5 v1.4 前沿：Data Flywheel (数据飞轮) 与 DPO 工程化\n\n顶级的 AI 产品靠数据护城河。\n\n  隐式反馈：复制、停留时长、部分采纳等行为偏好。\n  显式反馈：人工订正和点踩。\n  DPO (直接偏好优化)：用好坏对数据回流微调模型或 Reranker。\n\n    11.6 v1.4 前沿：AI Trust & Guardrails (安全护栏)\n\n必须基于 OWASP 标准引入安全护栏：\n\n  Prompt Injection 防御：输入端拦截越狱攻击。\n  PII 敏感数据脱轨：向大模型发数据前的掩码处理。\n"
    },
    14: {
        "html": """
<h3>14.7 v1.4 前沿：Realtime Multi-modal (实时多模态 Agent)</h3>
<p>传统的“录音-ASR转文字-LLM思考-TTS转语音”具有瀑布流的高延迟，无法做真正的实时交互。</p>
<h4>14.7.1 WebRTC 与端到端语音</h4>
<p>OpenAI Realtime API 级别的架构，音频直接在网络协议中流式对传。PM 的核心指标：将端到端延迟控制在 500ms（人类舒适区）以内。</p>
<h4>14.7.2 VAD 与打断机制 (Interruption)</h4>
<p>系统必须能识别 VAD (Voice Activity Detection)，当用户突然插话时，需瞬间截断当前生成的 Token 队列并丢弃多余音频，重新生成。</p>

<h3>14.8 v1.4 前沿：TTS (文本转语音) 与音频产品化</h3>
<p>TTS 不仅是读字，更要有情感和资产安全性：</p>
<ul>
<li><strong>Zero-shot Voice Cloning (零样本声音克隆)</strong>：仅需 3-5 秒音频即可克隆音色，PM 必须设计鉴权验证防线，防止滥用。</li>
<li><strong>Emotion/Prosody Control (情感与韵律控制)</strong>：通过 Prompt 给大模型打上呼吸、停顿、笑声标签，取代传统的 SSML 标签调节。</li>
<li><strong>Streaming Chunk 策略</strong>：流式 TTS 需要将整段话切分成“句子块”下发，以掩盖生成延迟。</li>
</ul>
""",
        "plain": "\n\n    14.7 v1.4 前沿：Realtime Multi-modal (实时多模态 Agent)\n\n传统的 ASR-LLM-TTS 具有高延迟。\n\n    14.7.1 WebRTC 与端到端语音\n\n音频直接流式对传，将端到端延迟控制在 500ms 以内。\n\n    14.7.2 VAD 与打断机制\n\n识别 VAD，当用户突然插话时截断当前生成的 Token 队列。\n\n    14.8 v1.4 前沿：TTS (文本转语音) 与音频产品化\n\n  Zero-shot Voice Cloning：防范零样本克隆引发的欺诈风险。\n  Emotion/Prosody Control：基于文本和 Prompt 控制呼吸和情绪，取代 SSML。\n  Streaming Chunk 策略：流式 TTS 需要句子切分降低首包延迟。\n"
    },
    31: {
        "html": """
<h3>31.4 v1.4 新增前沿索引</h3>
<ul>
<li><strong>Generative UI</strong>: Vercel 官方技术文档《Generative UI with Next.js AI SDK》.</li>
<li><strong>Data Flywheel / DPO</strong>: Anthropic 论文《Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback》.</li>
<li><strong>Realtime API</strong>: OpenAI 官方开发者文档《Realtime API via WebRTC》.</li>
<li><strong>AI Safety & Guardrails</strong>: OWASP 基金会《Top 10 for Large Language Model Applications》及 NVIDIA《NeMo Guardrails Architecture》.</li>
</ul>
""",
        "plain": "\n\n    31.4 v1.4 新增前沿索引\n\n  Generative UI: Vercel 官方技术文档.\n  Data Flywheel / DPO: Anthropic 论文.\n  Realtime API: OpenAI 官方开发者文档.\n  AI Safety & Guardrails: OWASP 基金会规范.\n"
    }
}

for section in data["sections"]:
    sec_num = section.get("num")
    if sec_num in section_updates:
        section["html"] += section_updates[sec_num]["html"]
        section["plain"] += section_updates[sec_num]["plain"]
        print(f"Updated section {sec_num} for v1.4")

# --- 3. Update Quiz, Flashcards, Projects ---
data["quiz"].extend([
    {
        "q": "Generative UI (生成式界面) 的核心特征是什么？",
        "opts": ["模型回答的文字排版更漂亮", "模型直接根据意图流式返回一个完整的、可直接操作的结构化前端组件", "自动生成代码并部署网站", "让模型学会画图"],
        "a": 1,
        "explain": "Generative UI 使得 LUI 和 GUI 融合，突破了文字聊天框的限制，直接渲染可交互组件。"
    },
    {
        "q": "实时语音 Agent 系统中，VAD 的主要作用是什么？",
        "opts": ["翻译语言", "控制音量大小", "进行语音活动检测，从而判断用户是否在说话、是否需要触发系统打断 (Interruption)", "防止克隆人声"],
        "a": 2,
        "explain": "VAD (Voice Activity Detection) 负责检测人声，是实现多模态低延迟打断与并发控制的关键。"
    }
])

data["flashcards"].extend([
    {"term": "Generative UI", "desc": "生成式界面，模型流式下发渲染好的可操作前端组件（如动态表单），取代纯文字交互。"},
    {"term": "DPO / Data Flywheel", "desc": "直接偏好优化与数据飞轮，通过收集端侧的点赞/修改等偏好数据，反哺并微调模型，建立数据护城河。"},
    {"term": "VAD 打断机制", "desc": "Voice Activity Detection，在实时语音大模型中检测人声，实现用户插话时的即时打断与 Token 丢弃。"},
    {"term": "NeMo Guardrails", "desc": "NVIDIA 提出的企业级安全护栏框架，用于在输入和输出端防御提示词注入和信息越权。"},
    {"term": "Zero-shot TTS", "desc": "零样本语音生成与声音克隆，仅需极短的参考音频即可模拟发音人的音色。"}
])

data["projects"].extend([
    {
        "name": "Generative UI 意图组件 Demo",
        "tag": "v1.4 前沿",
        "desc": "基于 Vercel AI SDK，设计当用户提问“查一下张三请假单”时，直接渲染出可审批交互卡片的场景。"
    },
    {
        "name": "Data Flywheel 数据回流管线设计",
        "tag": "v1.4 前沿",
        "desc": "为内部知识库产品设计全套“隐式反馈+显式修正台”埋点，并规划其作为 Reranker 微调数据的落地方案。"
    }
])

# --- 4. Update Knowledge Map ---
new_card_v14 = '<div class="map-card highlight"><h3>v1.4 前沿交互与护城河</h3><p>Generative UI 动态组件、Realtime WebRTC 语音打断、Streaming TTS 克隆、DPO 数据飞轮回流与 Guardrails 安全护栏。</p></div>'
data["knowledgeMapHtml"] = data["knowledgeMapHtml"].replace("</div>\n</div>", f"</div>\n  {new_card_v14}\n</div>")

# --- Serialize back to content ---
new_json_str = json.dumps(data, ensure_ascii=False)
content = content.replace(data_json_str, new_json_str)

# --- 5. Update HTML UI Tweaks ---
content = content.replace("<title>AI产品经理专业知识系统 v1.3 交互课件</title>", "<title>AI产品经理专业知识系统 v1.4 交互课件</title>")
content = content.replace("v1.3 进阶优化版", "v1.4 前沿架构版")
content = content.replace('<button data-tab="v13">v1.3 进阶</button>', '<button data-tab="v13">v1.3 进阶</button><button data-tab="v14">v1.4 前沿</button>')

# badgeLabel update
old_badge = "function badgeLabel(s){if([5,7,8,10,31].includes(s.num))return 'v1.3'; if(s.num>=20&&s.num<=25)return 'v1.1'; if(s.num>=26&&s.num<=28)return 'v1.2'; if(s.num>=29&&s.num<=30)return '总结'; return ''}"
new_badge = "function badgeLabel(s){if([9,11,14].includes(s.num))return 'v1.4'; if([5,7,8,10,31].includes(s.num))return 'v1.3'; if(s.num>=20&&s.num<=25)return 'v1.1'; if(s.num>=26&&s.num<=28)return 'v1.2'; if(s.num>=29&&s.num<=30)return '总结'; return ''}"
content = content.replace(old_badge, new_badge)

# renderV14 update
render_v14_code = """function renderV14(){const items=DATA.sections.filter(s=>[9,11,14,31].includes(s.num));contentEl.innerHTML='<article class="article"><h2>v1.4 前沿内容</h2><div class="card-grid">'+items.map(s=>`<div class="card"><h3>${s.num}. ${s.title}</h3><p><span class="badge">v1.4</span> 前沿：点击左侧目录进入章节末尾查看。</p><button class="primary" onclick="openSection(${s.num})">打开章节</button></div>`).join('')+'</div></article>'}"""
content = content.replace("function renderQuiz()", render_v14_code + "\nfunction renderQuiz()")

# renderCurrentTab update
content = content.replace("if(currentTab==='v13')renderV13();", "if(currentTab==='v13')renderV13();if(currentTab==='v14')renderV14();")

with open(output_file, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully generated {output_file}")
