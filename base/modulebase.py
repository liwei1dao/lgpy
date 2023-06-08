

from base.moduleoptions import ModuleOptions
from core.core import IModule, IModuleOptions, IService,error


class ModuleBase(IModule):
    
    def __init__(self) -> None:
            self.comps = []
            
    #此方法可上层重构 返回自定义的参数载体接口对象 用于底层自动序列化参数使用
    def newOptions(self) -> IModuleOptions:
        return ModuleOptions()

    #模块初始化接口 上层实现可以更具需求重构扩展接口 通过此接口模块可以拿到 当前运行的服务对象以及实现的模块对象和模块参数对象
    #此函数底层实现 初始化模块的组件系统 
    def init(self,service:IService, module:IModule, options:IModuleOptions) -> error:
        for i in self.comps:
            comp = self.comps[i]
            err = comp.Init(service, module, comp, options)
            if err:
                return err
        return None

    #暗转组件接口 上层模块实现 徐涛重构此方法 注册模块组件
    def onInstallComp(self):
        pass
