import os
import unittest
import json

from yael import Publication

location = lambda *path: os.path.join(os.path.dirname(os.path.realpath(__file__)), *path)

class TestPublication(unittest.TestCase):
    """
    Test with an EPUB2 simple publication
    """

    def setUp(self):
        epubfile = location('assets/lovecraft.epub')
        self.publication = Publication(path=epubfile)

    def test_parse_basic_information(self):
        self.assertEquals("urn:uuid:83136816-fa25-11e2-93d4-001cc0a62c0b", self.publication.unique_identifier)
        self.assertEquals("OPS/images/cover.png", self.publication.internal_path_cover_image)
        self.assertEquals("2.0", self.publication.version)

    def test_structure_is_readable(self):
        reference_json = json.loads(
            open(location('assets/lovecraft.json')).read()
        )

        self.assertEquals(
            reference_json['container'],
            self.publication.json_object().get('container')
        )

    def test_ncx_toc(self):
        self.assertEquals(
            "83136816-fa25-11e2-93d4-001cc0a62c0b",
            self.publication.container.default_rendition.ncx_toc.json_object().get('dtb_uid')
        )

    def test_landmarks(self):
        """
        An EPUB2 document should not have landmarks
        """
        self.assertIsNone(self.publication.container.default_rendition.landmarks)

    def test_dc_subject_metadata(self):
        print(self.publication.metadata)
        self.fail()

    # dc:subject metadata
    #for metadatum in p.container.default_rendition.pac_document.metadata.metadata_by_tag(DC.E_NS_SUBJECT):
    #    print(metadatum)

    # get the value for the media:active-class metadatum
    #metadata = p.container.default_rendition.pac_document.metadata.metadata_by_property(OPFMeta3.V_MEDIA_ACTIVE_CLASS)
    #if len(metadata) > 0:
    #    print(metadata[0].v_text)
   
    # get the values for the media:narrator metadata
    #for metadatum in p.container.default_rendition.pac_document.metadata.metadata_by_property(OPFMeta3.V_MEDIA_NARRATOR):
    #    print(metadatum.v_text)

    # get the values for the media:duration metadata
    #for metadatum in p.container.default_rendition.pac_document.metadata.metadata_by_property(OPFMeta3.V_MEDIA_DURATION):
    #    if metadatum.v_refines == None:
    #        print("Total: %s" % metadatum.v_text)
    #    else:
    #        print("Ref %s: %s" % (metadatum.v_refines, metadatum.v_text))

    # all PNG images
    #for img in p.container.default_rendition.pac_document.manifest.items_by_media_type("image/png"):
    #    print(img)
   
    # all JPEG images
    #for img in p.container.default_rendition.pac_document.manifest.items_by_media_type(MediaType.JPEG):
    #    print(img)

    # all images
    #for img in p.container.default_rendition.pac_document.manifest.image_items:
    #    print(img)

    # all manifest items with scripted property
    #for item in p.container.default_rendition.pac_document.manifest.scripted_items:
    #    print(item)
   
    # all Media Overlay documents
    #for item in p.container.default_rendition.pac_document.manifest.mo_items:
    #    print(item)

    # all files referenced in the manifest, in order
    #for i_p_file in p.container.default_rendition.pac_document.files_referenced_manifest:
    #    print(i_p_file)

    # all files referenced in the spine, in order
    #for i_p_file in p.container.default_rendition.pac_document.files_referenced_spine:
    #    print(i_p_file)

    # all files referenced in the spine, with linear="yes" or omitted, in order
    #for i_p_file in p.container.default_rendition.pac_document.files_referenced_spine_linear:
    #    print(i_p_file)

    # for all MO documents, print the referenced audio files
    #for mo_doc in p.container.default_rendition.mo_documents:
    #    print(mo_doc.internal_path)
    #    for audio_file in mo_doc.referenced_audio_files:
    #        print(" + %s" % audio_file)
    #    print("")

    # for all MO documents, print the referenced text fragment identifiers, in order
    #for mo_doc in p.container.default_rendition.mo_documents:
    #    print(mo_doc.internal_path)
    #    for text_id in mo_doc.referenced_fragment_identifiers:
    #        print(" + %s" % text_id)
    #    print("")

    # for all MO documents, print the referenced text fragment identifiers,
    # grouped by text file
    #for mo_doc in p.container.default_rendition.mo_documents:
    #    grouped = mo_doc.grouped_referenced_fragment_identifiers
    #    for key in grouped:
    #        print(" + %s" % key)
    #        for text_id in grouped[key]:
    #            print("    + %s" % text_id)
    #    print("")

    # test Multiple Renditions
    #if len(p.container.renditions) > 1:
    #    print("Publication Unique  ID: %s" % p.unique_identifier)
    #    print("Publication Release ID: %s" % p.release_identifier)
    #    print("Rendition 1 Unique  ID: %s" % p.container.renditions[0].pac_document.v_unique_identifier)
    #    print("Rendition 2 Unique  ID: %s" % p.container.renditions[1].pac_document.v_unique_identifier)
    #    print("")
    #    print("Rendition Mapping Document\n%s" % p.container.rm_document.json_string(clean=True, pretty=True))

    # extract the cover image and save it to /tmp/extracted_cover.png
    #i_p_cover = p.internal_path_cover_image
    #if (i_p_cover != None) and (i_p_cover in p.assets):
    #    print("Extracting '%s' ..." % i_p_cover)
    #    blob = p.assets[i_p_cover].contents
    #    output_file = open("/tmp/extracted_cover.png", mode="wb")
    #    output_file.write(blob)
    #    output_file.close()
    #    print("Extracted /tmp/extracted_cover.png")
    
    # iterates over the spine, printing the contents
    # of the referenced content documents
    #for itemref in p.container.default_rendition.pac_document.spine.itemrefs:
    #    item = p.container.default_rendition.pac_document.manifest.item_by_id(itemref.v_idref)
    #    if item != None:
    #        print("")
    #        print("%s (linear? %s)" % (itemref.v_idref, not (itemref.v_linear == "no")))
    #        print("")
    #        print(item.contents)
    #        print("")

    # copy all the assets into a single directory /tmp/foo/ ("flatten")
    #if not os.path.exists("/tmp/foo"):
    #    os.mkdir("/tmp/foo")
    #for i_p_asset in p.assets.keys():
    #    destination = os.path.join("/tmp/foo", os.path.basename(i_p_asset))
    #    print("Copying '%s' into '%s'..." % (i_p_asset, destination))
    #    fil = open(destination, "wb")
    #    fil.write(p.assets[i_p_asset].contents)
    #    fil.close()
    #    print("Done")

    # print all the assets obfuscated with the IDPF algorithm
    #if p.encryption != None:
    #    print("Assets obfuscated with the Adobe algorithm")
    #    for i_p_asset in p.encryption.adobe_obfuscated_assets:
    #        print("  + %s" % i_p_asset)
    #    print("")
    #    print("Assets obfuscated with the IDPF algorithm")
    #    for i_p_asset in p.encryption.idpf_obfuscated_assets:
    #        print("  + %s" % i_p_asset)
    #    print("")

    # print the number of items in the manifest
    #print("Manifest length = %d" % len(p.container.default_rendition.pac_document.manifest))

    # print the number of itemrefs in the spine
    #print("Spine length = %d" % len(p.container.default_rendition.pac_document.spine))

    # print the spine index and linear spine index of the following assets
    #i_p_assets = ["OEBPS/Text/cover.xhtml", "OEBPS/Text/p001.xhtml", "OEBPS/z.html", "doesnotexist.xhtml"]
    #for i_p in i_p_assets:
    #    print("Spine index of        '%s' = %d" % (i_p, p.container.default_rendition.pac_document.spine_index_by_internal_path(i_p)))
    #    print("Linear spine index of '%s' = %d" % (i_p, p.container.default_rendition.pac_document.spine_linear_index_by_internal_path(i_p)))
