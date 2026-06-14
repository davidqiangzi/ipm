import json

html_file = "/Users/dongchongchao/project/ipm/AI产品经理专业知识系统_v1.3_交互课件.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

try:
    prefix = "const DATA = "
    suffix = ";\nconst storageKey="
    data_json_str = content.split(prefix)[1].split(suffix)[0]
    data = json.loads(data_json_str)
except Exception as e:
    print("Could not find DATA object:", e)
    exit(1)

# 1. Update Quiz
data["quiz"].extend([
    {
        "q": "GraphRAG 相比于传统向量 RAG，在哪个场景下优势最明显？",
        "opts": ["精准查找某一条特定事实", "生成文章摘要", "跨文档、跨实体的宏观主题分析与总结", "翻译多语言文本"],
        "a": 2,
        "explain": "GraphRAG 建立实体连通性与社区摘要，特别擅长“连接点滴线索”的宏观推理。"
    },
    {
        "q": "在 Multi-Agent 架构中，Supervisor 模式的主要特征是？",
        "opts": ["多个 Agent 互相平等地进行头脑风暴", "一个高级 LLM 作为 Router 规划并下发任务给多个垂直子 Agent", "不需要任何编排", "使用单体大模型一次性完成所有事情"],
        "a": 1,
        "explain": "Supervisor 模式通过主管 Agent 将任务路由拆解，由专业子 Agent 分工执行。"
    },
    {
        "q": "MCP (Model Context Protocol) 协议中，不属于其核心对象的是？",
        "opts": ["Resources (资源)", "Prompts (模板)", "Tools (工具)", "Vectors (向量)"],
        "a": 3,
        "explain": "MCP 标准定义的核心是 Resources、Prompts 和 Tools，不包含底层 Vectors 的概念。"
    }
])

# 2. Update Flashcards
data["flashcards"].extend([
    {"term": "GraphRAG", "desc": "将文档预处理为实体与关系图谱，利用社区摘要提升宏观主题问答质量的检索技术。"},
    {"term": "Agentic RAG", "desc": "将线性检索转化为带有意图路由、多步检索、失败退回闭环能力的智能检索体系。"},
    {"term": "MCP 协议", "desc": "Model Context Protocol，打通模型与企业系统的标准化开放协议，定义 Resource、Prompt、Tool。"},
    {"term": "LLM-as-a-Judge", "desc": "使用强模型(如 GPT-4)基于打分 Schema 对系统输出进行多维自动化评测的方法论。"},
    {"term": "SLM", "desc": "小语言模型(Small Language Model)，适合在端侧或特定高频场景处理敏感数据，用算力摊销替代 Token 计费。"}
])

# 3. Update Projects
data["projects"].extend([
    {
        "name": "GraphRAG 知识图谱抽取",
        "tag": "v1.3 进阶",
        "desc": "上传 5 份研报，使用 GraphRAG 抽取实体与关系，生成可视化知识图谱，并评测对宏观问题的回答质量。"
    },
    {
        "name": "基于 MCP 的本地文件网关",
        "tag": "v1.3 进阶",
        "desc": "基于 Anthropic MCP 标准跑通一个本地 Server，向 Agent 暴露本地读取文件的 Resource 能力。"
    },
    {
        "name": "LLM-as-a-Judge 自动化评测流水线",
        "tag": "v1.3 进阶",
        "desc": "基于 100 条黄金测试集，用 RAGAS 框架的 Context Precision/Recall 跑出自动化评测基准分数。"
    }
])

# 4. Update Knowledge Map
if "v1.3 进阶前沿" not in data["knowledgeMapHtml"]:
    new_card = '<div class="map-card highlight"><h3>v1.3 进阶前沿</h3><p>GraphRAG 图谱检索、Multi-Agent 协同路由、MCP 标准企业网关接入、LLM-as-a-Judge 评测与 SLM 降级。</p></div>'
    data["knowledgeMapHtml"] = data["knowledgeMapHtml"].replace("</div>\n</div>", f"</div>\n  {new_card}\n</div>")

# Serialize back
new_json_str = json.dumps(data, ensure_ascii=False)
new_content = content.replace(data_json_str, new_json_str)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Extra sections successfully updated!")
