TOP=..
include $(TOP)/configure/CONFIG
include $(TOP)/cfg/CONFIG_PY
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#----------------------------------------------------
#  Optimization of db files using dbst (DEFAULT: NO)
#DB_OPT = YES

#----------------------------------------------------
# Create and install (or just install) into <top>/db
# databases, templates, substitutions like this
DB += weather.db
PY += weather.py

#----------------------------------------------------
# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_template = <templatename>

include $(TOP)/configure/RULES
include $(TOP)/cfg/RULES_PY
#----------------------------------------
#  ADD RULES AFTER THIS LINE

