import re

html_file = "/Users/dongchongchao/project/ipm/AI产品经理专业知识系统_v1.4_交互课件.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# We need to replace the old renderCourse logic.
# The old one was injected in patch_tts.py
old_render_course = """function renderCourse(){  const s=DATA.sections[currentIndex];  contentEl.innerHTML=`<article class="article" style="position:relative;">    <div id="ttsBtn" style="position:absolute;top:28px;right:28px;font-size:24px;cursor:pointer;user-select:none;transition:transform 0.2s" title="朗读本章">🎧</div>    ${s.html}    <div class="section-controls">      <button class="primary" id="prevBtn">上一章</button>      <button class="primary" id="nextBtn">下一章</button>    </div>  </article>`;    const ttsBtn = document.getElementById('ttsBtn');  ttsBtn.onclick = () => {    if (window.speechSynthesis.speaking || window.speechSynthesis.pending) {      window.speechSynthesis.cancel();      ttsBtn.textContent = '🎧';    } else {      const u = new SpeechSynthesisUtterance(s.plain);      u.lang = 'zh-CN';      u.rate = 1.0;      u.onend = () => { if(document.getElementById('ttsBtn')) document.getElementById('ttsBtn').textContent = '🎧'; };      window.speechSynthesis.speak(u);      ttsBtn.textContent = '⏸️';    }  };  document.getElementById('prevBtn').onclick=()=>{if(currentIndex>0){currentIndex--;renderCourse();updateMarkReadBtn();renderNav();window.scrollTo(0,0)}};  document.getElementById('nextBtn').onclick=()=>{if(currentIndex<DATA.sections.length-1){currentIndex++;renderCourse();updateMarkReadBtn();renderNav();window.scrollTo(0,0)}};}"""

new_render_course = """function renderCourse(){
  const s=DATA.sections[currentIndex];
  contentEl.innerHTML=`<article class="article" style="position:relative;">
    <div style="position:absolute;top:28px;right:28px;display:flex;align-items:center;gap:12px;">
      <div id="ttsProgressBg" style="width:120px;height:6px;background:var(--line);border-radius:3px;display:none;overflow:hidden;">
        <div id="ttsProgressInner" style="width:0%;height:100%;background:var(--brand);transition:width 0.2s;"></div>
      </div>
      <div id="ttsBtn" style="font-size:24px;cursor:pointer;user-select:none;transition:transform 0.2s" title="朗读本章">🎧</div>
    </div>
    ${s.html}
    <div class="section-controls">
      <button class="primary" id="prevBtn">上一章</button>
      <button class="primary" id="nextBtn">下一章</button>
    </div>
  </article>`;
  
  const ttsBtn = document.getElementById('ttsBtn');
  const ttsBg = document.getElementById('ttsProgressBg');
  const ttsInner = document.getElementById('ttsProgressInner');
  
  ttsBtn.onclick = () => {
    if (window.speechSynthesis.speaking) {
      if (window.speechSynthesis.paused) {
        window.speechSynthesis.resume();
        ttsBtn.textContent = '⏸️';
      } else {
        window.speechSynthesis.pause();
        ttsBtn.textContent = '▶️';
      }
    } else {
      const u = new SpeechSynthesisUtterance(s.plain);
      u.lang = 'zh-CN';
      u.rate = 1.0;
      ttsBg.style.display = 'block';
      
      u.onboundary = (e) => {
         if (e.name === 'word' || e.name === 'sentence') {
             const pct = Math.min(100, (e.charIndex / s.plain.length) * 100);
             if(ttsInner) ttsInner.style.width = pct + '%';
         }
      };
      u.onend = () => { 
        if(ttsBtn) ttsBtn.textContent = '🎧'; 
        if(ttsBg) ttsBg.style.display = 'none';
        if(ttsInner) ttsInner.style.width = '0%';
      };
      
      window.speechSynthesis.cancel();
      window.speechSynthesis.speak(u);
      ttsBtn.textContent = '⏸️';
    }
  };

  document.getElementById('prevBtn').onclick=()=>{if(currentIndex>0){currentIndex--;renderCourse();updateMarkReadBtn();renderNav();window.scrollTo(0,0)}};
  document.getElementById('nextBtn').onclick=()=>{if(currentIndex<DATA.sections.length-1){currentIndex++;renderCourse();updateMarkReadBtn();renderNav();window.scrollTo(0,0)}};
}""".replace('\n', '')

if old_render_course in content:
    content = content.replace(old_render_course, new_render_course)
else:
    print("Could not find the old render course logic to replace.")
    # Fallback to replace via regex if exact match fails
    import re
    content = re.sub(r'function renderCourse\(\)\{.*?\}function renderMap', new_render_course + 'function renderMap', content, flags=re.DOTALL)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("TTS pause and progress feature added successfully!")
