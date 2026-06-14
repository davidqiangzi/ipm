import re

html_file = "/Users/dongchongchao/project/ipm/AI产品经理专业知识系统_v1.3_交互课件.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update `#markRead` and its JS logic
content = content.replace(
    "document.getElementById('markRead').onclick=()=>{const s=DATA.sections[currentIndex];progress[s.num]=true;saveProgress();renderNav();updateProgress()};",
    "document.getElementById('markRead').onclick=()=>{const s=DATA.sections[currentIndex];if(progress[s.num]){delete progress[s.num]}else{progress[s.num]=true}saveProgress();renderNav();updateProgress();updateMarkReadBtn()};"
)

# We need to define updateMarkReadBtn
update_btn_js = "function updateMarkReadBtn(){const s=DATA.sections[currentIndex];const btn=document.getElementById('markRead');if(btn){btn.textContent=progress[s.num]?'取消本章已学':'标记本章已学'}}"
content = content.replace("function renderCurrentTab(){", update_btn_js + "\nfunction renderCurrentTab(){")

# We also need to call updateMarkReadBtn when course renders
content = content.replace("renderCourse();", "renderCourse();updateMarkReadBtn();")

# 2. Update Theme Button to use sun/moon icons
sun_svg = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon-sun"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>'
moon_svg = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon-moon"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>'

# Add a function to update theme icon
update_theme_js = f"function updateThemeBtn(){{const cur=document.documentElement.getAttribute('data-theme');const btn=document.getElementById('themeBtn');if(btn){{btn.innerHTML=cur==='dark'?'{sun_svg}':'{moon_svg}'}}}}"
content = content.replace("function updateMarkReadBtn()", update_theme_js + "\nfunction updateMarkReadBtn()")

content = content.replace(
    "document.getElementById('themeBtn').onclick=()=>{const cur=document.documentElement.getAttribute('data-theme');document.documentElement.setAttribute('data-theme',cur==='dark'?'light':'dark')};",
    "document.getElementById('themeBtn').onclick=()=>{const cur=document.documentElement.getAttribute('data-theme');document.documentElement.setAttribute('data-theme',cur==='dark'?'light':'dark');updateThemeBtn()};updateThemeBtn();"
)

# Replace the initial button text
content = content.replace('<button id="themeBtn">深浅色切换</button>', '<button id="themeBtn" style="padding:6px 10px;display:inline-flex;align-items:center;justify-content:center"></button>')

# 3. Add GitHub button
github_svg = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#e3b341" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right:6px"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>'
github_btn = f'<a href="https://github.com/davidqiangzi/ipm" target="_blank" style="text-decoration:none;display:inline-flex;align-items:center;border:1px solid var(--line);background:var(--card);color:var(--text);padding:6px 14px;border-radius:999px;font-size:14px;font-weight:600;transition:all 0.2s">{github_svg}Star on GitHub</a>'

content = content.replace(
    '<div class="actions">',
    '<div class="actions" style="align-items:center">' + github_btn
)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("UI tweaks successfully applied!")
