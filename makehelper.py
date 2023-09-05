#!/usr/bin/env python
"""
Set some python derived Makefile variables.

Emits something like the following

PY_OK := YES  # indicates success of this script
HAVE_NUMPY := YES/NO
PY_VER := 2.6
PY_INCDIRS := /path ...
PY_LIBDIRS := /path ...
"""

from __future__ import print_function

import sys
import os

if len(sys.argv)<2:
    out = sys.stdout
else:
    try:
        os.makedirs(os.path.dirname(sys.argv[1]))
    except OSError:
        pass
    out = open(sys.argv[1], 'w')

from sysconfig import get_config_var
try:
    from distutils.sysconfig import get_python_inc, get_python_lib
except ImportError:
    def get_python_inc():
        return get_config_var('INCLUDEPY') or ''
    def get_python_lib():
        return get_config_var('LIBDIR') or get_config_var('LIBDEST') or '', \
               get_config_var('BINDIR') or '',
    

incdirs = [get_python_inc()]
libdirs = [get_python_lib()]

have_np='NO'
try:
    from numpy.distutils.misc_util import get_numpy_include_dirs
    incdirs = get_numpy_include_dirs()+incdirs
    have_np='YES'
except ImportError:
    pass

print('TARGET_CFLAGS +=',get_config_var('BASECFLAGS') or '', file=out)
print('TARGET_CXXFLAGS +=',get_config_var('BASECFLAGS') or '', file=out)

print('PY_VER :=',get_config_var('VERSION'), file=out)
ldver = get_config_var('LDVERSION')
if ldver is None:
    ldver = get_config_var('VERSION')
    if get_config_var('Py_DEBUG'):
        ldver = ldver+'_d'
print('PY_LD_VER :=',ldver, file=out)
print('PY_INCDIRS :=',' '.join(incdirs), file=out)
print('PY_LIBDIRS :=',' '.join(libdirs), file=out)
print('PY_LDLIBS :=', get_config_var('BLDLIBRARY') or '', file=out)
print('HAVE_NUMPY :=',have_np, file=out)

try:
    import asyncio
except ImportError:
    print('HAVE_ASYNCIO := NO', file=out)
else:
    print('HAVE_ASYNCIO := YES', file=out)

try:
    import cothread
except ImportError:
    print('HAVE_COTHREAD := NO', file=out)
else:
    print('HAVE_COTHREAD := YES', file=out)

print('PY_OK := YES', file=out)

out.close()
