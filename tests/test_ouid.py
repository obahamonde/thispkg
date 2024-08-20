from thispkg import DocumentObject


def test_ouid():
    doc = DocumentObject()
    assert doc.id.startswith("documentobject_")
    assert len(doc.id) > 16
