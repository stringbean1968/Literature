import os
import shutil

BASE = "/home/runner/work/Literature/Literature/Conform/PrudentiaAedificatoria/Overleaf"

def w(path, content):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w') as f:
        f.write(content)
    print(f"Written: {path}")

# Empty files
open(os.path.join(BASE, "../Artefact/.gitkeep"), 'w').close()
open(os.path.join(BASE, "Preamble.tex"), 'w').close()

# Copy commands.tex
src = "/home/runner/work/Literature/Literature/Conform/PrudentiaVeterinaria/Overleaf/01_Primary/commands.tex"
shutil.copy(src, os.path.join(BASE, "01_Primary/commands.tex"))
print("Copied commands.tex")

# Copy Main Outline For Chapters.txt
src2 = "/home/runner/work/Literature/Literature/Conform/PrudentiaVeterinaria/Main Outline For Chapters.txt"
shutil.copy(src2, os.path.join(BASE, "Main Outline For Chapters.txt"))
print("Copied Main Outline For Chapters.txt")

# main.tex
w("01_Primary/main.tex", r"""\documentclass[oneside]{book}

% Packages
\usepackage{fontspec}
\usepackage{graphicx} % Required for inserting images
\usepackage{titlesec}
\usepackage[top=2.5cm, bottom=2.5cm, left=2.5cm,right=2.5cm]{geometry}

% paragraph management, space after each with no first line indent
\usepackage{parskip}

% provides formatting for coloured bars etc
\usepackage{tcolorbox}
\usepackage{mdframed}
\usepackage{enumitem}
\usepackage{xparse}
\usepackage{changepage}

\usepackage{tabularx}
\usepackage{booktabs}        % For nicer horizontal rules
\usepackage{float}

\tcbuselibrary{skins}

% paragraph management, space after each with no first line indent
\setlength{\parskip}{14pt}   % Adjust to taste

\newmdenv[
  topline=false,
  bottomline=false,
  rightline=false,
  leftline=true,
  linewidth=3pt,
  linecolor=gray!60,
  backgroundcolor=white,
  leftmargin=20pt,
  rightmargin=20pt,
  innerleftmargin=10pt,
  innertopmargin=4pt,
  innerbottommargin=4pt,
  skipabove=12pt,
  skipbelow=12pt,
  fontcolor=black,
]{quotebar}

\setmainfont{TeX Gyre Heros}

% Format: smaller font, bold, with chapter number
\titleformat{\chapter}[hang]
  {\normalfont\Large\bfseries}   % <-- Change \Large to suit your preference
  {\thechapter}
  {10pt}                         % Space between "Chapter X" label and title text
  {}                             % Code before title text

% Spacing: {left}{space ABOVE title}{space BELOW title}
\titlespacing*{\chapter}
  {0pt}     % left indent
  {0cm}    % space ABOVE (adjust to taste)
  {12pt}    % space BELOW -- small gap after chapter title

\titleformat{\paragraph}[runin]{\normalfont}{\theparagraph}{1em}{}

\pagestyle{plain}

\begin{document}
\include{01_Primary/commands}

\title{
  {\Huge\bfseries Prudentia} \\[6pt]
  {\LARGE\itshape Aedificatoria} \\[10pt]
  {\Large Risk Assessment for Construction, Trades, and Building Services}
}
\author{Paul Stringer.}
\date{}
\maketitle
\include{Introduction/Introduction}
%\tableofcontents
\paragraph{TOC Goes Here}
\newpage
\include{Part1/Part1}
\include{Part1/Chapter1}
\include{Part1/Chapter2}
\include{Part1/Chapter3}
\include{Part1/Chapter4}
\include{Part2/Part2}
\include{Part2/Chapter5}
\include{Part2/Chapter6}
\include{Part2/Chapter7}
\include{Part2/Chapter8}
\include{Part2/Chapter9}
\include{Part2/Chapter10}
\include{Part3/Part3}
\include{Part3/Chapter11}
\include{Part3/Chapter12}
\include{Part3/Chapter13}
\include{Part4/Part4}
\include{Part4/Chapter14}
\include{Part4/Chapter15}
\include{Part4/Chapter16}
\include{Part4/Chapter17}
\include{Part4/Chapter18}
\include{Part4/Chapter19}
\include{Part5/Part5}
\include{Part5/Chapter20}
\include{Part5/Chapter21}
\include{Part5/Chapter22}
\include{Part5/Chapter23}
\include{Part6/Part6}
\include{Part6/Chapter24}
\include{Part6/Chapter25}
\include{Part6/Chapter26}
\include{Part7/Part7}
\include{Part7/Chapter27}
\include{Part7/Chapter28}
\include{Part8/Part8}
\include{Part8/Chapter29}
\include{Part8/Chapter30}
\include{X_Appendices/Appendices}
\include{X_Appendices/AppendixA}
\include{X_Appendices/AppendixB}
\include{X_Appendices/AppendixC}
\include{X_Appendices/AppendixD}
\end{document}
""")

# Introduction
w("Introduction/Introduction.tex", r"""\chapter{Introduction}
\label{chap:Introduction}

%---------------------------- SECTION ----------------------------
\section{A Sister Volume to \textit{Prudentia}}

\paragraph{This book is one of a planned series. The base volume, \textit{Prudentia}, sets out the profession-agnostic method. Each subsequent volume applies that method to a single sector. \textit{Prudentia Aedificatoria} is the construction and trades volume.}

\paragraph{\textit{Prudentia Aedificatoria} applies the same five-step risk assessment framework to the specific hazards, regulatory duties, and operational patterns of construction companies, trade contractors, building services firms, and sole traders working in the built environment.}

\paragraph{Construction remains one of the UK's highest-risk industries. Fatal injury rates, occupational disease burden, and enforcement action all remain disproportionately high relative to the wider workforce. This book is designed to help practitioners build assessments that are defensible, proportionate, and genuinely embedded in site operations rather than stored in an office filing cabinet.}

\paragraph{This volume assumes that your goal is not merely to satisfy an inspector, but to run safer sites and more resilient businesses. Compliance is treated as a floor, not a ceiling.}

%---------------------------- SECTION ----------------------------
\section{Who this book is for}

\paragraph{\textit{Prudentia Aedificatoria} is written for construction company owners, site managers, principal contractors, health and safety advisers, CDM coordinators, self-employed trades, and professional risk assessors who carry accountability for risk decisions in the built environment.}

\paragraph{The intended reader includes not only the compliance specialist but the working tradesperson who must make real-time risk decisions without formal H\&S support at hand, the site manager who assigns work and supervises contractors, and the governance lead who must assure a board or client that the risk function is operating effectively.}

%---------------------------- SECTION ----------------------------
\section{Methodology used in this book}

\paragraph{This volume applies the \textit{Prudentia} five-step method directly to construction and trades contexts: identify hazards, determine who is affected, evaluate risk, select controls, and record and review. The value of the method lies in its repeatability and comparability across different sites and trades.}

\paragraph{Every chapter uses the same structure: contextual framing, legal and professional framework, five-step application, hierarchy of controls, assessment cadence and triggers, common failure modes, and a summary table. This repeating rhythm supports delegation, toolbox talk delivery, and governance oversight.}

\barquote{A risk assessment that cannot be understood on site is not a risk assessment. It is a filing obligation.}

%---------------------------- SECTION ----------------------------
\section{Legal context and devolved variation}

\paragraph{\textit{Prudentia Aedificatoria} is UK-centred. It references the Health and Safety at Work etc.\ Act 1974, the Construction (Design and Management) Regulations 2015, and the full suite of sector-specific regulations that apply to UK construction and trades work.}

\paragraph{CDM 2015 applies across Great Britain. Northern Ireland operates under the Construction (Design and Management) Regulations (Northern Ireland) 2016, which broadly mirror the GB regulations. Fire safety legislation and environmental regulation have devolved elements across England, Scotland, Wales, and Northern Ireland that practitioners operating across borders must track.}

\paragraph{Where precise citation detail has not been independently verified, this volume states obligations in practical terms. Practitioners should maintain current legal mapping and update assessments as statutory guidance evolves.}

%---------------------------- SECTION ----------------------------
\section{How to use Prudentia Aedificatoria in governance}

\paragraph{Use this book as a build tool, an audit benchmark, and a training framework. Build chapter-aligned assessments for operational depth, then aggregate residual risk and action status into a company-level risk register for management review.}

\paragraph{For pre-construction phase plan preparation, the assessments in Parts I, II, III, and IV provide the raw material for site-specific risk identification. F10 notification timing, Principal Contractor obligations, and construction phase plan content are addressed directly in the relevant chapters.}

\paragraph{For continuous improvement, apply the scheduled review cadences from the Cadence Matrix (Appendix B) and tighten review frequency where residual risk remains high, operating conditions change, or incidents occur. Integrate chapter outputs with toolbox talks, site inspections, near-miss reporting, and management review cycles.}

\barquote{In Chapter~\ref{chap:What is Risk in a Construction and Trades Context?}, we begin by defining risk in specifically construction terms and setting the language and scope for the whole volume.}
""")

# Part headers
w("Part1/Part1.tex", r"\part{Foundations of Risk in Construction and Trades}")
w("Part2/Part2.tex", r"\part{Physical Hazards on Site}")
w("Part3/Part3.tex", r"\part{Hazardous Substances and Agents}")
w("Part4/Part4.tex", r"\part{Utilities, Energy and Environmental Hazards}")
w("Part5/Part5.tex", r"\part{Specialist Works and High-Risk Activities}")
w("Part6/Part6.tex", r"\part{People, Welfare and Occupational Health}")
w("Part7/Part7.tex", r"\part{Governance, Compliance and Business Risk}")
w("Part8/Part8.tex", r"\part{Continuous Improvement and Programme Governance}")
w("X_Appendices/Appendices.tex", "\\appendix\n\\part{Appendices}")

print("Part headers done.")
