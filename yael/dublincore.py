# coding=utf-8

"""
Dublin Core constants.
"""

from yael.namespace import Namespace


class DublinCore:
    """
    Enumeration of Dublin Core constants.

    See the source code for the complete list.
    """

    CONTRIBUTOR = "contributor"
    COVERAGE = "coverage"
    CREATOR = "creator"
    DATE = "date"
    DESCRIPTION = "description"
    FORMAT = "format"
    IDENTIFIER = "identifier"
    LANGUAGE = "language"
    PUBLISHER = "publisher"
    RELATION = "relation"
    RIGHTS = "rights"
    SOURCE = "source"
    SUBJECT = "subject"
    TITLE = "title"
    TYPE = "type"
    NS_CONTRIBUTOR = "{{{0}}}{1}".format(Namespace.DC, CONTRIBUTOR)
    NS_COVERAGE = "{{{0}}}{1}".format(Namespace.DC, COVERAGE)
    NS_CREATOR = "{{{0}}}{1}".format(Namespace.DC, CREATOR)
    NS_DATE = "{{{0}}}{1}".format(Namespace.DC, DATE)
    NS_DESCRIPTION = "{{{0}}}{1}".format(Namespace.DC, DESCRIPTION)
    NS_FORMAT = "{{{0}}}{1}".format(Namespace.DC, FORMAT)
    NS_IDENTIFIER = "{{{0}}}{1}".format(Namespace.DC, IDENTIFIER)
    NS_LANGUAGE = "{{{0}}}{1}".format(Namespace.DC, LANGUAGE)
    NS_PUBLISHER = "{{{0}}}{1}".format(Namespace.DC, PUBLISHER)
    NS_RELATION = "{{{0}}}{1}".format(Namespace.DC, RELATION)
    NS_RIGHTS = "{{{0}}}{1}".format(Namespace.DC, RIGHTS)
    NS_SOURCE = "{{{0}}}{1}".format(Namespace.DC, SOURCE)
    NS_SUBJECT = "{{{0}}}{1}".format(Namespace.DC, SUBJECT)
    NS_TITLE = "{{{0}}}{1}".format(Namespace.DC, TITLE)
    NS_TYPE = "{{{0}}}{1}".format(Namespace.DC, TYPE)
    DCTERMS_MODIFIED = "dcterms:modified"

    ALL_ELEMENTS = [
        CONTRIBUTOR,
        COVERAGE,
        CREATOR,
        DATE,
        DESCRIPTION,
        FORMAT,
        IDENTIFIER,
        LANGUAGE,
        PUBLISHER,
        RELATION,
        RIGHTS,
        SOURCE,
        SUBJECT,
        TITLE,
        TYPE,
    ]

    ALL_NS_ELEMENTS = [
        NS_CONTRIBUTOR,
        NS_COVERAGE,
        NS_CREATOR,
        NS_DATE,
        NS_DESCRIPTION,
        NS_FORMAT,
        NS_IDENTIFIER,
        NS_LANGUAGE,
        NS_PUBLISHER,
        NS_RELATION,
        NS_RIGHTS,
        NS_SOURCE,
        NS_SUBJECT,
        NS_TITLE,
        NS_TYPE,
    ]
