from typing import Tuple
from core.core import error
from .core import ILogger
from .options import Options

def newSys(options:Options) -> Tuple[ILogger,error]:
    sys = Logger(options)
    return sys,None

class Logger:
    def __init__(self,options:Options) -> None:
        pass