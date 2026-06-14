import re

html_file = "/Users/dongchongchao/project/ipm/AI产品经理专业知识系统_v1.3_交互课件.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Tabs HTML
content = content.replace(
    '<button data-tab="v12">v1.1 / v1.2 增强</button>',
    '<button data-tab="v12">v1.1 / v1.2</button><button data-tab="v13">v1.3 进阶</button>'
)

# 2. Update badgeLabel function
old_badge = "function badgeLabel(s){if(s.num>=20&&s.num<=25)return 'v1.1'; if(s.num>=26&&s.num<=28)return 'v1.2'; if(s.num>=29&&s.num<=30)return '总结'; if(s.num===7)return '增强'; return ''}"
new_badge = "function badgeLabel(s){if([5,7,8,10,31].includes(s.num))return 'v1.3'; if(s.num>=20&&s.num<=25)return 'v1.1'; if(s.num>=26&&s.num<=28)return 'v1.2'; if(s.num>=29&&s.num<=30)return '总结'; return ''}"
content = content.replace(old_badge, new_badge)

# 3. Add renderV13 function
render_v13_code = """function renderV13(){const items=DATA.sections.filter(s=>[5,7,8,10,31].includes(s.num));contentEl.innerHTML='<article class="article"><h2>v1.3 进阶内容</h2><div class="card-grid">'+items.map(s=>`<div class="card"><h3>${s.num}. ${s.title}</h3><p><span class="badge">v1.3</span> 进阶：点击左侧目录进入章节末尾查看。</p><button class="primary" onclick="openSection(${s.num})">打开章节</button></div>`).join('')+'</div></article>'}"""

# insert renderV13 before renderQuiz
content = content.replace("function renderQuiz()", render_v13_code + "\nfunction renderQuiz()")

# 4. Update renderCurrentTab to handle v13
old_render_tab = "if(currentTab==='v12')renderV12();if(currentTab==='quiz')renderQuiz();"
new_render_tab = "if(currentTab==='v12')renderV12();if(currentTab==='v13')renderV13();if(currentTab==='quiz')renderQuiz();"
content = content.replace(old_render_tab, new_render_tab)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("UI patched!")
