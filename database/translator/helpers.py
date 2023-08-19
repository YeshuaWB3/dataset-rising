from utils.enums import Source
from tag_normalizer.tag_normalizer import TagNormalizer
from translator.e621_translator import E621PostTranslator, E621TagTranslator
from translator.translator import PostTranslator, TagTranslator


def get_post_translator(source: Source, tag_normalizer: TagNormalizer) -> PostTranslator:
    if source == Source.E621:
        return E621PostTranslator(tag_normalizer)

    raise NotImplementedError(f'Unsupported source (\'{source}\') or type (\'{type}\')')


def get_tag_translator(source: Source) -> TagTranslator:
    if source == Source.E621:
        return E621TagTranslator()

    raise NotImplementedError(f'Unsupported source (\'{source}\') or type (\'{type}\')')
