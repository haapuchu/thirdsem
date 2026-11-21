import os

BASE_DIR = r"C:\Users\singh\.gemini\antigravity\scratch\academic-portal"

THEME_INIT = "<script>(function(){const t=localStorage.getItem('theme');if(t){document.documentElement.setAttribute('data-theme',t);}})();</script>"

def drawer(depth=0):
    p = "../" * depth if depth > 0 else "./"
    return f"""<div id="drawer-overlay" class="drawer-overlay" aria-hidden="true"></div>
<aside id="side-drawer" class="side-drawer" aria-label="side navigation" aria-hidden="true">
  <div class="drawer-header">
    <span class="drawer-title">thirdsem // menu</span>
    <button id="drawer-close" class="drawer-close-btn" type="button" aria-label="close menu">&times;</button>
  </div>
  <div class="drawer-body">
    <div class="drawer-nav-group">
      <a class="drawer-nav-link" href="{p}index.html"><strong>./ (home)</strong></a>
    </div>

    <div class="drawer-nav-group">
      <a class="drawer-subject-link" href="{p}discrete/index.html">discrete/</a>
      <div class="drawer-sublinks">
        <a class="drawer-sublink" href="{p}discrete/assignments/index.html">assignments/</a>
      </div>
    </div>

    <div class="drawer-nav-group">
      <a class="drawer-subject-link" href="{p}dld/index.html">dld/</a>
      <div class="drawer-sublinks">
        <a class="drawer-sublink" href="{p}dld/assignments/index.html">assignments/</a>
        <a class="drawer-sublink" href="{p}dld/practical-lab-record/index.html">practical lab record/</a>
      </div>
    </div>

    <div class="drawer-nav-group">
      <a class="drawer-subject-link" href="{p}ppl/index.html">ppl/</a>
      <div class="drawer-sublinks">
        <a class="drawer-sublink" href="{p}ppl/assignments/index.html">assignments/</a>
        <a class="drawer-sublink" href="{p}ppl/practical-lab-record/index.html">practical lab record/</a>
      </div>
    </div>

    <div class="drawer-nav-group">
      <a class="drawer-subject-link" href="{p}dev-tools/index.html">dev tools/</a>
      <div class="drawer-sublinks">
        <a class="drawer-sublink" href="{p}dev-tools/assignments/index.html">assignments/</a>
        <a class="drawer-sublink" href="{p}dev-tools/practical-lab-record/index.html">practical lab record/</a>
      </div>
    </div>

    <div class="drawer-nav-group">
      <a class="drawer-subject-link" href="{p}dsa/index.html">dsa/</a>
      <div class="drawer-sublinks">
        <a class="drawer-sublink" href="{p}dsa/assignments/index.html">assignments/</a>
        <a class="drawer-sublink" href="{p}dsa/practical-lab-record/index.html">practical lab record/</a>
      </div>
    </div>

    <div class="drawer-nav-group">
      <a class="drawer-subject-link" href="{p}feedback-control-systems/index.html">feedback control systems/</a>
      <div class="drawer-sublinks">
        <a class="drawer-sublink" href="{p}feedback-control-systems/assignments/index.html">assignments/</a>
      </div>
    </div>
  </div>
</aside>"""

def you_are_here(depth=0, items=None):
    if depth == 0 or not items:
        return '<div class="you-are-here"><span class="yah-label">you are here:</span> <span class="yah-path"><span class="yah-current">./</span></span></div>'
    p = "../" * depth if depth > 0 else "./"
    parts = [f'<a href="{p}index.html">./</a>']
    for label, href in items:
        if href:
            parts.append(f'<span class="yah-sep">/</span> <a href="{href}">{label}</a>')
        else:
            parts.append(f'<span class="yah-sep">/</span> <span class="yah-current">{label}</span>')
    return f'<div class="you-are-here"><span class="yah-label">you are here:</span> <span class="yah-path">{" ".join(parts)}</span></div>'

def header_controls():
    return """<div class="header-controls">
          <button id="menu-toggle" class="header-btn menu-btn" type="button" aria-label="toggle menu" aria-expanded="false">&equiv; menu</button>
          <button id="theme-toggle" class="header-btn theme-btn" type="button" aria-label="toggle theme">theme</button>
        </div>"""

def nav(depth=0):
    p = "../" * depth if depth > 0 else "./"
    return f"""<nav class="quick-nav">
  <a href="{p}discrete/index.html">discrete</a> / <a href="{p}dld/index.html">dld</a> / <a href="{p}ppl/index.html">ppl</a> / <a href="{p}dev-tools/index.html">dev tools</a> / <a href="{p}dsa/index.html">dsa</a> / <a href="{p}feedback-control-systems/index.html">feedback control systems</a>
</nav>"""

def footer(depth=0, sub_name=None):
    if depth == 0:
        return ""
    p = "../" * depth if depth > 0 else "./"
    if depth == 1:
        return f"""<footer>
  <a href="{p}index.html">&larr; home</a>
</footer>"""
    return f"""<footer>
  <a href="../index.html">&larr; {sub_name}</a> / <a href="{p}index.html">&larr; home</a>
</footer>"""

def pdf_embed(file_rel_path, label):
    return f"""<div class="pdf-container">
  <div class="pdf-toolbar">
    <div><strong>{label}</strong></div>
    <div>
      <a href="{file_rel_path}" target="_blank" rel="noopener noreferrer" class="pdf-btn">open pdf / download</a>
    </div>
  </div>
  <iframe src="{file_rel_path}" class="pdf-viewer-frame" title="{label}">
    <p><a href="{file_rel_path}" target="_blank">open pdf</a></p>
  </iframe>
  <p class="mobile-fallback-note">mobile: tap "open pdf / download" above if inline preview does not scroll.</p>
</div>"""

# -------------------------------------------------------------
# 1. ROOT index.html
# -------------------------------------------------------------
INDEX_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>thirdsem</title>
  {THEME_INIT}
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  {drawer(0)}
  <div class="container">
    <header>
      {you_are_here(0)}
      <div class="header-top">
        <h1 class="site-title">./</h1>
        {header_controls()}
      </div>
    </header>

    {nav(0)}

    <div class="notice-box">
      <p><strong>active deadline:</strong> dld assignments due 23 november 2026 (to be done on a separate notebook)</p>
    </div>

    <div class="filter-box">
      <input type="text" id="tree-filter" class="filter-input" placeholder="filter subjects (discrete, dld, ppl, dev tools, dsa, feedback control systems)..." autocomplete="off">
    </div>

    <main>
      <section class="tree-view">
        <span class="tree-root-label">./</span>
        <ul class="tree-list">
          <!-- discrete -->
          <li class="tree-node tree-node-subject">
            <div class="tree-branch">
              <span class="tree-symbol">├──</span>
              <a class="tree-link" href="discrete/index.html">discrete/</a>
            </div>
            <ul class="tree-children">
              <li class="tree-node">
                <div class="tree-branch">
                  <span class="tree-symbol">└──</span>
                  <a class="tree-link" href="discrete/assignments/index.html">assignments/</a>
                </div>
              </li>
            </ul>
          </li>

          <!-- dld -->
          <li class="tree-node tree-node-subject">
            <div class="tree-branch">
              <span class="tree-symbol">├──</span>
              <a class="tree-link" href="dld/index.html">dld/</a>
            </div>
            <ul class="tree-children">
              <li class="tree-node">
                <div class="tree-branch">
                  <span class="tree-symbol">├──</span>
                  <a class="tree-link" href="dld/assignments/index.html">assignments/</a>
                </div>
              </li>
              <li class="tree-node">
                <div class="tree-branch">
                  <span class="tree-symbol">└──</span>
                  <a class="tree-link" href="dld/practical-lab-record/index.html">practical lab record/</a>
                </div>
              </li>
            </ul>
          </li>

          <!-- ppl -->
          <li class="tree-node tree-node-subject">
            <div class="tree-branch">
              <span class="tree-symbol">├──</span>
              <a class="tree-link" href="ppl/index.html">ppl/</a>
            </div>
            <ul class="tree-children">
              <li class="tree-node">
                <div class="tree-branch">
                  <span class="tree-symbol">├──</span>
                  <a class="tree-link" href="ppl/assignments/index.html">assignments/</a>
                </div>
              </li>
              <li class="tree-node">
                <div class="tree-branch">
                  <span class="tree-symbol">└──</span>
                  <a class="tree-link" href="ppl/practical-lab-record/index.html">practical lab record/</a>
                </div>
              </li>
            </ul>
          </li>

          <!-- dev tools -->
          <li class="tree-node tree-node-subject">
            <div class="tree-branch">
              <span class="tree-symbol">├──</span>
              <a class="tree-link" href="dev-tools/index.html">dev tools/</a>
            </div>
            <ul class="tree-children">
              <li class="tree-node">
                <div class="tree-branch">
                  <span class="tree-symbol">├──</span>
                  <a class="tree-link" href="dev-tools/assignments/index.html">assignments/</a>
                </div>
              </li>
              <li class="tree-node">
                <div class="tree-branch">
                  <span class="tree-symbol">└──</span>
                  <a class="tree-link" href="dev-tools/practical-lab-record/index.html">practical lab record/</a>
                </div>
              </li>
            </ul>
          </li>

          <!-- dsa -->
          <li class="tree-node tree-node-subject">
            <div class="tree-branch">
              <span class="tree-symbol">├──</span>
              <a class="tree-link" href="dsa/index.html">dsa/</a>
            </div>
            <ul class="tree-children">
              <li class="tree-node">
                <div class="tree-branch">
                  <span class="tree-symbol">├──</span>
                  <a class="tree-link" href="dsa/assignments/index.html">assignments/</a>
                </div>
              </li>
              <li class="tree-node">
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
        </ul>
      </section>
    </main>
  </div>

  <script src="js/app.js"></script>
</body>
</html>"""

# -------------------------------------------------------------
# 2. DISCRETE
# -------------------------------------------------------------
DISCRETE_INDEX = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>discrete</title>
  {THEME_INIT}
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>
  {drawer(1)}
  <div class="container">
    <header>
      {you_are_here(1, [('discrete', None)])}
      <div class="header-top">
        <h1 class="site-title">discrete</h1>
        {header_controls()}
      </div>
    </header>

    {nav(1)}

    <div class="notice-box">
      <p><strong>note:</strong> handwrite in a separate notebook.</p>
    </div>

    <main>
      <section class="tree-view">
        <span class="tree-root-label">discrete/</span>
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
</html>"""

DISCRETE_ASSIGN = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>discrete // assignments</title>
  {THEME_INIT}
  <link rel="stylesheet" href="../../css/style.css">
</head>
<body>
  {drawer(2)}
  <div class="container">
    <header>
      {you_are_here(2, [('discrete', '../index.html'), ('assignments', None)])}
      <div class="header-top">
        <h1 class="site-title">discrete // assignments</h1>
        {header_controls()}
      </div>
    </header>

    {nav(2)}

    <div class="notice-box">
      <p><strong>instructions:</strong> handwrite in a separate notebook.</p>
    </div>

    <main>
      <section class="section-block">
        <h2 class="section-title">discrete assignment</h2>
        {pdf_embed('../../assets/pdfs/discrete/discrete_assignment.pdf', 'discrete_assignment.pdf')}
      </section>
    </main>

    {footer(2, 'discrete')}
  </div>
  <script src="../../js/app.js"></script>
</body>
</html>"""

# -------------------------------------------------------------
# 3. DLD
# -------------------------------------------------------------
DLD_INDEX = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>dld</title>
  {THEME_INIT}
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>
  {drawer(1)}
  <div class="container">
    <header>
      {you_are_here(1, [('dld', None)])}
      <div class="header-top">
        <h1 class="site-title">dld</h1>
        {header_controls()}
      </div>
    </header>

    {nav(1)}

    <div class="notice-box">
      <p><strong>active deadline:</strong> dld assignments due 23 november 2026 (to be done on a separate notebook)</p>
    </div>

    <main>
      <section class="tree-view">
        <span class="tree-root-label">dld/</span>
        <ul class="tree-list">
          <li class="tree-node">
            <div class="tree-branch">
              <span class="tree-symbol">├──</span>
              <a class="tree-link" href="assignments/index.html">assignments/</a>
            </div>
          </li>
          <li class="tree-node">
            <div class="tree-branch">
              <span class="tree-symbol">└──</span>
              <a class="tree-link" href="practical-lab-record/index.html">practical lab record/</a>
            </div>
          </li>
        </ul>
      </section>

      <div class="section-block">
        <h2 class="section-title">subpages</h2>
        <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
          <a href="assignments/index.html" class="btn">open assignments/ &rarr;</a>
          <a href="practical-lab-record/index.html" class="btn">open practical lab record/ &rarr;</a>
        </div>
      </div>
    </main>

    {footer(1)}
  </div>
  <script src="../js/app.js"></script>
</body>
</html>"""

DLD_ASSIGN = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>dld // assignments</title>
  {THEME_INIT}
  <link rel="stylesheet" href="../../css/style.css">
</head>
<body>
  {drawer(2)}
  <div class="container">
    <header>
      {you_are_here(2, [('dld', '../index.html'), ('assignments', None)])}
      <div class="header-top">
        <h1 class="site-title">dld // assignments</h1>
        {header_controls()}
      </div>
    </header>

    {nav(2)}

    <div class="notice-box">
      <p><strong>deadline:</strong> 23 november 2026</p>
      <p><strong>instructions:</strong> to be done on a separate notebook.</p>
    </div>

    <main>
      <section class="section-block">
        <h2 class="section-title">set 1</h2>
        {pdf_embed('../../assets/pdfs/dld/dld_assignment_1.pdf', 'dld_assignment_1.pdf')}
      </section>

      <section class="section-block">
        <h2 class="section-title">set 2</h2>
        {pdf_embed('../../assets/pdfs/dld/dld_assignment_2.pdf', 'dld_assignment_2.pdf')}
      </section>
    </main>

    {footer(2, 'dld')}
  </div>
  <script src="../../js/app.js"></script>
</body>
</html>"""

DLD_PRACT = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>dld // practical lab record</title>
  {THEME_INIT}
  <link rel="stylesheet" href="../../css/style.css">
</head>
<body>
  {drawer(2)}
  <div class="container">
    <header>
      {you_are_here(2, [('dld', '../index.html'), ('practical lab record', None)])}
      <div class="header-top">
        <h1 class="site-title">dld // practical lab record</h1>
        {header_controls()}
      </div>
    </header>

    {nav(2)}

    <div class="notice-box">
      <p><strong>course:</strong> digital logic design laboratory</p>
      <p><strong>experiment 3 date:</strong> 03 september 2026</p>
      <p><strong>experiment 4 date:</strong> 01 august 2026</p>
    </div>

    <main>
      <!-- Cover Page -->
      <section class="section-block">
        <h2 class="section-title">cover page &ndash; dld practical laboratory</h2>
        {pdf_embed('../../assets/pdfs/dld/cover_practical.pdf', 'cover_CS2302_Digital_Logic_and_Design_Practical.pdf')}
      </section>

      <!-- Experiment 3 Record -->
      <section class="section-block">
        <h2 class="section-title">experiment 3 (03 september 2026)</h2>
        {pdf_embed('../../assets/pdfs/dld/dld_exp3_lab_record.pdf', 'dld_exp3_lab_record.pdf')}
      </section>

      <!-- Experiment 4 Record -->
      <section class="section-block">
        <h2 class="section-title">experiment 4 (01 august 2026)</h2>
        {pdf_embed('../../assets/pdfs/dld/dld_exp4_lab_record.pdf', 'dld_exp4_lab_record.pdf')}
      </section>
    </main>

    {footer(2, 'dld')}
  </div>
  <script src="../../js/app.js"></script>
</body>
</html>"""

# -------------------------------------------------------------
# 4. PPL
# -------------------------------------------------------------
PPL_INDEX = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ppl</title>
  {THEME_INIT}
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>
  {drawer(1)}
  <div class="container">
    <header>
      {you_are_here(1, [('ppl', None)])}
      <div class="header-top">
        <h1 class="site-title">ppl</h1>
        {header_controls()}
      </div>
    </header>

    {nav(1)}

    <div class="notice-box">
      <p><strong>course:</strong> principles of programming languages</p>
    </div>

    <main>
      <section class="tree-view">
        <span class="tree-root-label">ppl/</span>
        <ul class="tree-list">
          <li class="tree-node">
            <div class="tree-branch">
              <span class="tree-symbol">├──</span>
              <a class="tree-link" href="assignments/index.html">assignments/</a>
            </div>
          </li>
          <li class="tree-node">
            <div class="tree-branch">
              <span class="tree-symbol">└──</span>
              <a class="tree-link" href="practical-lab-record/index.html">practical lab record/</a>
            </div>
          </li>
        </ul>
      </section>

      <div class="section-block">
        <h2 class="section-title">subpages</h2>
        <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
          <a href="assignments/index.html" class="btn">open assignments/ &rarr;</a>
          <a href="practical-lab-record/index.html" class="btn">open practical lab record/ &rarr;</a>
        </div>
      </div>
    </main>

    {footer(1)}
  </div>
  <script src="../js/app.js"></script>
</body>
</html>"""

PPL_ASSIGN = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ppl // assignments</title>
  {THEME_INIT}
  <link rel="stylesheet" href="../../css/style.css">
</head>
<body>
  {drawer(2)}
  <div class="container">
    <header>
      {you_are_here(2, [('ppl', '../index.html'), ('assignments', None)])}
      <div class="header-top">
        <h1 class="site-title">ppl // assignments</h1>
        {header_controls()}
      </div>
    </header>

    {nav(2)}

    <div class="notice-box">
      <p><strong>instructions:</strong> print and submit.</p>
    </div>

    <main>
      <section class="section-block">
        <h2 class="section-title">cover page &ndash; ppl assignment</h2>
        {pdf_embed('../../assets/pdfs/ppl/cover_assignment.pdf', 'cover_CS2308_Principles_of_Programming_Languages_Assignment.pdf')}
      </section>

      <section class="section-block">
        <h2 class="section-title">james ppl assignment</h2>
        {pdf_embed('../../assets/pdfs/ppl/james_ppl_assignment.pdf', 'james ppl assignments.pdf')}
      </section>
    </main>

    {footer(2, 'ppl')}
  </div>
  <script src="../../js/app.js"></script>
</body>
</html>"""

PPL_PRACT = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ppl // practical lab record</title>
  {THEME_INIT}
  <link rel="stylesheet" href="../../css/style.css">
</head>
<body>
  {drawer(2)}
  <div class="container">
    <header>
      {you_are_here(2, [('ppl', '../index.html'), ('practical lab record', None)])}
      <div class="header-top">
        <h1 class="site-title">ppl // practical lab record</h1>
        {header_controls()}
      </div>
    </header>

    {nav(2)}

    <div class="notice-box">
      <p><strong>course:</strong> cs2310 &ndash; ppl laboratory</p>
      <p><strong>instructions:</strong> handwrite the code and cut and paste outputs from the output print pdf.</p>
    </div>

    <main>
      <!-- Cover Page -->
      <section class="section-block">
        <h2 class="section-title">cover page &ndash; ppl practical laboratory</h2>
        {pdf_embed('../../assets/pdfs/ppl/cover_practical.pdf', 'cover_CS2310_Principles_of_Programming_Languages_Practical.pdf')}
      </section>

      <!-- Experiment List -->
      <section class="section-block">
        <h2 class="section-title">experiment list & dates</h2>
        <ul class="action-list">
          <li><strong>experiment 1:</strong> variable declaration and printing &bull; date: 16 october 2026</li>
          <li><strong>experiment 2:</strong> arithmetic operators &bull; date: 16 october 2026</li>
          <li><strong>experiment 3:</strong> finding the tsa and volume of a cuboid &bull; date: 16 october 2026</li>
          <li><strong>experiment 4:</strong> using an array to store and display marks of 5 students &bull; date: 16 october 2026</li>
          <li><strong>experiment 5:</strong> array operations &ndash; average, maximum, second element and index &bull; date: 16 october 2026</li>
          <li><strong>experiment 6:</strong> constructor in c++ &bull; date: 16 october 2026</li>
          <li><strong>experiment 7:</strong> finding the product of array elements &bull; date: 16 october 2026</li>
          <li><strong>experiment 8:</strong> factorial using recursion &bull; date: 16 october 2026</li>
          <li><strong>experiment 9:</strong> swapping two numbers using pass by value &bull; date: 16 october 2026</li>
          <li><strong>experiment 10:</strong> swapping two numbers using pass by reference &bull; date: 16 october 2026</li>
          <li><strong>experiment 11:</strong> array of objects &bull; date: 16 october 2026</li>
          <li><strong>experiment 12:</strong> bankaccount class &ndash; deposit and withdrawal &bull; date: 16 october 2026</li>
          <li><strong>experiment 13:</strong> to find the sum of elements in an array &bull; date: 16 october 2026</li>
          <li><strong>experiment 14:</strong> to find the sum of numbers up to n using recursion &bull; date: 16 october 2026</li>
          <li><strong>experiment 15:</strong> student class using a parameterized constructor &ndash; calculate total and average marks in three subjects &bull; date: 16 october 2026</li>
          <li><strong>experiment 16:</strong> product class using a parameterized constructor &ndash; calculate total price &bull; date: 16 october 2026</li>
          <li><strong>experiment 17:</strong> car class using a parameterized constructor &ndash; display car details &bull; date: 16 october 2026</li>
        </ul>
      </section>

      <!-- Code PDF -->
      <section class="section-block">
        <h2 class="section-title">ppl complete lab record (handwrite code)</h2>
        {pdf_embed('../../assets/pdfs/ppl/ppl_CPP_Lab_Record_Complete.pdf', 'CPP_Lab_Record_Complete.pdf')}
      </section>

      <!-- Outputs PDF -->
      <section class="section-block">
        <h2 class="section-title">ppl output print (cut & paste outputs)</h2>
        {pdf_embed('../../assets/pdfs/ppl/ppl_output_print.pdf', 'output print.pdf')}
      </section>
    </main>

    {footer(2, 'ppl')}
  </div>
  <script src="../../js/app.js"></script>
</body>
</html>"""

# -------------------------------------------------------------
# 5. DEV TOOLS
# -------------------------------------------------------------
DEV_INDEX = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>dev tools</title>
  {THEME_INIT}
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>
  {drawer(1)}
  <div class="container">
    <header>
      {you_are_here(1, [('dev tools', None)])}
      <div class="header-top">
        <h1 class="site-title">dev tools</h1>
        {header_controls()}
      </div>
    </header>

    {nav(1)}

    <div class="notice-box">
      <p><strong>course:</strong> development tools laboratory</p>
    </div>

    <main>
      <section class="tree-view">
        <span class="tree-root-label">dev tools/</span>
        <ul class="tree-list">
          <li class="tree-node">
            <div class="tree-branch">
              <span class="tree-symbol">├──</span>
              <a class="tree-link" href="assignments/index.html">assignments/</a>
            </div>
          </li>
          <li class="tree-node">
            <div class="tree-branch">
              <span class="tree-symbol">└──</span>
              <a class="tree-link" href="practical-lab-record/index.html">practical lab record/</a>
            </div>
          </li>
        </ul>
      </section>

      <div class="section-block">
        <h2 class="section-title">subpages</h2>
        <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
          <a href="assignments/index.html" class="btn">open assignments/ &rarr;</a>
          <a href="practical-lab-record/index.html" class="btn">open practical lab record/ &rarr;</a>
        </div>
      </div>
    </main>

    {footer(1)}
  </div>
  <script src="../js/app.js"></script>
</body>
</html>"""

DEV_ASSIGN = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>dev tools // assignments</title>
  {THEME_INIT}
  <link rel="stylesheet" href="../../css/style.css">
</head>
<body>
  {drawer(2)}
  <div class="container">
    <header>
      {you_are_here(2, [('dev tools', '../index.html'), ('assignments', None)])}
      <div class="header-top">
        <h1 class="site-title">dev tools // assignments</h1>
        {header_controls()}
      </div>
    </header>

    {nav(2)}

    <div class="notice-box">
      <p><strong>instructions:</strong> complete the assignments listed below.</p>
    </div>

    <main>
      <!-- Cover Page -->
      <section class="section-block">
        <h2 class="section-title">cover page &ndash; dev tools assignment</h2>
        {pdf_embed('../../assets/pdfs/dev-tools/cover_assignment.pdf', 'cover_CS2303_Development_Tools_Assignment.pdf')}
      </section>

      <!-- Assignment Questions -->
      <section class="section-block">
        <h2 class="section-title">assignments</h2>
        <ul class="action-list">
          <li><strong>1.</strong> resume/cv in latex with passport photo</li>
          <li><strong>2.</strong> technical paper using ieee conference latex template</li>
        </ul>
      </section>
    </main>

    {footer(2, 'dev tools')}
  </div>
  <script src="../../js/app.js"></script>
</body>
</html>"""

DEV_PRACT = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>dev tools // practical lab record</title>
  {THEME_INIT}
  <link rel="stylesheet" href="../../css/style.css">
</head>
<body>
  {drawer(2)}
  <div class="container">
    <header>
      {you_are_here(2, [('dev tools', '../index.html'), ('practical lab record', None)])}
      <div class="header-top">
        <h1 class="site-title">dev tools // practical lab record</h1>
        {header_controls()}
      </div>
    </header>

    {nav(2)}

    <div class="notice-box">
      <p><strong>course:</strong> cs2303 &ndash; development tools laboratory</p>
      <p><strong>instructions:</strong> for exp 1 to 5, all print and attach; for exp 6 & 7, handwrite the code and paste the outputs from the outputs pdf.</p>
    </div>

    <main>
      <!-- Cover Page -->
      <section class="section-block">
        <h2 class="section-title">cover page &ndash; dev tools practical laboratory</h2>
        {pdf_embed('../../assets/pdfs/dev-tools/cover_practical.pdf', 'cover_CS2303_Development_Tools_Practical.pdf')}
      </section>

      <!-- Experiment List -->
      <section class="section-block">
        <h2 class="section-title">experiment list & dates</h2>
        <ul class="action-list">
          <li><strong>experiment 1:</strong> technical report &bull; date: 02 september 2026 (print and attach)</li>
          <li><strong>experiment 2:</strong> mathematical symbols, operators and equations &bull; date: 16 september 2026 (print and attach)</li>
          <li><strong>experiment 3:</strong> creating a table with caption and label &bull; date: 16 october 2026 (print and attach)</li>
          <li><strong>experiment 4:</strong> side-by-side figures using subfigures &bull; date: 16 october 2026 (print and attach)</li>
          <li><strong>experiment 5:</strong> citations and references in latex &bull; date: 16 october 2026 (print and attach)</li>
          <li><strong>experiment 6:</strong> date: 21 november 2026 (handwrite code, paste output)</li>
          <li><strong>experiment 7:</strong> date: 21 november 2026 (handwrite code, paste output)</li>
        </ul>
      </section>

      <!-- Experiments 1 to 5 -->
      <section class="section-block">
        <h2 class="section-title">experiments 1 to 5 (print and attach)</h2>
        {pdf_embed('../../assets/pdfs/dev-tools/adit_dev_tools_1_to_5_lab_copy_output_and_code.pdf', 'dev_tools_1_to_5_lab_copy_output_and_code.pdf')}
      </section>

      <!-- Experiment 6 & 7 Code -->
      <section class="section-block">
        <h2 class="section-title">experiments 6 & 7 &ndash; code (handwrite code)</h2>
        {pdf_embed('../../assets/pdfs/dev-tools/dev_tools_6_7.pdf', 'dev tools 6 7.pdf')}
      </section>

      <!-- Experiment 6 & 7 Output -->
      <section class="section-block">
        <h2 class="section-title">experiments 6 & 7 &ndash; output (paste output)</h2>
        {pdf_embed('../../assets/pdfs/dev-tools/dev_6_7_output.pdf', 'dev 6 7 output.pdf')}
      </section>
    </main>

    {footer(2, 'dev tools')}
  </div>
  <script src="../../js/app.js"></script>
</body>
</html>"""

# -------------------------------------------------------------
# 6. DSA
# -------------------------------------------------------------
DSA_INDEX = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>dsa</title>
  {THEME_INIT}
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>
  {drawer(1)}
  <div class="container">
    <header>
      {you_are_here(1, [('dsa', None)])}
      <div class="header-top">
        <h1 class="site-title">dsa</h1>
        {header_controls()}
      </div>
    </header>

    {nav(1)}

    <div class="notice-box">
      <p><strong>course:</strong> data structures and algorithms</p>
    </div>

    <main>
      <section class="tree-view">
        <span class="tree-root-label">dsa/</span>
        <ul class="tree-list">
          <li class="tree-node">
            <div class="tree-branch">
              <span class="tree-symbol">├──</span>
              <a class="tree-link" href="assignments/index.html">assignments/</a>
            </div>
          </li>
          <li class="tree-node">
            <div class="tree-branch">
              <span class="tree-symbol">└──</span>
              <a class="tree-link" href="practical-lab-record/index.html">practical lab record/</a>
            </div>
          </li>
        </ul>
      </section>

      <div class="section-block">
        <h2 class="section-title">subpages</h2>
        <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
          <a href="assignments/index.html" class="btn">open assignments/ &rarr;</a>
          <a href="practical-lab-record/index.html" class="btn">open practical lab record/ &rarr;</a>
        </div>
      </div>
    </main>

    {footer(1)}
  </div>
  <script src="../js/app.js"></script>
</body>
</html>"""

DSA_ASSIGN = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>dsa // assignments</title>
  {THEME_INIT}
  <link rel="stylesheet" href="../../css/style.css">
</head>
<body>
  {drawer(2)}
  <div class="container">
    <header>
      {you_are_here(2, [('dsa', '../index.html'), ('assignments', None)])}
      <div class="header-top">
        <h1 class="site-title">dsa // assignments</h1>
        {header_controls()}
      </div>
    </header>

    {nav(2)}

    <div class="notice-box">
      <p><strong>instructions:</strong> handwrite in a4 sheet.</p>
    </div>

    <main>
      <!-- Cover Page -->
      <section class="section-block">
        <h2 class="section-title">cover page &ndash; dsa assignment</h2>
        {pdf_embed('../../assets/pdfs/dsa/cover_assignment.pdf', 'cover_CS2304_Data_Structures_and_Algorithms_I_Assignment.pdf')}
      </section>

      <!-- Assignment PDF -->
      <section class="section-block">
        <h2 class="section-title">dsa assignment</h2>
        {pdf_embed('../../assets/pdfs/dsa/dsa_assignment.pdf', 'dsa assignment.pdf')}
      </section>
    </main>

    {footer(2, 'dsa')}
  </div>
  <script src="../../js/app.js"></script>
</body>
</html>"""

DSA_PRACT = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>dsa // practical lab record</title>
  {THEME_INIT}
  <link rel="stylesheet" href="../../css/style.css">
</head>
<body>
  {drawer(2)}
  <div class="container">
    <header>
      {you_are_here(2, [('dsa', '../index.html'), ('practical lab record', None)])}
      <div class="header-top">
        <h1 class="site-title">dsa // practical lab record</h1>
        {header_controls()}
      </div>
    </header>

    {nav(2)}

    <div class="notice-box">
      <p><strong>course:</strong> cs2305 &ndash; data structures and algorithms &ndash; i laboratory</p>
      <p><strong>instructions:</strong> handwrite the code and paste the outputs.</p>
    </div>

    <main>
      <!-- Cover Page -->
      <section class="section-block">
        <h2 class="section-title">cover page &ndash; dsa practical laboratory</h2>
        {pdf_embed('../../assets/pdfs/dsa/cover_practical.pdf', 'cover_CS2304_Data_Structures_and_Algorithms_I_Practical.pdf')}
      </section>

      <!-- Experiment List -->
      <section class="section-block">
        <h2 class="section-title">experiment list & dates</h2>
        <ul class="action-list">
          <li><strong>experiment 1:</strong> sum of digits of a number &bull; date: 12 august 2026</li>
          <li><strong>experiment 2:</strong> palindrome string check &bull; date: 12 august 2026</li>
          <li><strong>experiment 3:</strong> histogram of character frequencies &bull; date: 12 august 2026</li>
          <li><strong>experiment 4:</strong> bubble sort &bull; date: 09 september 2026</li>
          <li><strong>experiment 5:</strong> insertion sort &bull; date: 09 september 2026</li>
          <li><strong>experiment 6:</strong> selection sort &bull; date: 09 september 2026</li>
          <li><strong>experiment 7:</strong> change case of each letter in a string &bull; date: 12 september 2026</li>
          <li><strong>experiment 8:</strong> dynamic memory allocation using malloc() &bull; date: 12 september 2026</li>
          <li><strong>experiment 9:</strong> resizing memory using realloc() &bull; date: 12 september 2026</li>
          <li><strong>experiment 10:</strong> creating a single node in linked list &bull; date: 23 september 2026</li>
          <li><strong>experiment 11:</strong> creating a singly linked list &bull; date: 23 september 2026</li>
          <li><strong>experiment 12:</strong> insertion in a singly linked list &bull; date: 07 october 2026</li>
        </ul>
      </section>

      <!-- Practical Code -->
      <section class="section-block">
        <h2 class="section-title">dsa practical (handwrite code)</h2>
        {pdf_embed('../../assets/pdfs/dsa/dsa_practical.pdf', 'dsa practical.pdf')}
      </section>

      <!-- Outputs Only -->
      <section class="section-block">
        <h2 class="section-title">outputs only (print and paste)</h2>
        {pdf_embed('../../assets/pdfs/dsa/Linked_List_and_C_Programs_Outputs_Only.pdf', 'Linked_List_and_C_Programs_Outputs_Only.pdf')}
      </section>
    </main>

    {footer(2, 'dsa')}
  </div>
  <script src="../../js/app.js"></script>
</body>
</html>"""

# -------------------------------------------------------------
# 7. FEEDBACK CONTROL SYSTEMS
# -------------------------------------------------------------
FCS_INDEX = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>feedback control systems</title>
  {THEME_INIT}
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>
  {drawer(1)}
  <div class="container">
    <header>
      {you_are_here(1, [('feedback control systems', None)])}
      <div class="header-top">
        <h1 class="site-title">feedback control systems</h1>
        {header_controls()}
      </div>
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
</html>"""

FCS_ASSIGN = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>feedback control systems // assignments</title>
  {THEME_INIT}
  <link rel="stylesheet" href="../../css/style.css">
</head>
<body>
  {drawer(2)}
  <div class="container">
    <header>
      {you_are_here(2, [('feedback control systems', '../index.html'), ('assignments', None)])}
      <div class="header-top">
        <h1 class="site-title">feedback control systems // assignments</h1>
        {header_controls()}
      </div>
    </header>

    {nav(2)}

    <div class="notice-box">
      <p><strong>instructions:</strong> complete the official matlab onramp course for the real certificate, or use mtucert.netlify.app to generate a certificate.</p>
    </div>

    <main>
      <!-- Option 1: Actual Course -->
      <section class="section-block">
        <h2 class="section-title">option 1: matlab onramp (actual course & real certificate)</h2>
        <ul class="action-list">
          <li><strong>details:</strong> the actual course where you have to complete the course to get the real certificate.</li>
          <li><strong>platform:</strong> mathworks academy</li>
          <li><strong>official link:</strong> <a href="https://matlabacademy.mathworks.com/details/matlab-onramp/gettingstarted" target="_blank" rel="noopener noreferrer" style="color:var(--link); text-decoration:underline;">https://matlabacademy.mathworks.com/details/matlab-onramp/gettingstarted</a></li>
        </ul>
        <div style="margin-top:0.75rem;">
          <a href="https://matlabacademy.mathworks.com/details/matlab-onramp/gettingstarted" target="_blank" rel="noopener noreferrer" class="pdf-btn">open matlab onramp (official) &rarr;</a>
        </div>
      </section>

      <!-- Option 2: Fake Certificate Generator -->
      <section class="section-block">
        <h2 class="section-title">option 2: mtucert (fake certificate website)</h2>
        <ul class="action-list">
          <li><strong>details:</strong> a website made to download fake certificates for people who do not want to do the course.</li>
          <li><strong>portal link:</strong> <a href="https://mtucert.netlify.app" target="_blank" rel="noopener noreferrer" style="color:var(--link); text-decoration:underline;">https://mtucert.netlify.app</a></li>
        </ul>
        <div style="margin-top:0.75rem;">
          <a href="https://mtucert.netlify.app" target="_blank" rel="noopener noreferrer" class="pdf-btn">open mtucert (fake certificate) &rarr;</a>
        </div>
      </section>
    </main>

    {footer(2, "feedback control systems")}
  </div>
  <script src="../../js/app.js"></script>
</body>
</html>"""

# Write all files
pages = {
    os.path.join(BASE_DIR, "index.html"): INDEX_HTML,
    os.path.join(BASE_DIR, "discrete", "index.html"): DISCRETE_INDEX,
    os.path.join(BASE_DIR, "discrete", "assignments", "index.html"): DISCRETE_ASSIGN,
    os.path.join(BASE_DIR, "dld", "index.html"): DLD_INDEX,
    os.path.join(BASE_DIR, "dld", "assignments", "index.html"): DLD_ASSIGN,
    os.path.join(BASE_DIR, "dld", "practical-lab-record", "index.html"): DLD_PRACT,
    os.path.join(BASE_DIR, "ppl", "index.html"): PPL_INDEX,
    os.path.join(BASE_DIR, "ppl", "assignments", "index.html"): PPL_ASSIGN,
    os.path.join(BASE_DIR, "ppl", "practical-lab-record", "index.html"): PPL_PRACT,
    os.path.join(BASE_DIR, "dev-tools", "index.html"): DEV_INDEX,
    os.path.join(BASE_DIR, "dev-tools", "assignments", "index.html"): DEV_ASSIGN,
    os.path.join(BASE_DIR, "dev-tools", "practical-lab-record", "index.html"): DEV_PRACT,
    os.path.join(BASE_DIR, "dsa", "index.html"): DSA_INDEX,
    os.path.join(BASE_DIR, "dsa", "assignments", "index.html"): DSA_ASSIGN,
    os.path.join(BASE_DIR, "dsa", "practical-lab-record", "index.html"): DSA_PRACT,
    os.path.join(BASE_DIR, "feedback-control-systems", "index.html"): FCS_INDEX,
    os.path.join(BASE_DIR, "feedback-control-systems", "assignments", "index.html"): FCS_ASSIGN,
}

for path, content in pages.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Successfully generated all {len(pages)} pages with side drawer, you-are-here navigation, and mobile optimizations!")
