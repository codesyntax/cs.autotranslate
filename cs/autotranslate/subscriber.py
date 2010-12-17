from Acquisition import aq_parent
from Products.LinguaPlone.public import AlreadyTranslated

from cs.autotranslate.translate import IAutoTranslatableFolder

def translate(object, event):
    parent = aq_parent(object)
    if IAutoTranslatableFolder.providedBy(parent):
        translations = parent.getTranslations()
        for lang, translated in translations.items():
            if lang != object.Language():
                try:
                    object.addTranslation(language=lang,
                                          title=object.Title())
                except AlreadyTranslated:
                    from logging import getLogger
                    log = getLogger('cs.autotranslate.subscribers')
                    log.info('Folder already translated')
                
