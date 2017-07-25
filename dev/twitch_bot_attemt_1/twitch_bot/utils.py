def fixPath(path):
    import os
    return os.path.expanduser(os.path.abspath(path))

def importFileByPath(path):
    import sys
    import os
    if sys.version_info >= (3,5): # python 3.5 +
        # try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(os.path.basename(path), path)
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        return foo
        # except ImportError:
        #     pass
    elif sys.version_info >= (3,3): # python 3.3, 3.4
        from importlib.machinery import SourceFileLoader
        return SourceFileLoader(os.path.basename(path), path).load_module()
    else: # python 2  
        import imp
        return imp.load_source(os.path.basename(path), path)