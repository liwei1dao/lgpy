from abc import ABCMeta, abstractmethod
from typing import Tuple

class error:
    def __init__(self,err:str):
        self.err = err
        
#服务配置数据接口定义
class ServiceSttings :
    def __init__(self):
        self.id = ""           #/服务Id
        self.Type = ""         #服务类型 (相同的服务可以启动多个)
        self.Tag = ""          #服务集群标签 (相同标签的集群服务可以互相发现和发现)
        self.Category = 0      #服务列表 (用于区分集群服务下相似业务功能的服务器 例如:游戏服务器)
        self.Ip = ""           #服务所在Ip				()
        self.Port = 0          #服务rpcx监听端口
        self.Opentime = ""     #开服时间
        self.Comps = {}        #服务组件配置
        self.Sys = {}          #服务系统配置
        self.Modules = {}      #服务模块配置
        
class ICompOptions(metaclass=ABCMeta):
    def __init__(self,):
        pass
    #序列化参数接口
    @abstractmethod
    def loadConfig(self,settings:dict) ->  error: 
        pass

class IModuleOptions(metaclass=ABCMeta):
    def __init__(self,):
        pass
    #序列化参数接口
    @abstractmethod
    def loadConfig(self,settings:dict) ->  error: 
        pass

#基础服务组件的接口设计
class IServiceComp (metaclass=ABCMeta): 
    @abstractmethod
    def getName(self) -> str:
        pass
    @abstractmethod
    def newOptions(self) -> ICompOptions:
        pass
    @abstractmethod
    def init(self,service:'IService', comp:'IServiceComp', options:'ICompOptions') -> error:
        pass
    @abstractmethod
    def start() -> error:
        pass
    @abstractmethod
    def destroy() -> error:
        pass

class IService(metaclass=ABCMeta):
    #获取服务标签
    @abstractmethod
    def getTag(self) -> str:
        pass
    #获取id
    @abstractmethod
    def getId(self) -> str:
        pass
    #获取服务类型
    @abstractmethod
    def getType(self) -> str:
        pass
    #获取服务版本
    @abstractmethod
    def getVersion(self) -> str:
        pass
    #初始化接口
    @abstractmethod
    def init(self, service:'IService') -> error:                        
        pass
    #初始化系统
    def initSys():
        pass
    #组装服务组件               
    def onInstallComp(self,*cops:IServiceComp):
        pass
    #启动服务
    def start(self) -> error:
        pass
    #运行服务                                         
    def run(self,*mods:'IModule'):
        pass
    #关闭服务                                       
    def close(self,closemsg:str):
        pass
    #销毁服务                                      
    def dstroy(self) -> error: 
        pass
    #获取组件                                      
    def getComp(self,compName:str) -> Tuple[IServiceComp,error]:
        pass
    #获取模块   
    def getModule(self,moduleName:str) -> Tuple['IModule',error]:
        pass
 

#模块组件接口设计
class IModuleComp(metaclass=ABCMeta):
    #组件初始化函数
    def init(self,service:IService, module:'IModule', comp:'IModuleComp', options:IModuleOptions) -> error:
        pass
    #组件启动函数
    def start() -> error:
        pass
    #组件销毁函数                                                                        
    def destroy() -> error:
        pass                                                         

 
 
#基础模块的接口设计
class IModule(metaclass=ABCMeta):
    #模块类型
    def getType(self) -> str:
        pass
    #返回模块的参数类型 用于自动序列化模块参数对象
    def newOptions(self) ->  IModuleOptions:  
        pass
    #服务运行时 优先执行完所有模块的Init 函数                                   
    def init(self,service:IService, module:'IModule', options:IModuleOptions) -> error: 
        pass
     #模块启动时在Init中有限执行模块的组件转载函数 初始化组件列表
    def onInstallComp(self):                                                           
        pass
    #服务初始化所有模块后在同一执行各个模块的启动函数
    def start(self) -> error:                                                 
        pass
    #模块需要独立携程运行时可以重构此接口
    def run(self) -> error:                                     
        pass
    #模块销毁接口
    def destroy(self) -> error:                                           
        pass