TOP=..

include $(TOP)/configure/CONFIG

PYTHON ?= python$(PY_VER)

TARGETS = $(CONFIG_TARGETS)

ifdef T_A
CONFIGS = os/CONFIG_PY.Common.$(T_A)
ifdef BASE_7_0
# Base 3.14 and 3.15 cannot use the cfg folder.
CFG = CONFIG_PY RULES_PY os/CONFIG_PY.Common.$(T_A)
else
CONFIGS += CONFIG_PY RULES_PY
endif

endif

CONFIGS += $(subst ../,,$(wildcard $(CONFIG_INSTALLS)))

include $(TOP)/configure/RULES

os/CONFIG_PY.Common.$(T_A): $(TOP)/makehelper.py
	$(PYTHON) $< $@

ifdef BASE_3_15
realclean: py_clean
else
realclean:: py_clean
endif

py_clean:
	$(RMDIR) os
