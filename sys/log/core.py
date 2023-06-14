from abc import ABCMeta, abstractmethod
from typing import Callable
from core.core import error
from .options import Option,newOptions
from .log import newSys

class Ilogf(metaclass=ABCMeta):
    @abstractmethod
    def debugf(format:str, *args):
        pass
    @abstractmethod
    def infof(format:str, *args):
        pass
    @abstractmethod
    def printf(format:str, *args):
        pass
    @abstractmethod
    def warnf(format:str, *args):
        pass
    @abstractmethod
    def errorf(format:str, *args):
        pass
    @abstractmethod
    def fatalf(format:str, *args):
        pass
    @abstractmethod
    def panicf(format:str, *args):
        pass

class ILogger(Ilogf):
    pass


defsys:ILogger = None 

def onInit(config:dict,*opt:Option) -> error:
	return


def debugf(format:str, *args):
    defsys.debugf(format,args)
def infof(format:str, *args):
	defsys.infof(format,args)
def printf(format:str, *args):
    defsys.printf(format,args)
def warnf(format:str, *args):
    defsys.warnf(format,args)
def errorf(format:str, *args):
    defsys.errorf(format,args)
def fatalf(format:str, *args):
    defsys.fatalf(format,args)
def panicf(format:str, *args):
    defsys.panicf(format,args)