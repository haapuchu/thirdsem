import os
import shutil

BASE_DIR = r"C:\Users\singh\.gemini\antigravity\scratch\academic-portal"

os.makedirs(os.path.join(BASE_DIR, "css"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "js"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "assets", "pdfs"), exist_ok=True)

# 1. Subject Definitions (Names kept exactly as requested)
# Note: 'discrete' has ONLY assignments.
SUBJECTS = [
    {
        "id": "discrete",
        "name": "discrete",
        "assignments": {
            "title": "discrete // assignments",
            "what_to_do": [
                "Review theoretical definitions and standard mathematical laws (De Morgan's, Distributive, Absorption).",
                "Construct formal proofs step-by-step: direct proof, proof by contradiction, and mathematical induction.",
                "Draw formal diagrams: Venn diagrams for set theory, Hasse diagrams for partially ordered sets (Posets), and node-edge graphs.",
                "Verify truth tables for logical equivalences before writing the final solution."
            ],
            "what_to_write": [
                "1. Header: discrete, Assignment Number, Student Name, Roll No, Date.",
                "2. Problem Statement: Copy each question clearly in bold or distinct ink.",
                "3. Axioms / Theorems Applied: State every theorem or algebraic equivalence law explicitly by name.",
                "4. Step-by-Step Derivation / Truth Table: Show each intermediate step without skipping algebra.",
                "5. Final Boxed Answer: Conclude with a boxed final expression or formal Q.E.D."
            ],
            "submission_guidelines": [
                "Page limit: Maximum 4 pages per assignment set.",
                "Handwriting: Blue/Black ink only, margins on left (1.5 inch) for instructor markings.",
                "Diagrams: Must be drawn with a ruler and compass/stencil. No freehand graphs."
            ],
            "pdf_rel_path": "../../assets/pdfs/discrete/assignments.pdf"
        },
        "practical": None  # ONLY assignments for discrete
    },
    {
        "id": "dld",
        "name": "dld",
        "assignments": {
            "title": "dld // assignments",
            "what_to_do": [
                "Derive canonical Sum of Products (SOP) and Product of Sums (POS) forms from given truth specifications.",
                "Perform Boolean minimization using K-Maps (2, 3, 4, and 5 variable maps) and algebraic postulates.",
                "Design combinational logic: Half/Full Adder, Subtractor, Code Converters (BCD to Excess-3, Gray Code), and Multiplexers.",
                "Analyze flip-flop conversions and excitation tables for JK, D, T, and SR flip-flops."
            ],
            "what_to_write": [
                "1. Assignment Identification: Name, Roll Number, dld, Submission Date.",
                "2. Truth Table: Complete truth table with all binary input states (000 through 111...).",
                "3. K-Map Grid: Draw square cells with Gray code indexing (00, 01, 11, 10). Box groups (pairs, quads, octets) with don't cares (X).",
                "4. Simplified Equation: Express minimized output boolean formula clearly.",
                "5. Logic Circuit Schematic: Draw circuit with standard ANSI/IEEE gate symbols and label all pin connections."
            ],
            "submission_guidelines": [
                "Ensure circuit lines do not intersect without a connection dot.",
                "Use clean straight lines for bus tracks and logic signals."
            ],
            "pdf_rel_path": "../../assets/pdfs/dld/assignments.pdf"
        },
        "practical": {
            "title": "dld // practical lab record",
            "what_to_do": [
                "Wire TTL Integrated Circuits (7400 NAND, 7402 NOR, 7408 AND, 7432 OR, 7486 XOR) on breadboards or trainer kits.",
                "Construct and verify Adders/Subtractors, 4:1 Multiplexers (IC 74153), and 3:8 Decoders (IC 74138).",
                "Build synchronous and asynchronous mod-N counters using IC 7474 (D-FF) and IC 7476 (JK-FF).",
                "Record logic probe voltages (High ~ 5V, Low ~ 0V) and verify LED indicators against truth tables."
            ],
            "what_to_write": [
                "1. Aim: Objective of the experiment.",
                "2. Apparatus Required: Full list of IC numbers, trainer kit specification, patch cords.",
                "3. IC Pinout Diagrams: Explicitly sketch pin connections showing VCC (Pin 14) and GND (Pin 7).",
                "4. Circuit Diagram: Complete schematic with pin numbers marked at every gate terminal.",
                "5. Observation / Truth Table: Tabulated side-by-side comparison of Theoretical vs Practical LED state.",
                "6. Precautions & Result: Electrical safety rules observed and conclusive verification note."
            ],
            "submission_guidelines": [
                "Record sheets must have neat diagrams on the blank left page and text on the ruled right page.",
                "Must be verified and signed by lab instructor during the scheduled lab period."
            ],
            "pdf_rel_path": "../../assets/pdfs/dld/practical-lab-record.pdf"
        }
    },
    {
        "id": "ppl",
        "name": "ppl",
        "assignments": {
            "title": "ppl // assignments",
            "what_to_do": [
                "Analyze formal grammar structures using Backus-Naur Form (BNF) and Extended BNF.",
                "Construct parse trees and leftmost/rightmost derivations to detect grammar ambiguity.",
                "Trace execution environments: stack activation records, static vs dynamic scoping, and closures.",
                "Compare parameter passing modes: pass-by-value, pass-by-reference, and pass-by-name."
            ],
            "what_to_write": [
                "1. Assignment Metadata: ppl, Assignment Sheet ID, Student Roll Number.",
                "2. Theoretical Foundation: Explain the semantic model or type discipline in question.",
                "3. Grammar Productions & Derivations: Show explicit non-terminal substitutions step-by-step.",
                "4. Parse Tree: Draw hierarchical tree with non-terminals as branches and terminals as leaf nodes.",
                "5. Comparison Matrix: Tabulated comparison contrasting multiple paradigms with concrete short snippets."
            ],
            "submission_guidelines": [
                "Write clear text derivations. Highlight terminals in quotes or monospace.",
                "Diagrams must have explicit root and branch nodes."
            ],
            "pdf_rel_path": "../../assets/pdfs/ppl/assignments.pdf"
        },
        "practical": {
            "title": "ppl // practical lab record",
            "what_to_do": [
                "Implement declarative and functional programs in Haskell, Scheme, or Python.",
                "Write recursive list operations, higher-order functions (map, filter, reduce), and lambda functions.",
                "Construct Prolog knowledge bases: formulate facts, rules, and run unification/backtracking queries.",
                "Document execution commands using the respective compilers/interpreters (GHC, SWI-Prolog)."
            ],
            "what_to_write": [
                "1. Aim: Language mechanism or paradigm under study.",
                "2. Paradigm Overview: Summary of functional or logic programming constructs utilized.",
                "3. Formal Logic / Rules: Declarative specification or mathematical definition of the problem.",
                "4. Program Listing: Clean, commented source code.",
                "5. Execution Trace: Terminal logs of interactive sessions, queries, and variable bindings.",
                "6. Inference & Conclusion: Reflection on declarative semantics vs imperative loops."
            ],
            "submission_guidelines": [
                "Include both successful unification queries and failed backtracking cases for Prolog.",
                "Keep code listings cleanly indented."
            ],
            "pdf_rel_path": "../../assets/pdfs/ppl/practical-lab-record.pdf"
        }
    },
    {
        "id": "dev-tools",
        "name": "dev tools",
        "assignments": {
            "title": "dev tools // assignments",
            "what_to_do": [
                "Formulate branching models: Git Flow, trunk-based development, and rebase vs merge strategies.",
                "Write advanced Bash shell scripts for log parsing and automated file batching.",
                "Design multi-stage Dockerfiles optimizing image size, caching layers, and non-root users.",
                "Construct CI/CD automation pipelines for automated linting, testing, and deployment."
            ],
            "what_to_write": [
                "1. Header: dev tools, Assignment Title, Environment Specs (OS, Kernel, Tool versions).",
                "2. Problem Statement: Real-world engineering or deployment challenge.",
                "3. Configuration Code: Complete scripts (.sh, Dockerfile, .github/workflows/*.yml).",
                "4. Command Breakdown: Detailed table explaining every flag, argument, and pipe command used.",
                "5. Output Verification: Terminal output proof and exit status ($? == 0)."
            ],
            "submission_guidelines": [
                "All commands must be verified to run on modern Linux / WSL environments.",
                "Configs must be free of hardcoded secret keys or passwords."
            ],
            "pdf_rel_path": "../../assets/pdfs/dev-tools/assignments.pdf"
        },
        "practical": {
            "title": "dev tools // practical lab record",
            "what_to_do": [
                "Execute hands-on Git workflows: interactive rebase, cherry-pick, conflict resolution, tag creation.",
                "Build, tag, run, inspect, and stop Docker containers; manage persistent volumes and bridge networks.",
                "Automate project builds using Makefiles with variables, phony targets, and clean rules.",
                "Debug HTTP APIs using cURL and Postman, capturing headers and status codes."
            ],
            "what_to_write": [
                "1. Aim: Name of tool, service, or workflow configured.",
                "2. Prerequisites: Packages and system prerequisites installed.",
                "3. Sequential Commands: Verbatim step-by-step terminal commands.",
                "4. Configuration Files: Cleanly written config files (e.g., Makefile, compose.yaml).",
                "5. Terminal Transcript: Actual command output screenshots or pasted logs.",
                "6. Outcome: Verification that build, container, or Git history is in expected state."
            ],
            "submission_guidelines": [
                "Differentiate user commands with prompt symbol ($ ) from terminal output.",
                "Include git graph log output (git log --oneline --graph --all)."
            ],
            "pdf_rel_path": "../../assets/pdfs/dev-tools/practical-lab-record.pdf"
        }
    },
    {
        "id": "dsa",
        "name": "dsa",
        "assignments": {
            "title": "dsa // assignments",
            "what_to_do": [
                "Analyze runtime complexity using asymptotic notations (Big-O, Omega, Theta).",
                "Solve recurrence relations using the Master Method and recursion tree methods.",
                "Simulate tree rebalancing: AVL tree single/double rotations and Red-Black tree insertion cases.",
                "Formulate Dynamic Programming state-transition tables and base conditions."
            ],
            "what_to_write": [
                "1. Assignment Identification: Name, Roll No, dsa, Assignment No.",
                "2. Problem Definition: Precise mathematical/algorithmic formulation.",
                "3. Algorithmic Pseudocode: Clear, structured pseudocode with line numbers.",
                "4. Dry Run & Trace Table: Step-by-step execution trace tracking pointers, arrays, or recursion stack.",
                "5. Complexity Derivation: Explicit mathematical proof of best, worst, and average case time and space complexity."
            ],
            "submission_guidelines": [
                "Always state assumptions regarding input range and memory boundaries.",
                "Use clean diagrams for pointer changes and linked list transformations."
            ],
            "pdf_rel_path": "../../assets/pdfs/dsa/assignments.pdf"
        },
        "practical": {
            "title": "dsa // practical lab record",
            "what_to_do": [
                "Implement core data structures from scratch (Singly/Doubly Linked Lists, Stack, Queue, BST, Heap).",
                "Implement sorting algorithms: QuickSort, MergeSort, HeapSort with comparison counts.",
                "Implement Graph Algorithms: BFS, DFS, Dijkstra's Shortest Path, Kruskal's Algorithm.",
                "Test against multiple datasets: empty, single element, already-sorted, reverse-sorted, duplicate keys."
            ],
            "what_to_write": [
                "1. Aim: Precise name of the data structure or algorithm implemented.",
                "2. Algorithm: Step-by-step algorithm explanation.",
                "3. Source Code: Modular, well-formatted code listing in C / C++ / Java / Python.",
                "4. Test Cases & Output: Formatted terminal output showing menu-driven interface, insertions, deletions, and traversals.",
                "5. Complexity Analysis: Rigorous Time and Auxiliary Space complexity summary.",
                "6. Result: Concluding statement of successful compilation and test pass."
            ],
            "submission_guidelines": [
                "In C/C++, all dynamically allocated memory must be properly freed to prevent leaks.",
                "Lab record index page must be signed by faculty for each experiment."
            ],
            "pdf_rel_path": "../../assets/pdfs/dsa/practical-lab-record.pdf"
        }
    }
]

# Clean up discrete/practical-lab-record if it exists
discrete_lab_dir = os.path.join(BASE_DIR, "discrete", "practical-lab-record")
if os.path.exists(discrete_lab_dir):
    shutil.rmtree(discrete_lab_dir)
discrete_lab_pdf = os.path.join(BASE_DIR, "assets", "pdfs", "discrete", "practical-lab-record.pdf")
if os.path.exists(discrete_lab_pdf):
    os.remove(discrete_lab_pdf)

# 2. CSS with Light/Dark variables
CSS_CONTENT = """/* ==========================================================================
   MINIMAL, TO-THE-POINT, HIGHLY RESPONSIVE
   ========================================================================== */

:root, [data-theme="light"] {
  --bg: #ffffff;
  --text: #111111;
  --muted: #666666;
  --border: #222222;
  --border-light: #e5e5e5;
  --card-bg: #fcfcfc;
  --tree-line: #888888;
  --link: #0044cc;
  --font-mono: ui-monospace, 'SFMono-Regular', Menlo, Monaco, Consolas, monospace;
  --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  --max-w: 920px;
}

@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #121212;
    --text: #eeeeee;
    --muted: #999999;
    --border: #444444;
    --border-light: #2a2a2a;
    --card-bg: #181818;
    --tree-line: #666666;
    --link: #66b2ff;
  }
}

[data-theme="dark"] {
  --bg: #121212;
  --text: #eeeeee;
  --muted: #999999;
  --border: #444444;
  --border-light: #2a2a2a;
  --card-bg: #181818;
  --tree-line: #666666;
  --link: #66b2ff;
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  background-color: var(--bg);
  color: var(--text);
  font-family: var(--font-sans);
  font-size: 15px;
  line-height: 1.5;
  padding: 1.25rem 1rem 3rem 1rem;
}

.container {
  max-width: var(--max-w);
  margin: 0 auto;
}

/* Header */
header {
  border-bottom: 1px solid var(--border);
  padding-bottom: 0.75rem;
  margin-bottom: 1rem;
}

.header-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}

.breadcrumbs {
  font-family: var(--font-mono);
  font-size: 0.85rem;
  margin-bottom: 0.25rem;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.35rem;
}

.breadcrumbs a {
  color: var(--link);
  text-decoration: underline;
}

.breadcrumbs span.sep {
  color: var(--muted);
}

.breadcrumbs span.current {
  font-weight: 700;
  color: var(--text);
}

h1.site-title {
  font-size: 1.4rem;
  font-family: var(--font-mono);
  font-weight: 700;
  letter-spacing: -0.5px;
  text-transform: lowercase;
}

/* Theme Toggle Button */
.theme-btn {
  background: transparent;
  border: 1px solid var(--border);
  color: var(--text);
  font-family: var(--font-mono);
  font-size: 0.75rem;
  padding: 0.25rem 0.6rem;
  cursor: pointer;
  line-height: 1;
}

.theme-btn:hover {
  background: var(--border);
  color: var(--bg);
}

/* Quick Nav */
.quick-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin: 0.75rem 0;
  padding: 0.5rem 0;
  border-bottom: 1px dashed var(--border-light);
  font-family: var(--font-mono);
  font-size: 0.85rem;
}

.quick-nav a {
  color: var(--link);
  text-decoration: underline;
}

.quick-nav a:hover {
  color: var(--text);
}

/* Search Input */
.filter-box {
  margin: 1rem 0;
}

.filter-input {
  width: 100%;
  padding: 0.6rem 0.75rem;
  font-family: var(--font-mono);
  font-size: 0.95rem;
  border: 1px solid var(--border);
  background: var(--bg);
  color: var(--text);
  outline: none;
}

.filter-input:focus {
  border-color: var(--link);
}

/* Tree Structure */
.tree-view {
  font-family: var(--font-mono);
  border: 1px solid var(--border);
  padding: 1.25rem;
  margin: 1rem 0;
  background: var(--card-bg);
  overflow-x: auto;
}

.tree-root-label {
  font-weight: 700;
  font-size: 1rem;
  margin-bottom: 0.5rem;
  display: block;
}

.tree-list {
  list-style: none;
  padding-left: 0;
}

.tree-node {
  margin: 0.25rem 0;
}

.tree-branch {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  white-space: nowrap;
}

.tree-symbol {
  color: var(--tree-line);
  user-select: none;
  font-weight: 600;
}

.tree-link {
  color: var(--link);
  text-decoration: underline;
  font-weight: 600;
}

.tree-link:hover {
  color: var(--text);
}

.tree-children {
  list-style: none;
  padding-left: 1.5rem;
  margin-top: 0.15rem;
  border-left: 1px dashed var(--tree-line);
  margin-left: 0.5rem;
}

/* Section Blocks */
.section-block {
  margin: 1.25rem 0;
  border: 1px solid var(--border);
  padding: 1rem;
  background: var(--bg);
}

.section-title {
  font-family: var(--font-mono);
  font-size: 1rem;
  font-weight: 700;
  text-transform: uppercase;
  border-bottom: 1px solid var(--border-light);
  padding-bottom: 0.4rem;
  margin-bottom: 0.75rem;
}

/* Actionable instruction lists */
.action-list {
  list-style: none;
  padding: 0;
}

.action-list li {
  position: relative;
  padding-left: 1.25rem;
  margin-bottom: 0.5rem;
}

.action-list li::before {
  content: ">";
  position: absolute;
  left: 0;
  font-family: var(--font-mono);
  font-weight: bold;
  color: var(--muted);
}

/* Interactive Checklists */
.checklist {
  list-style: none;
  padding: 0;
}

.checklist-item {
  display: flex;
  align-items: flex-start;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
  cursor: pointer;
  padding: 0.25rem 0;
}

.checklist-item input[type="checkbox"] {
  margin-top: 0.2rem;
  cursor: pointer;
  accent-color: var(--text);
  width: 1rem;
  height: 1rem;
}

.checklist-item.checked span {
  text-decoration: line-through;
  color: var(--muted);
}

/* PDF Embed Container */
.pdf-container {
  margin: 1.5rem 0;
  border: 1px solid var(--border);
  background: var(--card-bg);
  padding: 0.75rem;
}

.pdf-toolbar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid var(--border-light);
  font-family: var(--font-mono);
  font-size: 0.85rem;
}

.pdf-btn {
  display: inline-block;
  background: var(--text);
  color: var(--bg);
  padding: 0.35rem 0.75rem;
  text-decoration: none;
  font-weight: 600;
  font-family: var(--font-mono);
  font-size: 0.8rem;
  border: 1px solid var(--text);
  cursor: pointer;
}

.pdf-btn:hover {
  background: transparent;
  color: var(--text);
}

.pdf-viewer-frame {
  width: 100%;
  height: 650px;
  min-height: 480px;
  border: 1px solid var(--border-light);
  background: #ffffff;
  display: block;
}

.mobile-fallback-note {
  margin-top: 0.4rem;
  font-size: 0.8rem;
  color: var(--muted);
  font-family: var(--font-mono);
}

/* 2-column responsive layout */
.grid-2 {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}

@media (min-width: 768px) {
  .grid-2 {
    grid-template-columns: 1fr 1fr;
  }
}

/* Minimal Footer */
footer {
  margin-top: 2.5rem;
  padding-top: 1rem;
  border-top: 1px dashed var(--border-light);
  font-family: var(--font-mono);
  font-size: 0.85rem;
}

footer a {
  color: var(--link);
  text-decoration: underline;
}

/* Buttons */
.btn {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.85rem;
  padding: 0.35rem 0.75rem;
  border: 1px solid var(--border);
  text-decoration: none;
  color: var(--text);
  background: var(--card-bg);
}

.btn:hover {
  background: var(--border);
  color: var(--bg);
}

/* Mobile responsive rules */
@media (max-width: 600px) {
  body {
    padding: 1rem 0.75rem 2.5rem 0.75rem;
  }
  
  .tree-view {
    padding: 0.75rem;
  }
  
  .tree-children {
    padding-left: 1.1rem;
    margin-left: 0.25rem;
  }

  .pdf-viewer-frame {
    height: 420px;
    min-height: 380px;
  }
  
  .pdf-toolbar {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .pdf-btn {
    width: 100%;
    text-align: center;
  }
}
"""

with open(os.path.join(BASE_DIR, "css", "style.css"), "w", encoding="utf-8") as f:
    f.write(CSS_CONTENT)

# 3. Inlined head snippet to prevent theme flash
THEME_INIT_SCRIPT = "<script>(function(){const t=localStorage.getItem('theme');if(t){document.documentElement.setAttribute('data-theme',t);}})();</script>"

# 4. Helper to generate Quick Nav
def make_quick_nav(current_id=None, depth=0):
    root_prefix = "../" * depth if depth > 0 else "./"
    items = []
    for s in SUBJECTS:
        s_href = f"{root_prefix}{s['id']}/index.html"
        items.append(f'<a href="{s_href}">{s["name"]}</a>')
    return f"""<nav class="quick-nav">
  {' / '.join(items)}
</nav>"""

# 5. Helper to generate Minimal Footer
def make_footer(depth=0):
    root_prefix = "../" * depth if depth > 0 else "./"
    if depth == 0:
        return ""
    return f"""<footer>
  <a href="{root_prefix}index.html">&larr; home</a>
</footer>"""

# 6. Generate Root index.html
home_tree_html = []
for idx, s in enumerate(SUBJECTS):
    is_last = (idx == len(SUBJECTS) - 1)
    branch_sym = "└──" if is_last else "├──"
    
    # Children for subject
    children_html = []
    has_practical = s.get("practical") is not None
    
    assign_sym = "└──" if not has_practical else "├──"
    extra_tag = '<span style="color: var(--muted); font-size: 0.82rem; margin-left: 0.35rem;">[due 23 nov 2026 &bull; separate notebook]</span>' if s['id'] == 'dld' else ''
    children_html.append(f"""
        <li class="tree-node">
          <div class="tree-branch">
            <span class="tree-symbol">{assign_sym}</span>
            <a class="tree-link" href="{s['id']}/assignments/index.html">assignments/</a>
            {extra_tag}
          </div>
        </li>""")
    
    if has_practical:
        children_html.append(f"""
        <li class="tree-node">
          <div class="tree-branch">
            <span class="tree-symbol">└──</span>
            <a class="tree-link" href="{s['id']}/practical-lab-record/index.html">practical lab record/</a>
          </div>
        </li>""")

    home_tree_html.append(f"""
    <li class="tree-node tree-node-subject">
      <div class="tree-branch">
        <span class="tree-symbol">{branch_sym}</span>
        <a class="tree-link" href="{s['id']}/index.html">{s['name']}/</a>
      </div>
      <ul class="tree-children">
        {''.join(children_html)}
      </ul>
    </li>""")

ROOT_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>./</title>
  {THEME_INIT_SCRIPT}
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <div class="container">
    <header>
      <div class="header-top">
        <h1 class="site-title">./</h1>
        <button id="theme-toggle" class="theme-btn" type="button" aria-label="Toggle theme">theme</button>
      </div>
    </header>

    {make_quick_nav(None, depth=0)}

    <!-- Active Deadline Notice -->
    <div class="notice-box">
      <p><strong>active deadline:</strong> dld assignments due 23 november 2026 (to be done on a separate notebook)</p>
    </div>

    <div class="filter-box">
      <input type="text" id="tree-filter" class="filter-input" placeholder="filter subjects (discrete, dld, ppl, dev tools, dsa)..." autocomplete="off">
    </div>

    <main>
      <section class="tree-view">
        <span class="tree-root-label">./</span>
        <ul class="tree-list">
          {''.join(home_tree_html)}
        </ul>
      </section>
    </main>
  </div>

  <script src="js/app.js"></script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(ROOT_HTML)

# 7. Generate Subject Hub Pages (e.g. discrete/index.html)
for s in SUBJECTS:
    sub_dir = os.path.join(BASE_DIR, s['id'])
    os.makedirs(sub_dir, exist_ok=True)
    has_practical = s.get("practical") is not None

    tree_children = []
    assign_sym = "└──" if not has_practical else "├──"
    tree_children.append(f"""
          <li class="tree-node">
            <div class="tree-branch">
              <span class="tree-symbol">{assign_sym}</span>
              <a class="tree-link" href="assignments/index.html">assignments/</a>
            </div>
          </li>""")
    if has_practical:
        tree_children.append("""
          <li class="tree-node">
            <div class="tree-branch">
              <span class="tree-symbol">└──</span>
              <a class="tree-link" href="practical-lab-record/index.html">practical lab record/</a>
            </div>
          </li>""")

    # Section cards
    if has_practical:
        cards_html = """
      <div class="grid-2">
        <div class="section-block">
          <h2 class="section-title">assignments</h2>
          <div style="margin-top: 0.5rem;">
            <a href="assignments/index.html" class="btn">open assignments/ &rarr;</a>
          </div>
        </div>

        <div class="section-block">
          <h2 class="section-title">practical lab record</h2>
          <div style="margin-top: 0.5rem;">
            <a href="practical-lab-record/index.html" class="btn">open practical lab record/ &rarr;</a>
          </div>
        </div>
      </div>"""
    else:
        cards_html = """
      <div class="section-block">
        <h2 class="section-title">assignments</h2>
        <div style="margin-top: 0.5rem;">
          <a href="assignments/index.html" class="btn">open assignments/ &rarr;</a>
        </div>
      </div>"""

    SUB_PAGE_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{s['name']}</title>
  {THEME_INIT_SCRIPT}
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>
  <div class="container">
    <header>
      <div class="header-top">
        <div class="breadcrumbs">
          <a href="../index.html">home</a>
          <span class="sep">/</span>
          <span class="current">{s['name']}</span>
        </div>
        <button id="theme-toggle" class="theme-btn" type="button" aria-label="Toggle theme">theme</button>
      </div>
      <h1 class="site-title">{s['name']}</h1>
    </header>

    {make_quick_nav(s['id'], depth=1)}

    <main>
      <section class="tree-view">
        <span class="tree-root-label">{s['name']}/</span>
        <ul class="tree-list">
          {''.join(tree_children)}
        </ul>
      </section>
      {cards_html}
    </main>

    {make_footer(depth=1)}
  </div>

  <script src="../js/app.js"></script>
</body>
</html>
"""
    if s['id'] == 'dld' and os.path.exists(os.path.join(sub_dir, "index.html")):
        # Preserving custom dld hub with deadline notice
        pass
    else:
        with open(os.path.join(sub_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(SUB_PAGE_HTML)

# 8. Generate Subpages: assignments/index.html & practical-lab-record/index.html
for s in SUBJECTS:
    # 8a. assignments (all subjects have assignments)
    assign_dir = os.path.join(BASE_DIR, s['id'], "assignments")
    os.makedirs(assign_dir, exist_ok=True)
    assign_data = s["assignments"]

    what_to_do_items = "".join([f"<li>{item}</li>" for item in assign_data["what_to_do"]])
    what_to_write_items = "".join([f"<li>{item}</li>" for item in assign_data["what_to_write"]])
    guidelines_items = "".join([
        f'<label class="checklist-item"><input type="checkbox"><span>{item}</span></label>'
        for item in assign_data["submission_guidelines"]
    ])

    ASSIGN_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{s['name']} // assignments</title>
  {THEME_INIT_SCRIPT}
  <link rel="stylesheet" href="../../css/style.css">
</head>
<body>
  <div class="container">
    <header>
      <div class="header-top">
        <div class="breadcrumbs">
          <a href="../../index.html">home</a>
          <span class="sep">/</span>
          <a href="../index.html">{s['name']}</a>
          <span class="sep">/</span>
          <span class="current">assignments</span>
        </div>
        <button id="theme-toggle" class="theme-btn" type="button" aria-label="Toggle theme">theme</button>
      </div>
      <h1 class="site-title">{s['name']} // assignments</h1>
    </header>

    {make_quick_nav(s['id'], depth=2)}

    <main>
      <div class="grid-2">
        <section class="section-block">
          <h2 class="section-title">What To Do</h2>
          <ul class="action-list">
            {what_to_do_items}
          </ul>
        </section>

        <section class="section-block">
          <h2 class="section-title">What To Write</h2>
          <ul class="action-list">
            {what_to_write_items}
          </ul>
        </section>
      </div>

      <section class="section-block">
        <h2 class="section-title">Checklist</h2>
        <div class="checklist">
          {guidelines_items}
        </div>
      </section>

      <section class="pdf-container">
        <div class="pdf-toolbar">
          <div>
            <strong>{s['name']}/assignments.pdf</strong>
          </div>
          <div>
            <a href="{assign_data['pdf_rel_path']}" target="_blank" rel="noopener noreferrer" class="pdf-btn">
              Open PDF / Download
            </a>
          </div>
        </div>

        <iframe 
          src="{assign_data['pdf_rel_path']}" 
          class="pdf-viewer-frame"
          title="{s['name']} assignments PDF">
          <p><a href="{assign_data['pdf_rel_path']}" target="_blank">Open PDF</a></p>
        </iframe>
        
        <p class="mobile-fallback-note">
          Mobile: tap "Open PDF / Download" above if inline preview does not scroll.
        </p>
      </section>
    </main>

    {make_footer(depth=2)}
  </div>

  <script src="../../js/app.js"></script>
</body>
</html>
"""
    if s['id'] == 'dld' and os.path.exists(os.path.join(assign_dir, "index.html")):
        # Preserving custom rich dld assignments page
        pass
    else:
        with open(os.path.join(assign_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(ASSIGN_HTML)

    # 8b. practical-lab-record (only if practical is defined!)
    if s.get("practical") is not None:
        pract_dir = os.path.join(BASE_DIR, s['id'], "practical-lab-record")
        os.makedirs(pract_dir, exist_ok=True)
        pract_data = s["practical"]

        p_what_to_do = "".join([f"<li>{item}</li>" for item in pract_data["what_to_do"]])
        p_what_to_write = "".join([f"<li>{item}</li>" for item in pract_data["what_to_write"]])
        p_guidelines = "".join([
            f'<label class="checklist-item"><input type="checkbox"><span>{item}</span></label>'
            for item in pract_data["submission_guidelines"]
        ])

        PRACT_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{s['name']} // practical lab record</title>
  {THEME_INIT_SCRIPT}
  <link rel="stylesheet" href="../../css/style.css">
</head>
<body>
  <div class="container">
    <header>
      <div class="header-top">
        <div class="breadcrumbs">
          <a href="../../index.html">home</a>
          <span class="sep">/</span>
          <a href="../index.html">{s['name']}</a>
          <span class="sep">/</span>
          <span class="current">practical lab record</span>
        </div>
        <button id="theme-toggle" class="theme-btn" type="button" aria-label="Toggle theme">theme</button>
      </div>
      <h1 class="site-title">{s['name']} // practical lab record</h1>
    </header>

    {make_quick_nav(s['id'], depth=2)}

    <main>
      <div class="grid-2">
        <section class="section-block">
          <h2 class="section-title">What To Do</h2>
          <ul class="action-list">
            {p_what_to_do}
          </ul>
        </section>

        <section class="section-block">
          <h2 class="section-title">What To Write</h2>
          <ul class="action-list">
            {p_what_to_write}
          </ul>
        </section>
      </div>

      <section class="section-block">
        <h2 class="section-title">Checklist</h2>
        <div class="checklist">
          {p_guidelines}
        </div>
      </section>

      <section class="pdf-container">
        <div class="pdf-toolbar">
          <div>
            <strong>{s['name']}/practical-lab-record.pdf</strong>
          </div>
          <div>
            <a href="{pract_data['pdf_rel_path']}" target="_blank" rel="noopener noreferrer" class="pdf-btn">
              Open PDF / Download
            </a>
          </div>
        </div>

        <iframe 
          src="{pract_data['pdf_rel_path']}" 
          class="pdf-viewer-frame"
          title="{s['name']} practical lab record PDF">
          <p><a href="{pract_data['pdf_rel_path']}" target="_blank">Open PDF</a></p>
        </iframe>
        
        <p class="mobile-fallback-note">
          Mobile: tap "Open PDF / Download" above if inline preview does not scroll.
        </p>
      </section>
    </main>

    {make_footer(depth=2)}
  </div>

  <script src="../../js/app.js"></script>
</body>
</html>
"""
        with open(os.path.join(pract_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(PRACT_HTML)

print("Regeneration complete!")
