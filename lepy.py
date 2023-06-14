
from core.core import IModule, IService


def run(service:IService, *mod:IModule):
    err = service.init(service)
    if err:
        pass
    pass
    