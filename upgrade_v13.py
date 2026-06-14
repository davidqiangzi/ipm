import json

html_file = "/Users/dongchongchao/project/ipm/AI产品经理专业知识系统_v1.2.1_交互课件.html"
output_file = "/Users/dongchongchao/project/ipm/AI产品经理专业知识系统_v1.3_交互课件.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# Extract DATA json using string splits
try:
    prefix = "const DATA = "
    suffix = ";\nconst storageKey="
    data_json_str = content.split(prefix)[1].split(suffix)[0]
    data = json.loads(data_json_str)
except Exception as e:
    print("Could not find DATA object:", e)
    exit(1)

# Update introHtml
data["introHtml"] = data.get("introHtml", "").replace("v1.2.1（结构整理版）", "v1.3（进阶优化版）")
data["introHtml"] += "\n<blockquote>\n<p><strong>v1.3 进阶更新</strong>：补充 GraphRAG、Agentic RAG、Multi-Agent 协同、MCP 协议网关及 LLM-as-a-Judge 自动化评测规范。</p>\n</blockquote>\n"

# Define updates (HTML + Plain Text)
updates = {
    5: {
        "html": """
<h3>5.10 v1.3 进阶：GraphRAG 与 Agentic RAG</h3>
<h4>5.10.1 GraphRAG（知识图谱增强检索）</h4>
<p>传统 RAG 基于向量检索，在“大海捞针”提取事实时表现优异，但在处理<strong>宏观主题总结</strong>时往往缺乏跨文档实体关系的理解。</p>
<ul>
<li><strong>全局连通性</strong>：将非结构化文档预处理为实体与关系的知识图谱。</li>
<li><strong>社区摘要 (Community Summaries)</strong>：支持对图谱的子社区进行预汇总，提升宏观问题的召回质量。</li>
<li><strong>混合检索 (Hybrid RAG)</strong>：向量检索细粒度查询 + 知识图谱跨域推理 + 关键词检索特定名词。</li>
</ul>
<h4>5.10.2 Agentic RAG 动态路由机制</h4>
<p>传统 RAG 是线性单向的，Agentic RAG 将其转化为具有规划和工具调用的闭环：</p>
<ul>
<li><strong>查询路由 (Query Routing)</strong>：根据意图判断查向量库、SQL 或联网搜索。</li>
<li><strong>多步检索 (Multi-step Retrieval)</strong>：第一轮召回不充分时，自动改写 Query 发起二次检索。</li>
<li><strong>退回与降级</strong>：检索不到时提供兜底和追问建议。</li>
</ul>
""",
        "plain": "\n\n    5.10 v1.3 进阶：GraphRAG 与 Agentic RAG\n\n    5.10.1 GraphRAG（知识图谱增强检索）\n\n传统 RAG 基于向量检索，在“大海捞针”提取事实时表现优异，但在处理宏观主题总结时往往缺乏跨文档实体关系的理解。\n\n  全局连通性：将非结构化文档预处理为实体与关系的知识图谱。\n  社区摘要 (Community Summaries)：支持对图谱的子社区进行预汇总，提升宏观问题的召回质量。\n  混合检索 (Hybrid RAG)：向量检索细粒度查询 + 知识图谱跨域推理 + 关键词检索特定名词。\n\n    5.10.2 Agentic RAG 动态路由机制\n\n传统 RAG 是线性单向的，Agentic RAG 将其转化为具有规划和工具调用的闭环：\n\n  查询路由 (Query Routing)：根据意图判断查向量库、SQL 或联网搜索。\n  多步检索 (Multi-step Retrieval)：第一轮召回不充分时，自动改写 Query 发起二次检索。\n  退回与降级：检索不到时提供兜底和追问建议。\n"
    },
    7: {
        "html": """
<h3>7.8 v1.3 进阶：Multi-Agent 协同模式</h3>
<p>面对企业级复杂长流程，单体大模型容易遭遇“指令迷失”。多智能体协作（Multi-Agent）通过角色拆分与上下文隔离解决此问题。</p>
<h4>7.8.1 典型 Multi-Agent 架构</h4>
<ol>
<li><strong>Supervisor (主管-下属) 模式</strong>：一个高级 LLM 扮演 Router，拆解任务给多个垂直子 Agent，最后汇总。适合明确分工。</li>
<li><strong>Swarm / Peer-to-Peer 模式</strong>：多个 Agent 在虚拟环境中基于握手协议交互。适合头脑风暴或红蓝对抗。</li>
</ol>
<h4>7.8.2 状态机图与图工作流</h4>
<p>引入 LangGraph 等图架构概念。产品经理不仅要画流程图，更要画状态流转图，明确 State Variables 和 Edges。</p>
""",
        "plain": "\n\n    7.8 v1.3 进阶：Multi-Agent 协同模式\n\n面对企业级复杂长流程，单体大模型容易遭遇“指令迷失”。多智能体协作（Multi-Agent）通过角色拆分与上下文隔离解决此问题。\n\n    7.8.1 典型 Multi-Agent 架构\n\n1. Supervisor (主管-下属) 模式：一个高级 LLM 扮演 Router，拆解任务给多个垂直子 Agent，最后汇总。适合明确分工。\n2. Swarm / Peer-to-Peer 模式：多个 Agent 在虚拟环境中基于握手协议交互。适合头脑风暴或红蓝对抗。\n\n    7.8.2 状态机图与图工作流\n\n引入 LangGraph 等图架构概念。产品经理不仅要画流程图，更要画状态流转图，明确 State Variables 和 Edges。\n"
    },
    8: {
        "html": """
<h3>8.5 v1.3 进阶：MCP 协议与企业网关</h3>
<p>MCP (Model Context Protocol) 是打通模型与企业系统的标准化开放协议。</p>
<h4>8.5.1 企业级 MCP 的核心对象</h4>
<ul>
<li><strong>Resources (资源)</strong>: 提供本地/云端数据的只读访问。</li>
<li><strong>Prompts (模板)</strong>: 服务器端托管的可重用提示词。</li>
<li><strong>Tools (工具)</strong>: 模型可执行的操作（如提交 JIRA）。</li>
</ul>
<h4>8.5.2 安全治理设计要点</h4>
<ul>
<li><strong>身份鉴权</strong>：必须设计 User-Level 鉴权方案，Agent 仅继承当前用户权限。</li>
<li><strong>Human-in-the-loop</strong>：涉及写操作必须设计界面执行前二次确认 (Approval UX)。</li>
</ul>
""",
        "plain": "\n\n    8.5 v1.3 进阶：MCP 协议与企业网关\n\nMCP (Model Context Protocol) 是打通模型与企业系统的标准化开放协议。\n\n    8.5.1 企业级 MCP 的核心对象\n\n  Resources (资源): 提供本地/云端数据的只读访问。\n  Prompts (模板): 服务器端托管的可重用提示词。\n  Tools (工具): 模型可执行的操作（如提交 JIRA）。\n\n    8.5.2 安全治理设计要点\n\n  身份鉴权：必须设计 User-Level 鉴权方案，Agent 仅继承当前用户权限。\n  Human-in-the-loop：涉及写操作必须设计界面执行前二次确认 (Approval UX)。\n"
    },
    10: {
        "html": """
<h3>10.6 v1.3 进阶：LLM-as-a-Judge 与 SLM</h3>
<h4>10.6.1 LLM-as-a-Judge 落地规范</h4>
<p>人工验收成本高，使用强模型（GPT-4/Claude 3.5）做裁判是工业标配。</p>
<ul>
<li><strong>建立黄金测试集</strong>：100~500 个带标准规则的基础用例。</li>
<li><strong>多维度评分 Schema</strong>：包括准确性、完整性和安全性。</li>
<li><strong>RAGAS 评估指标</strong>：重点使用 Context Precision 和 Context Recall。</li>
</ul>
<h4>10.6.2 SLM (小语言模型) 端侧 ROI</h4>
<p>针对数据敏感或成本敏感的高频查询，采用本地 Llama 3 8B 等 SLM，配合置信度向大模型降级路由机制。ROI 测算从按 Token 计费转向硬件算力摊销。</p>
""",
        "plain": "\n\n    10.6 v1.3 进阶：LLM-as-a-Judge 与 SLM\n\n    10.6.1 LLM-as-a-Judge 落地规范\n\n人工验收成本高，使用强模型（GPT-4/Claude 3.5）做裁判是工业标配。\n\n  建立黄金测试集：100~500 个带标准规则的基础用例。\n  多维度评分 Schema：包括准确性、完整性和安全性。\n  RAGAS 评估指标：重点使用 Context Precision 和 Context Recall。\n\n    10.6.2 SLM (小语言模型) 端侧 ROI\n\n针对数据敏感或成本敏感的高频查询，采用本地 Llama 3 8B 等 SLM，配合置信度向大模型降级路由机制。ROI 测算从按 Token 计费转向硬件算力摊销。\n"
    },
    31: {
        "html": """
<h3>31.3 v1.3 新增来源索引</h3>
<ul>
<li><strong>GraphRAG</strong>: Microsoft Research 论文《From Local to Global: A Graph RAG Approach to Query-Focused Summarization》 (Edge et al., 2024).</li>
<li><strong>Multi-Agent</strong>: Microsoft 论文《AutoGen: Enabling Next-Gen LLM Applications》(Wu et al., 2023).</li>
<li><strong>LangGraph</strong>: LangChain 官方文档 - LangGraph (Stateful Multi-Agent).</li>
<li><strong>MCP</strong>: Anthropic 发布的 Model Context Protocol 官方标准文档.</li>
<li><strong>LLM-as-a-Judge</strong>: LMSYS Org 论文《Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena》(Zheng et al., 2023).</li>
</ul>
""",
        "plain": "\n\n    31.3 v1.3 新增来源索引\n\n  GraphRAG: Microsoft Research 论文《From Local to Global: A Graph RAG Approach...》\n  Multi-Agent: Microsoft 论文《AutoGen...》\n  LangGraph: LangChain 官方文档.\n  MCP: Anthropic 发布的 Model Context Protocol.\n  LLM-as-a-Judge: LMSYS Org 论文《Judging LLM-as-a-Judge...》\n"
    }
}

for section in data["sections"]:
    sec_num = section.get("num")
    if sec_num in updates:
        section["html"] += updates[sec_num]["html"]
        section["plain"] += updates[sec_num]["plain"]
        print(f"Updated section {sec_num}")

# Serialize
new_json_str = json.dumps(data, ensure_ascii=False)

# Replace in content
new_content = content.replace(data_json_str, new_json_str)

# Update UI and Titles
new_content = new_content.replace("<title>AI产品经理专业知识系统 v1.2.1 交互课件</title>", "<title>AI产品经理专业知识系统 v1.3 交互课件</title>")
new_content = new_content.replace("v1.2.1 结构整理版", "v1.3 进阶优化版")

with open(output_file, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Successfully generated {output_file}")
