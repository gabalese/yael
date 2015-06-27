# coding=utf-8

"""
Parsing option constants.
"""


class ParsingOptions:
    """
    Enumeration of parsing option constants
    to be used when creating a
    :class:`yael.publication.Publication`
    by parsing a file or directory.
    """

    # Resolve asset references. Default.
    ASSET_REFS = "asset_refs"

    # Do not resolve asset references.
    NO_ASSET_REFS = "no_asset_refs"

    # Parse META-INF/encryption.xml, if present. Default.
    ENCRYPTION = "encryption"

    # Do not parse META-INF/encryption.xml.
    NO_ENCRYPTION = "no_encryption"

    # Parse the Media Overlay Documents (SMIL files), if present. Default.
    MEDIA_OVERLAY = "media_overlay"

    # Do not parse the Media Overlay Documents (SMIL files).
    NO_MEDIA_OVERLAY = "no_media_overlay"

    # Parse META-INF/metadata.xml and Multiple Renditions, if present. Default.
    MULTIPLE_RENDITIONS = "multiple_renditions"

    # Do not parse META-INF/metadata.xml and Multiple Renditions.
    NO_MULTIPLE_RENDITIONS = "no_multiple_renditions"

    # Parse the NCX TOC, if present. Default.
    NCX = "ncx"

    # Do not parse the NCX TOC.
    NO_NCX = "no_ncx"

    # Parse the Navigation Document, if present. Default.
    NAV = "nav"

    # Do not parse the Navigation Document.
    NO_NAV = "no_nav"


