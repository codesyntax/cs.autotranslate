from zope.interface import Interface, implements, alsoProvides
from zope.app.content.interfaces import IContentType
from p4a.subtyper.interfaces import IPortalTypedFolderishDescriptor

from cs.autotranslate import translateMessageFactory as _

class IAutoTranslatableFolder(Interface):
    """ Marker interface for folders to have auto translating items"""

alsoProvides(IAutoTranslatableFolder, IContentType)

class AutoTranslatableFolder(object):
    implements(IPortalTypedFolderishDescriptor)
    title = _(u'Auto translatable items')
    description = _(u'Mark this folder as autotranslatable item container')
    type_interface = IAutoTranslatableFolder
    for_portal_type = 'Folder'
