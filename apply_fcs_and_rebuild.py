import os
import re

base_dir = r"C:\Users\singh\.gemini\antigravity\scratch\academic-portal"

build_script_path = os.path.join(base_dir, "build_full_site.py")
with open(build_script_path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update nav in build_full_site.py
old_nav = """def nav(depth=0):
    p = "../" * depth if depth > 0 else "./"
    return f\"\"\"<nav class="quick-nav">
  <a href="{p}discrete/index.html">discrete</a> / <a href="{p}dld/index.html">dld</a> / <a href="{p}ppl/index.html">ppl</a> / <a href="{p}dev-tools/index.html">dev tools</a> / <a href="{p}dsa/index.html">dsa</a>
</nav>\"\"\""""

new_nav = """def nav(depth=0):
    p = "../" * depth if depth > 0 else "./"
    return f\"\"\"<nav class="quick-nav">
  <a href="{p}discrete/index.html">discrete</a> / <a href="{p}dld/index.html">dld</a> / <a href="{p}ppl/index.html">ppl</a> / <a href="{p}dev-tools/index.html">dev tools</a> / <a href="{p}dsa/index.html">dsa</a> / <a href="{p}feedback-control-systems/index.html">feedback control systems</a>
</nav>\"\"\""""

if old_nav in code:
    code = code.replace(old_nav, new_nav)
    print("Updated nav in build_full_site.py")

# 2. Update title in INDEX_HTML
code = code.replace("<title>./</title>", "<title>thirdsem</title>")

# 3. Update filter placeholder
code = code.replace(
    'placeholder="filter subjects (discrete, dld, ppl, dev tools, dsa)..."',
    'placeholder="filter subjects (discrete, dld, ppl, dev tools, dsa, feedback control systems)..."'
)

# 4. Update dsa and add feedback control systems in tree-view
old_dsa_tree = """          <!-- dsa -->
          <li class="tree-node tree-node-subject">
            <div class="tree-branch">
              <span class="tree-symbol">└──</span>
              <a class="tree-link" href="dsa/index.html">dsa/</a>
            </div>"""

new_dsa_tree = """          <!-- dsa -->
          <li class="tree-node tree-node-subject">
            <div class="tree-branch">
              <span class="tree-symbol">├──</span>
              <a class="tree-link" href="dsa/index.html">dsa/</a>
            </div>"""

if old_dsa_tree in code:
    code = code.replace(old_dsa_tree, new_dsa_tree)

old_dsa_end = """              <li class="tree-node">
                <div class="tree-branch">
                  <span class="tree-symbol">└──</span>
                  <a class="tree-link" href="dsa/practical-lab-record/index.html">practical lab record/</a>
                </div>
              </li>
            </ul>
          </li>
        </ul>"""

new_dsa_end = """              <li class="tree-node">
                <div class="tree-branch">
                  <span class="tree-symbol">└──</span>
                  <a class="tree-link" href="dsa/practical-lab-record/index.html">practical lab record/</a>
                </div>
              </li>
            </ul>
          </li>

          <!-- feedback control systems -->
          <li class="tree-node tree-node-subject">
            <div class="tree-branch">
              <span class="tree-symbol">└──</span>
              <a class="tree-link" href="feedback-control-systems/index.html">feedback control systems/</a>
            </div>
            <ul class="tree-children">
              <li class="tree-node">
                <div class="tree-branch">
                  <span class="tree-symbol">└──</span>
                  <a class="tree-link" href="feedback-control-systems/assignments/index.html">assignments/</a>
                </div>
              </li>
            </ul>
          </li>
        </ul>"""

if old_dsa_end in code:
    code = code.replace(old_dsa_end, new_dsa_end)
    print("Updated tree view in build_full_site.py")

# 5. Append FCS pages generation if not already present
fcs_block = """
# ==========================================
# 6. FEEDBACK CONTROL SYSTEMS (only assignments)
# ==========================================
os.makedirs(os.path.join(BASE_DIR, "feedback-control-systems", "assignments"), exist_ok=True)

FCS_INDEX = f\"\"\"<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>feedback control systems</title>
  {THEME_INIT}
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>
  <div class="container">
    <header>
      <div class="header-top">
        <div class="breadcrumbs">
          <a href="../index.html">home</a>
          <span class="sep">/</span>
          <span class="current">feedback control systems</span>
        </div>
        <button id="theme-toggle" class="theme-btn" type="button" aria-label="toggle theme">theme</button>
      </div>
      <h1 class="site-title">feedback control systems</h1>
    </header>

    {nav(1)}

    <div class="notice-box">
      <p><strong>course:</strong> feedback control systems</p>
      <p><strong>note:</strong> only assignments.</p>
    </div>

    <main>
      <section class="tree-view">
        <span class="tree-root-label">feedback control systems/</span>
        <ul class="tree-list">
          <li class="tree-node">
            <div class="tree-branch">
              <span class="tree-symbol">└──</span>
              <a class="tree-link" href="assignments/index.html">assignments/</a>
            </div>
          </li>
        </ul>
      </section>

      <div class="section-block">
        <h2 class="section-title">assignments</h2>
        <div>
          <a href="assignments/index.html" class="btn">open assignments/ &rarr;</a>
        </div>
      </div>
    </main>

    {footer(1)}
  </div>
  <script src="../js/app.js"></script>
</body>
</html>\"\"\"
with open(os.path.join(BASE_DIR, "feedback-control-systems", "index.html"), "w", encoding="utf-8") as f:
    f.write(FCS_INDEX)

FCS_ASSIGN = f\"\"\"<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>feedback control systems // assignments</title>
  {THEME_INIT}
  <link rel="stylesheet" href="../../css/style.css">
</head>
<body>
  <div class="container">
    <header>
      <div class="header-top">
        <div class="breadcrumbs">
          <a href="../../index.html">home</a>
          <span class="sep">/</span>
          <a href="../index.html">feedback control systems</a>
          <span class="sep">/</span>
          <span class="current">assignments</span>
        </div>
        <button id="theme-toggle" class="theme-btn" type="button" aria-label="toggle theme">theme</button>
      </div>
      <h1 class="site-title">feedback control systems // assignments</h1>
    </header>

    {nav(2)}

    <div class="notice-box">
      <p><strong>instructions:</strong> complete the matlab onramp course and get the certificate from mtucert.netlify.app.</p>
    </div>

    <main>
      <section class="section-block">
        <h2 class="section-title">assignment checklist</h2>
        <ul class="checklist">
          <li class="checklist-item">
            <label><input type="checkbox"> <span>complete the matlab onramp (getting started) course</span></label>
          </li>
          <li class="checklist-item">
            <label><input type="checkbox"> <span>generate / obtain certificate from mtucert.netlify.app</span></label>
          </li>
        </ul>
      </section>

      <section class="section-block">
        <h2 class="section-title">1. matlab onramp course</h2>
        <ul class="action-list">
          <li><strong>course:</strong> matlab onramp (getting started)</li>
          <li><strong>platform:</strong> mathworks academy</li>
          <li><strong>official link:</strong> <a href="https://matlabacademy.mathworks.com/details/matlab-onramp/gettingstarted" target="_blank" rel="noopener noreferrer" style="color:var(--link); text-decoration:underline;">https://matlabacademy.mathworks.com/details/matlab-onramp/gettingstarted</a></li>
        </ul>
        <div style="margin-top:0.75rem;">
          <a href="https://matlabacademy.mathworks.com/details/matlab-onramp/gettingstarted" target="_blank" rel="noopener noreferrer" class="pdf-btn">open matlab onramp course &rarr;</a>
        </div>
      </section>

      <section class="section-block">
        <h2 class="section-title">2. mtu certificate portal</h2>
        <ul class="action-list">
          <li><strong>portal:</strong> mtucert</li>
          <li><strong>certificate link:</strong> <a href="https://mtucert.netlify.app" target="_blank" rel="noopener noreferrer" style="color:var(--link); text-decoration:underline;">https://mtucert.netlify.app</a></li>
        </ul>
        <div style="margin-top:0.75rem;">
          <a href="https://mtucert.netlify.app" target="_blank" rel="noopener noreferrer" class="pdf-btn">open mtucert portal &rarr;</a>
        </div>
      </section>
    </main>

    {footer(2, "feedback control systems")}
  </div>
  <script src="../../js/app.js"></script>
</body>
</html>\"\"\"
with open(os.path.join(BASE_DIR, "feedback-control-systems", "assignments", "index.html"), "w", encoding="utf-8") as f:
    f.write(FCS_ASSIGN)
"""

if "FEEDBACK CONTROL SYSTEMS" not in code:
    code = code + fcs_block
    print("Appended FCS pages in build_full_site.py")

with open(build_script_path, "w", encoding="utf-8") as f:
    f.write(code)

print("Saved updated build_full_site.py")
