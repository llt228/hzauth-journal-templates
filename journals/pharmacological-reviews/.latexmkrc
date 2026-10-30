# latexmk configuration for this journal template.
# Build with pdflatex + BibTeX.
$pdf_mode = 1;
$bibtex_use = 2;
$pdflatex = 'pdflatex -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
$clean_ext = 'bbl blg run.xml synctex.gz nav snm vrb';
