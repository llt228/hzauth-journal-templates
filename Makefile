.PHONY: build compile verify clean

build:
	python3 scripts/build.py

compile:
	bash scripts/compile_all.sh

verify:
	python3 scripts/verify.py

clean:
	find journals -name '*.aux' -o -name '*.log' -o -name '*.bbl' -o -name '*.blg' \
		-o -name '*.fls' -o -name '*.fdb_latexmk' -o -name '*.out' -o -name '*.toc' \
		-o -name '*.synctex.gz' | xargs -r rm -f
