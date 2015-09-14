import sys
import imp


class FakeImportDispatcher(object):

    replaces = {}

    def __init__(self, *args):

        pass

    def find_module(self, name):

        #if name not in FakeImportDispatcher.replaces:
        #    return None

        return self

    @staticmethod
    def add_replace(name, replace):

        FakeImportDispatcher.replaces[name] = replace

    def load_module(self, name):
        print("Load module {name}...".format(name=name))
        #
        if name in FakeImportDispatcher.replaces:
            name = FakeImportDispatcher.replaces.get(name)
        #
        print "now i load {mod}".format(mod=name)
        #
        fh, pathname, description = imp.find_module(name, ['.'])
        p = imp.load_module(name, fh, pathname, description)
        #
        return p


class FakeImporter(object):
    def __init__(self):
        self.__dispatcher = FakeImportDispatcher

        sys.path_hooks.insert(0, self.__dispatcher)
        #sys.meta_path.insert(0, self.__dispatcher)


    def replace(self, name, replace_name):
        self.__dispatcher.add_replace(name, replace_name)

#
def test():

    im = FakeImporter()
    im.replace("import_to_owerride", "override")
    import override
    override.to_owerride()

if __name__ == "__main__":
    test()

