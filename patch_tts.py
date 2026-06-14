import re

html_file = "/Users/dongchongchao/project/ipm/AI产品经理专业知识系统_v1.4_交互课件.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# Modify renderCourse to include TTS button and logic
old_render_course = "function renderCourse(){const s=DATA.sections[currentIndex];contentEl.innerHTML=`<article class=\"article\">${s.html}<div class=\"section-controls\"><button class=\"primary\" id=\"prevBtn\">上一章</button><button class=\"primary\" id=\"nextBtn\">下一章</button></div></article>`;document.getElementById('prevBtn').onclick=()=>{if(currentIndex>0){currentIndex--;renderCourse();updateMarkReadBtn();renderNav();window.scrollTo(0,0)}};document.getElementById('nextBtn').onclick=()=>{if(currentIndex<DATA.sections.length-1){currentIndex++;renderCourse();updateMarkReadBtn();renderNav();window.scrollTo(0,0)}}}"

new_render_course = """function renderCourse(){
  const s=DATA.sections[currentIndex];
  contentEl.innerHTML=`<article class="article" style="position:relative;">
    <div id="ttsBtn" style="position:absolute;top:28px;right:28px;font-size:24px;cursor:pointer;user-select:none;transition:transform 0.2s" title="朗读本章">🎧</div>
    ${s.html}
    <div class="section-controls">
      <button class="primary" id="prevBtn">上一章</button>
      <button class="primary" id="nextBtn">下一章</button>
    </div>
  </article>`;
  
  const ttsBtn = document.getElementById('ttsBtn');
  ttsBtn.onclick = () => {
    if (window.speechSynthesis.speaking || window.speechSynthesis.pending) {
      window.speechSynthesis.cancel();
      ttsBtn.textContent = '🎧';
    } else {
      const u = new SpeechSynthesisUtterance(s.plain);
      u.lang = 'zh-CN';
      u.rate = 1.0;
      u.onend = () => { if(document.getElementById('ttsBtn')) document.getElementById('ttsBtn').textContent = '🎧'; };
      window.speechSynthesis.speak(u);
      ttsBtn.textContent = '⏸️';
    }
  };

  document.getElementById('prevBtn').onclick=()=>{if(currentIndex>0){currentIndex--;renderCourse();updateMarkReadBtn();renderNav();window.scrollTo(0,0)}};
  document.getElementById('nextBtn').onclick=()=>{if(currentIndex<DATA.sections.length-1){currentIndex++;renderCourse();updateMarkReadBtn();renderNav();window.scrollTo(0,0)}};
}""".replace('\n', '')

content = content.replace(old_render_course, new_render_course)

# Cancel speech when changing tabs
content = content.replace("function renderCurrentTab(){", "function renderCurrentTab(){window.speechSynthesis.cancel();")

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("TTS feature added successfully!")
