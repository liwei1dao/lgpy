
from base.moduleoptions import ModuleOptions
from core.core import IModule, IModuleOptions, IService,error


class ServerBase(IService):
    #模块初始化接口 上层实现可以更具需求重构扩展接口 通过此接口模块可以拿到 当前运行的服务对象以及实现的模块对象和模块参数对象
    #此函数底层实现 初始化模块的组件系统 
    def init(self,service:IService, options:IModuleOptions) -> error:
        pass