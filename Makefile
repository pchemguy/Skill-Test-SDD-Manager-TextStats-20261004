PYTHON ?= python
DIST_DIR ?= dist

.PHONY: dist check

# Explicit package/test files keep bytecode caches and workflow resources out.
dist:
	mkdir -p "$(DIST_DIR)"
	$(PYTHON) -m tarfile -c "$(DIST_DIR)/textstats.tar.gz" textstats/*.py README.md Makefile AI_DISCLOSURE.md SDD-MANAGER.md docs tests/__init__.py tests/unit/*.py tests/integration/*.py

check:
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -m unittest discover -s tests/unit -t . -v
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -m unittest discover -s tests/integration -t . -v
