TOP=..

include $(TOP)/configure/CONFIG

PYTHON ?= python$(PY_VER)

TARGETS = $(CONFIG_TARGETS)

ifdef T_A
ifdef BASE_7_0
# We want the CONFIG_PY.Common.$(T_A) file to be created only in the 'cfg' and not in the 'configure' folder
CFG = CONFIG_PY RULES_PY os/CONFIG_PY.Common.$(T_A)
else
# Base 3.14 and 3.15 cannot use the cfg folder.
CONFIGS = CONFIG_PY RULES_PY os/CONFIG_PY.Common.$(T_A)
endif

os/CONFIG_PY.Common.$(T_A): $(TOP)/makehelper.py
	$(PYTHON) $< $@

endif

CONFIGS += $(subst ../,,$(wildcard $(CONFIG_INSTALLS)))

include $(TOP)/configure/RULES

ifdef BASE_3_15
realclean: py_clean
else
realclean:: py_clean
endif

py_clean:
	$(RMDIR) os
