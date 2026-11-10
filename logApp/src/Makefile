TOP=../..

include $(TOP)/configure/CONFIG
ifndef BASE_7_0
include $(TOP)/configure/CONFIG_PY
endif
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

LOADABLE_LIBRARY_HOST_Linux = _inotifyy

_inotifyy_SRCS += inotify_wrap.c

PY += inotifyy.py
PY += logwatch/__init__.py
PY += logwatch/caputlog.py

#===========================

include $(TOP)/configure/RULES
ifndef BASE_7_0
include $(TOP)/configure/RULES_PY
endif
#----------------------------------------
#  ADD RULES AFTER THIS LINE
