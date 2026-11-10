TOP=..
include $(TOP)/configure/CONFIG
ifndef BASE_7_0
include $(TOP)/configure/CONFIG_PY
endif
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

PY += bplreport.py
DB += applmetrics.db
DB += bplstorage.db

include $(TOP)/configure/RULES
ifndef BASE_7_0
include $(TOP)/configure/RULES_PY
endif
#----------------------------------------
#  ADD RULES AFTER THIS LINE
