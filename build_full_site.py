import os

BASE_DIR = r"C:\Users\singh\.gemini\antigravity\scratch\academic-portal"

THEME_INIT = "<script>(function(){const t=localStorage.getItem('theme');if(t){document.documentElement.setAttribute('data-theme',t);}})();</script>"

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

# ==========================================
# 1. ROOT index.html
# ==========================================
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
  <div class="container">
    <header>
      <div class="header-top">
        <h1 class="site-title">./</h1>
        <button id="theme-toggle" class="theme-btn" type="button" aria-label="toggle theme">theme</button>
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
</html>
"""
with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(INDEX_HTML)

# ==========================================
# 2. DISCRETE (only assignments)
# ==========================================
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
  <div class="container">
    <header>
      <div class="header-top">
        <div class="breadcrumbs">
          <a href="../index.html">home</a>
          <span class="sep">/</span>
          <span class="current">discrete</span>
        </div>
        <button id="theme-toggle" class="theme-btn" type="button" aria-label="toggle theme">theme</button>
      </div>
      <h1 class="site-title">discrete</h1>
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

    {footer(1, 'discrete')}
  </div>
  <script src="../js/app.js"></script>
</body>
</html>"""
with open(os.path.join(BASE_DIR, "discrete", "index.html"), "w", encoding="utf-8") as f:
    f.write(DISCRETE_INDEX)

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
  <div class="container">
    <header>
      <div class="header-top">
        <div class="breadcrumbs">
          <a href="../../index.html">home</a>
          <span class="sep">/</span>
          <a href="../index.html">discrete</a>
          <span class="sep">/</span>
          <span class="current">assignments</span>
        </div>
        <button id="theme-toggle" class="theme-btn" type="button" aria-label="toggle theme">theme</button>
      </div>
      <h1 class="site-title">discrete // assignments</h1>
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
with open(os.path.join(BASE_DIR, "discrete", "assignments", "index.html"), "w", encoding="utf-8") as f:
    f.write(DISCRETE_ASSIGN)

# ==========================================
# 3. DLD
# ==========================================
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
  <div class="container">
    <header>
      <div class="header-top">
        <div class="breadcrumbs">
          <a href="../index.html">home</a>
          <span class="sep">/</span>
          <span class="current">dld</span>
        </div>
        <button id="theme-toggle" class="theme-btn" type="button" aria-label="toggle theme">theme</button>
      </div>
      <h1 class="site-title">dld</h1>
    </header>

    {nav(1)}

    <div class="notice-box">
      <p><strong>deadline:</strong> 23 november 2026</p>
      <p><strong>note:</strong> to be done on a separate notebook.</p>
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

      <div class="grid-2">
        <div class="section-block">
          <h2 class="section-title">assignments</h2>
          <div>
            <a href="assignments/index.html" class="btn">open assignments/ &rarr;</a>
          </div>
        </div>

        <div class="section-block">
          <h2 class="section-title">practical lab record</h2>
          <div>
            <a href="practical-lab-record/index.html" class="btn">open practical lab record/ &rarr;</a>
          </div>
        </div>
      </div>
    </main>

    {footer(1, 'dld')}
  </div>
  <script src="../js/app.js"></script>
</body>
</html>"""
with open(os.path.join(BASE_DIR, "dld", "index.html"), "w", encoding="utf-8") as f:
    f.write(DLD_INDEX)

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
  <div class="container">
    <header>
      <div class="header-top">
        <div class="breadcrumbs">
          <a href="../../index.html">home</a>
          <span class="sep">/</span>
          <a href="../index.html">dld</a>
          <span class="sep">/</span>
          <span class="current">assignments</span>
        </div>
        <button id="theme-toggle" class="theme-btn" type="button" aria-label="toggle theme">theme</button>
      </div>
      <h1 class="site-title">dld // assignments</h1>
    </header>

    {nav(2)}

    <div class="notice-box">
      <p><strong>deadline:</strong> 23 november 2026</p>
      <p><strong>note:</strong> to be done on a separate notebook.</p>
    </div>

    <main>
      <section class="section-block">
        <h2 class="section-title">assignment 1</h2>
        {pdf_embed('../../assets/pdfs/dld/dld_assignment_1.pdf', 'dld_assignment_1.pdf')}
      </section>

      <section class="section-block">
        <h2 class="section-title">assignment 2 (set i & set ii)</h2>
        {pdf_embed('../../assets/pdfs/dld/dld_assignment_2.pdf', 'dld 2nd assignment set i & set ii.pdf')}
      </section>
    </main>

    {footer(2, 'dld')}
  </div>
  <script src="../../js/app.js"></script>
</body>
</html>"""
with open(os.path.join(BASE_DIR, "dld", "assignments", "index.html"), "w", encoding="utf-8") as f:
    f.write(DLD_ASSIGN)

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
  <div class="container">
    <header>
      <div class="header-top">
        <div class="breadcrumbs">
          <a href="../../index.html">home</a>
          <span class="sep">/</span>
          <a href="../index.html">dld</a>
          <span class="sep">/</span>
          <span class="current">practical lab record</span>
        </div>
        <button id="theme-toggle" class="theme-btn" type="button" aria-label="toggle theme">theme</button>
      </div>
      <h1 class="site-title">dld // practical lab record</h1>
    </header>

    {nav(2)}

    <div class="notice-box">
      <p><strong>experiment 3:</strong> date: 03 september 2026</p>
      <p><strong>experiment 4:</strong> date: 01 august 2026</p>
    </div>

    <main>
      <!-- Cover Page -->
      <section class="section-block">
        <h2 class="section-title">cover page &ndash; digital logic design laboratory</h2>
        {pdf_embed('../../assets/pdfs/dld/cover_practical.pdf', 'cover_CS2307_Digital_Logic_Design_Laboratory.pdf')}
      </section>

      <!-- Exp 3 -->
      <section class="section-block">
        <h2 class="section-title">experiment 3 &ndash; lab record</h2>
        {pdf_embed('../../assets/pdfs/dld/dld_exp3_lab_record.pdf', 'dld_exp3_lab_record.pdf')}
      </section>

      <!-- Exp 4 -->
      <section class="section-block">
        <h2 class="section-title">experiment 4 &ndash; lab record</h2>
        {pdf_embed('../../assets/pdfs/dld/dld_exp4_lab_record.pdf', 'dld_exp4_lab_record.pdf')}
      </section>
    </main>

    {footer(2, 'dld')}
  </div>
  <script src="../../js/app.js"></script>
</body>
</html>"""
with open(os.path.join(BASE_DIR, "dld", "practical-lab-record", "index.html"), "w", encoding="utf-8") as f:
    f.write(DLD_PRACT)

# ==========================================
# 4. PPL
# ==========================================
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
  <div class="container">
    <header>
      <div class="header-top">
        <div class="breadcrumbs">
          <a href="../index.html">home</a>
          <span class="sep">/</span>
          <span class="current">ppl</span>
        </div>
        <button id="theme-toggle" class="theme-btn" type="button" aria-label="toggle theme">theme</button>
      </div>
      <h1 class="site-title">ppl</h1>
    </header>

    {nav(1)}

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

      <div class="grid-2">
        <div class="section-block">
          <h2 class="section-title">assignments</h2>
          <div>
            <a href="assignments/index.html" class="btn">open assignments/ &rarr;</a>
          </div>
        </div>

        <div class="section-block">
          <h2 class="section-title">practical lab record</h2>
          <div>
            <a href="practical-lab-record/index.html" class="btn">open practical lab record/ &rarr;</a>
          </div>
        </div>
      </div>
    </main>

    {footer(1, 'ppl')}
  </div>
  <script src="../js/app.js"></script>
</body>
</html>"""
with open(os.path.join(BASE_DIR, "ppl", "index.html"), "w", encoding="utf-8") as f:
    f.write(PPL_INDEX)

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
  <div class="container">
    <header>
      <div class="header-top">
        <div class="breadcrumbs">
          <a href="../../index.html">home</a>
          <span class="sep">/</span>
          <a href="../index.html">ppl</a>
          <span class="sep">/</span>
          <span class="current">assignments</span>
        </div>
        <button id="theme-toggle" class="theme-btn" type="button" aria-label="toggle theme">theme</button>
      </div>
      <h1 class="site-title">ppl // assignments</h1>
    </header>

    {nav(2)}

    <div class="notice-box">
      <p><strong>instruction:</strong> we have to print and submit.</p>
    </div>

    <main>
      <!-- Cover Page -->
      <section class="section-block">
        <h2 class="section-title">cover page &ndash; ppl assignment</h2>
        {pdf_embed('../../assets/pdfs/ppl/cover_assignment.pdf', 'cover_CS2309_Principles_of_Programming_Languages_Assignment.pdf')}
      </section>

      <section class="section-block">
        <h2 class="section-title">james ppl assignment (print & submit)</h2>
        {pdf_embed('../../assets/pdfs/ppl/james_ppl_assignment.pdf', 'james ppl assignment.pdf')}
      </section>
    </main>

    {footer(2, 'ppl')}
  </div>
  <script src="../../js/app.js"></script>
</body>
</html>"""
with open(os.path.join(BASE_DIR, "ppl", "assignments", "index.html"), "w", encoding="utf-8") as f:
    f.write(PPL_ASSIGN)

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
  <div class="container">
    <header>
      <div class="header-top">
        <div class="breadcrumbs">
          <a href="../../index.html">home</a>
          <span class="sep">/</span>
          <a href="../index.html">ppl</a>
          <span class="sep">/</span>
          <span class="current">practical lab record</span>
        </div>
        <button id="theme-toggle" class="theme-btn" type="button" aria-label="toggle theme">theme</button>
      </div>
      <h1 class="site-title">ppl // practical lab record</h1>
    </header>

    {nav(2)}

    <div class="notice-box">
      <p><strong>course:</strong> cs2310 &ndash; ppl laboratory</p>
      <p><strong>instructions:</strong> handwrite the source code for each experiment. cut and paste the corresponding terminal output from the output print pdf.</p>
    </div>

    <main>
      <!-- Cover Page -->
      <section class="section-block">
        <h2 class="section-title">cover page &ndash; ppl practical</h2>
        {pdf_embed('../../assets/pdfs/ppl/cover_practical.pdf', 'cover_CS2309_Principles_of_Programming_Languages_Practical.pdf')}
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
        <h2 class="section-title">cpp lab record complete (handwrite code)</h2>
        {pdf_embed('../../assets/pdfs/ppl/ppl_CPP_Lab_Record_Complete.pdf', 'ppl CPP_Lab_Record_Complete.pdf')}
      </section>

      <!-- Outputs PDF -->
      <section class="section-block">
        <h2 class="section-title">ppl output print (cut & paste outputs)</h2>
        {pdf_embed('../../assets/pdfs/ppl/ppl_output_print.pdf', 'ppl output print.pdf')}
      </section>
    </main>

    {footer(2, 'ppl')}
  </div>
  <script src="../../js/app.js"></script>
</body>
</html>"""
with open(os.path.join(BASE_DIR, "ppl", "practical-lab-record", "index.html"), "w", encoding="utf-8") as f:
    f.write(PPL_PRACT)

# ==========================================
# 5. DEV TOOLS
# ==========================================
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
  <div class="container">
    <header>
      <div class="header-top">
        <div class="breadcrumbs">
          <a href="../index.html">home</a>
          <span class="sep">/</span>
          <span class="current">dev tools</span>
        </div>
        <button id="theme-toggle" class="theme-btn" type="button" aria-label="toggle theme">theme</button>
      </div>
      <h1 class="site-title">dev tools</h1>
    </header>

    {nav(1)}

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

      <div class="grid-2">
        <div class="section-block">
          <h2 class="section-title">assignments</h2>
          <div>
            <a href="assignments/index.html" class="btn">open assignments/ &rarr;</a>
          </div>
        </div>

        <div class="section-block">
          <h2 class="section-title">practical lab record</h2>
          <div>
            <a href="practical-lab-record/index.html" class="btn">open practical lab record/ &rarr;</a>
          </div>
        </div>
      </div>
    </main>

    {footer(1, 'dev tools')}
  </div>
  <script src="../js/app.js"></script>
</body>
</html>"""
with open(os.path.join(BASE_DIR, "dev-tools", "index.html"), "w", encoding="utf-8") as f:
    f.write(DEV_INDEX)

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
  <div class="container">
    <header>
      <div class="header-top">
        <div class="breadcrumbs">
          <a href="../../index.html">home</a>
          <span class="sep">/</span>
          <a href="../index.html">dev tools</a>
          <span class="sep">/</span>
          <span class="current">assignments</span>
        </div>
        <button id="theme-toggle" class="theme-btn" type="button" aria-label="toggle theme">theme</button>
      </div>
      <h1 class="site-title">dev tools // assignments</h1>
    </header>

    {nav(2)}

    <main>
      <!-- Cover Page -->
      <section class="section-block">
        <h2 class="section-title">cover page &ndash; dev tools assignment</h2>
        {pdf_embed('../../assets/pdfs/dev-tools/cover_assignment.pdf', 'cover_CS2303_Development_Tools_Laboratory_Assignment.pdf')}
      </section>

      <section class="section-block">
        <h2 class="section-title">assignments</h2>
        <ul class="action-list">
          <li>1. resume/cv in latex with passport photo</li>
          <li>2. technical paper using ieee conference latex template</li>
        </ul>
      </section>
    </main>

    {footer(2, 'dev tools')}
  </div>
  <script src="../../js/app.js"></script>
</body>
</html>"""
with open(os.path.join(BASE_DIR, "dev-tools", "assignments", "index.html"), "w", encoding="utf-8") as f:
    f.write(DEV_ASSIGN)

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
  <div class="container">
    <header>
      <div class="header-top">
        <div class="breadcrumbs">
          <a href="../../index.html">home</a>
          <span class="sep">/</span>
          <a href="../index.html">dev tools</a>
          <span class="sep">/</span>
          <span class="current">practical lab record</span>
        </div>
        <button id="theme-toggle" class="theme-btn" type="button" aria-label="toggle theme">theme</button>
      </div>
      <h1 class="site-title">dev tools // practical lab record</h1>
    </header>

    {nav(2)}

    <div class="notice-box">
      <p><strong>course:</strong> cs2303 &ndash; development tools laboratory</p>
      <p><strong>experiments 1&ndash;5:</strong> all print and attach.</p>
      <p><strong>experiments 6 &amp; 7:</strong> handwrite the source code, and attach/paste the output from the outputs pdf.</p>
    </div>

    <main>
      <!-- Cover Page -->
      <section class="section-block">
        <h2 class="section-title">cover page &ndash; development tools laboratory</h2>
        {pdf_embed('../../assets/pdfs/dev-tools/cover_practical.pdf', 'cover_CS2303_Development_Tools_Laboratory_Practical.pdf')}
      </section>

      <!-- Experiment List -->
      <section class="section-block">
        <h2 class="section-title">experiment list & dates</h2>
        <ul class="action-list">
          <li><strong>experiment 1:</strong> technical report &bull; date: 02 september 2026</li>
          <li><strong>experiment 2:</strong> mathematical symbols, operators and equations &bull; date: 16 september 2026</li>
          <li><strong>experiment 3:</strong> creating a table with caption and label &bull; date: 16 october 2026</li>
          <li><strong>experiment 4:</strong> side-by-side figures using subfigures &bull; date: 16 october 2026</li>
          <li><strong>experiment 5:</strong> citations and references in latex &bull; date: 16 october 2026</li>
          <li><strong>experiment 6:</strong> date: 21 november 2026</li>
          <li><strong>experiment 7:</strong> date: 21 november 2026</li>
        </ul>
      </section>

      <!-- Exp 1-5 -->
      <section class="section-block">
        <h2 class="section-title">exp 1&ndash;5 lab copy output and code (print and attach)</h2>
        {pdf_embed('../../assets/pdfs/dev-tools/adit_dev_tools_1_to_5_lab_copy_output_and_code.pdf', 'adit dev tools 1 to 5 lab copy output and code.pdf')}
      </section>

      <!-- Exp 6 & 7 Code -->
      <section class="section-block">
        <h2 class="section-title">exp 6 &amp; 7 (handwrite code)</h2>
        {pdf_embed('../../assets/pdfs/dev-tools/dev_tools_6_7.pdf', 'dev tools 6 7.pdf')}
      </section>

      <!-- Exp 6 & 7 Output -->
      <section class="section-block">
        <h2 class="section-title">exp 6 &amp; 7 output (attach / paste outputs)</h2>
        {pdf_embed('../../assets/pdfs/dev-tools/dev_6_7_output.pdf', 'dev 6 7 output.pdf')}
      </section>
    </main>

    {footer(2, 'dev tools')}
  </div>
  <script src="../../js/app.js"></script>
</body>
</html>"""
with open(os.path.join(BASE_DIR, "dev-tools", "practical-lab-record", "index.html"), "w", encoding="utf-8") as f:
    f.write(DEV_PRACT)

# ==========================================
# 6. DSA
# ==========================================
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
  <div class="container">
    <header>
      <div class="header-top">
        <div class="breadcrumbs">
          <a href="../index.html">home</a>
          <span class="sep">/</span>
          <span class="current">dsa</span>
        </div>
        <button id="theme-toggle" class="theme-btn" type="button" aria-label="toggle theme">theme</button>
      </div>
      <h1 class="site-title">dsa</h1>
    </header>

    {nav(1)}

    <div class="notice-box">
      <p><strong>assignments note:</strong> handwrite in a4 sheet.</p>
      <p><strong>practicals note:</strong> handwrite the code and paste the outputs.</p>
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

      <div class="grid-2">
        <div class="section-block">
          <h2 class="section-title">assignments</h2>
          <div>
            <a href="assignments/index.html" class="btn">open assignments/ &rarr;</a>
          </div>
        </div>

        <div class="section-block">
          <h2 class="section-title">practical lab record</h2>
          <div>
            <a href="practical-lab-record/index.html" class="btn">open practical lab record/ &rarr;</a>
          </div>
        </div>
      </div>
    </main>

    {footer(1, 'dsa')}
  </div>
  <script src="../js/app.js"></script>
</body>
</html>"""
with open(os.path.join(BASE_DIR, "dsa", "index.html"), "w", encoding="utf-8") as f:
    f.write(DSA_INDEX)

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
  <div class="container">
    <header>
      <div class="header-top">
        <div class="breadcrumbs">
          <a href="../../index.html">home</a>
          <span class="sep">/</span>
          <a href="../index.html">dsa</a>
          <span class="sep">/</span>
          <span class="current">assignments</span>
        </div>
        <button id="theme-toggle" class="theme-btn" type="button" aria-label="toggle theme">theme</button>
      </div>
      <h1 class="site-title">dsa // assignments</h1>
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
with open(os.path.join(BASE_DIR, "dsa", "assignments", "index.html"), "w", encoding="utf-8") as f:
    f.write(DSA_ASSIGN)

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
  <div class="container">
    <header>
      <div class="header-top">
        <div class="breadcrumbs">
          <a href="../../index.html">home</a>
          <span class="sep">/</span>
          <a href="../index.html">dsa</a>
          <span class="sep">/</span>
          <span class="current">practical lab record</span>
        </div>
        <button id="theme-toggle" class="theme-btn" type="button" aria-label="toggle theme">theme</button>
      </div>
      <h1 class="site-title">dsa // practical lab record</h1>
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
with open(os.path.join(BASE_DIR, "dsa", "practical-lab-record", "index.html"), "w", encoding="utf-8") as f:
    f.write(DSA_PRACT)

print("Site built with all updated wording, experiments, and cover pages!")

# ==========================================
# 6. FEEDBACK CONTROL SYSTEMS (only assignments)
# ==========================================
os.makedirs(os.path.join(BASE_DIR, "feedback-control-systems", "assignments"), exist_ok=True)

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
</html>"""
with open(os.path.join(BASE_DIR, "feedback-control-systems", "index.html"), "w", encoding="utf-8") as f:
    f.write(FCS_INDEX)

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
with open(os.path.join(BASE_DIR, "feedback-control-systems", "assignments", "index.html"), "w", encoding="utf-8") as f:
    f.write(FCS_ASSIGN)
