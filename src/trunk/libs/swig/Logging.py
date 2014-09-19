# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_Logging', [dirname(__file__)])
        except ImportError:
            import _Logging
            return _Logging
        if fp is not None:
            try:
                _mod = imp.load_module('_Logging', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _Logging = swig_import_helper()
    del swig_import_helper
else:
    import _Logging
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


SEISCOMP_COMPONENT = _Logging.SEISCOMP_COMPONENT
LL_UNDEFINED = _Logging.LL_UNDEFINED
LL_CRITICAL = _Logging.LL_CRITICAL
LL_ERROR = _Logging.LL_ERROR
LL_WARNING = _Logging.LL_WARNING
LL_NOTICE = _Logging.LL_NOTICE
LL_INFO = _Logging.LL_INFO
LL_DEBUG = _Logging.LL_DEBUG
LL_QUANTITY = _Logging.LL_QUANTITY

def debug(*args):
  return _Logging.debug(*args)
debug = _Logging.debug

def info(*args):
  return _Logging.info(*args)
info = _Logging.info

def warning(*args):
  return _Logging.warning(*args)
warning = _Logging.warning

def error(*args):
  return _Logging.error(*args)
error = _Logging.error

def notice(*args):
  return _Logging.notice(*args)
notice = _Logging.notice

def log(*args):
  return _Logging.log(*args)
log = _Logging.log

def getAll():
  return _Logging.getAll()
getAll = _Logging.getAll

def getGlobalChannel(*args):
  return _Logging.getGlobalChannel(*args)
getGlobalChannel = _Logging.getGlobalChannel

def getComponentChannel(*args):
  return _Logging.getComponentChannel(*args)
getComponentChannel = _Logging.getComponentChannel

def getComponentAll(*args):
  return _Logging.getComponentAll(*args)
getComponentAll = _Logging.getComponentAll

def getComponentDebugs(*args):
  return _Logging.getComponentDebugs(*args)
getComponentDebugs = _Logging.getComponentDebugs

def getComponentInfos(*args):
  return _Logging.getComponentInfos(*args)
getComponentInfos = _Logging.getComponentInfos

def getComponentWarnings(*args):
  return _Logging.getComponentWarnings(*args)
getComponentWarnings = _Logging.getComponentWarnings

def getComponentErrors(*args):
  return _Logging.getComponentErrors(*args)
getComponentErrors = _Logging.getComponentErrors

def getComponentNotices(*args):
  return _Logging.getComponentNotices(*args)
getComponentNotices = _Logging.getComponentNotices

def consoleOutput():
  return _Logging.consoleOutput()
consoleOutput = _Logging.consoleOutput

def enableConsoleLogging(*args):
  return _Logging.enableConsoleLogging(*args)
enableConsoleLogging = _Logging.enableConsoleLogging

def disableConsoleLogging():
  return _Logging.disableConsoleLogging()
disableConsoleLogging = _Logging.disableConsoleLogging

def init(*args):
  return _Logging.init(*args)
init = _Logging.init
class Output(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Output, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Output, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _Logging.delete_Output
    __del__ = lambda self : None;
    def subscribe(self, *args): return _Logging.Output_subscribe(self, *args)
    def unsubscribe(self, *args): return _Logging.Output_unsubscribe(self, *args)
    def logComponent(self, *args): return _Logging.Output_logComponent(self, *args)
    def logContext(self, *args): return _Logging.Output_logContext(self, *args)
Output_swigregister = _Logging.Output_swigregister
Output_swigregister(Output)

class FdOutput(Output):
    __swig_setmethods__ = {}
    for _s in [Output]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, FdOutput, name, value)
    __swig_getmethods__ = {}
    for _s in [Output]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, FdOutput, name)
    __repr__ = _swig_repr
    def __init__(self, fdOut=2): 
        this = _Logging.new_FdOutput(fdOut)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Logging.delete_FdOutput
    __del__ = lambda self : None;
FdOutput_swigregister = _Logging.FdOutput_swigregister
FdOutput_swigregister(FdOutput)

class FileOutput(Output):
    __swig_setmethods__ = {}
    for _s in [Output]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, FileOutput, name, value)
    __swig_getmethods__ = {}
    for _s in [Output]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, FileOutput, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _Logging.new_FileOutput(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Logging.delete_FileOutput
    __del__ = lambda self : None;
    def open(self, *args): return _Logging.FileOutput_open(self, *args)
    def isOpen(self): return _Logging.FileOutput_isOpen(self)
FileOutput_swigregister = _Logging.FileOutput_swigregister
FileOutput_swigregister(FileOutput)

class FileRotatorOutput(FileOutput):
    __swig_setmethods__ = {}
    for _s in [FileOutput]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, FileRotatorOutput, name, value)
    __swig_getmethods__ = {}
    for _s in [FileOutput]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, FileRotatorOutput, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _Logging.new_FileRotatorOutput(*args)
        try: self.this.append(this)
        except: self.this = this
    def open(self, *args): return _Logging.FileRotatorOutput_open(self, *args)
    __swig_destroy__ = _Logging.delete_FileRotatorOutput
    __del__ = lambda self : None;
FileRotatorOutput_swigregister = _Logging.FileRotatorOutput_swigregister
FileRotatorOutput_swigregister(FileRotatorOutput)

class SyslogOutput(Output):
    __swig_setmethods__ = {}
    for _s in [Output]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SyslogOutput, name, value)
    __swig_getmethods__ = {}
    for _s in [Output]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, SyslogOutput, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _Logging.new_SyslogOutput(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Logging.delete_SyslogOutput
    __del__ = lambda self : None;
    def facility(self): return _Logging.SyslogOutput_facility(self)
    def open(self, *args): return _Logging.SyslogOutput_open(self, *args)
    def isOpen(self): return _Logging.SyslogOutput_isOpen(self)
    def close(self): return _Logging.SyslogOutput_close(self)
SyslogOutput_swigregister = _Logging.SyslogOutput_swigregister
SyslogOutput_swigregister(SyslogOutput)

# This file is compatible with both classic and new-style classes.


