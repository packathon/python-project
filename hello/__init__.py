# __init__ dosyasini genellikle paketimizin public API'ini tanimlamak icin
# kullaniyoruz
from .core import say_hello

__all__ = ['say_hello']
