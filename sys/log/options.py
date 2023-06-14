from typing import Tuple
from typing import Callable
from core.core import error

Option = Callable[["Options"], None]

class Options:
    fileName:str     #日志文件名包含

#日志文件名包含
def set_filename(v:str):
    def option(o:Options):
        o.filename = v
    return option

def newOptions(config :dict, *opts:Option)  -> Tuple[Options,error] :
	options = Options()
	options.fileName = "log"
	return options,None

def newOptionsByOption( *opts:Option) -> Tuple[Options,error] :
    options = Options()
    options.fileName = "log"
    return options,None 
