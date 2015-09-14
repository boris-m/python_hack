
from imp_override import FakeImporter


im = FakeImporter()
im.replace("import_to_owerride", "override")
import override
override.to_owerride()