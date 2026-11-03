%% tandf.cls
%% LaTeX class reconstructed from the official Taylor & Francis Word template
%% (TF_Template_Word_Windows_2016.dotx), downloaded from
%% https://authorservices.taylorandfrancis.com/publishing-your-research/writing-your-paper/formatting-and-templates/
%% Page size, margins, fonts, and heading styles follow the .docx styles.
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{tandf}[2026/11/03 v1.0 Taylor & Francis Word-template conversion]

\LoadClass[12pt,a4paper]{article}

\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}
\RequirePackage{mathptmx} % Times New Roman-like text and math
\RequirePackage[a4paper,top=2.5cm,bottom=2.5cm,left=3cm,right=3cm,headheight=14pt]{geometry}
\RequirePackage{setspace}
\RequirePackage{titlesec}
\RequirePackage{fancyhdr}
\RequirePackage{graphicx}
\RequirePackage{booktabs}
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage{natbib}
\RequirePackage[hidelinks]{hyperref}

\doublespacing

\setcounter{secnumdepth}{0}

\newcommand{\@journal}{}
\newcommand{\journal}[1]{\gdef\@journal{#1}}
\newcommand{\@affiliation}{}
\newcommand{\affiliation}[1]{\gdef\@affiliation{#1}}

\renewcommand{\maketitle}{%
  \begin{flushleft}%
    {\fontsize{14}{17}\selectfont\bfseries \@title\par}%
    \vspace{6pt}%
    {\fontsize{14}{17}\selectfont \@author\par}%
    \vspace{6pt}%
    {\fontsize{12}{14}\selectfont\itshape \@affiliation\par}%
  \end{flushleft}%
}

\renewenvironment{abstract}{%
  \par\vspace{12pt}%
  \begin{list}{}{%
    \setlength{\leftmargin}{1.27cm}%
    \setlength{\rightmargin}{1cm}%
    \setlength{\listparindent}{0pt}%
    \setlength{\itemindent}{0pt}%
    \setlength{\parsep}{0pt}%
    \setlength{\topsep}{0pt}%
  }%
  \item\relax\begin{spacing}{1.5}\fontsize{11}{16.5}\selectfont\selectfont
}{%
  \end{spacing}%
  \end{list}%
  \par\vspace{6pt}%
}

\newcommand{\keywords}[1]{%
  \par\vspace{6pt}%
  \noindent\hspace*{1.27cm}\begin{minipage}{\dimexpr\linewidth-2.27cm\relax}%
  \fontsize{11}{16.5}\selectfont\selectfont\textbf{Keywords:} #1%
  \end{minipage}\par\vspace{12pt}%
}

\titleformat{\section}{\normalfont\bfseries\fontsize{12}{14}\selectfont}{}{0pt}{}
\titlespacing*{\section}{0pt}{18pt}{3pt}
\titleformat{\subsection}{\normalfont\bfseries\itshape\fontsize{12}{14}\selectfont}{}{0pt}{}
\titlespacing*{\subsection}{0pt}{18pt}{3pt}
\titleformat{\subsubsection}{\normalfont\itshape\fontsize{12}{14}\selectfont}{}{0pt}{}
\titlespacing*{\subsubsection}{0pt}{18pt}{3pt}
\titleformat{\paragraph}[runin]{\normalfont\itshape\fontsize{12}{14}\selectfont}{}{0pt}{}
\titlespacing*{\paragraph}{0pt}{18pt}{0pt}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\fontsize{9}{11}\selectfont\itshape\@journal}
\fancyhead[R]{\fontsize{9}{11}\selectfont\thepage}
\renewcommand{\headrulewidth}{0pt}
\fancypagestyle{plain}{%
  \fancyhf{}%
  \fancyhead[L]{\fontsize{9}{11}\selectfont\itshape\@journal}%
  \fancyhead[R]{\fontsize{9}{11}\selectfont\thepage}%
  \renewcommand{\headrulewidth}{0pt}%
}

\AtBeginDocument{%
  \fontsize{12}{24}\selectfont\selectfont
}

\renewcommand{\refname}{References}
\setlength{\bibsep}{0pt}
