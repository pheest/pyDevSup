#!../../bin/linux-x86_64/softIocPy3.6

< envPaths

dbLoadRecords("../../db/logwatch.db","N=ACC-CT{}Log-I,FNAME=/var/log/epics/epics.log,FILTER=logwatch.caputlog")

iocInit()

dbl > records.dbl
