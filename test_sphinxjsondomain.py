import sphinxjsondomain

def test_normalize_object_name():
    """Test object name normalization."""
    previous_object_name = ':json:object:: test'
    result = sphinxjsondomain.normalize_object_name(previous_object_name)
    assert result == ':json:object::-test'
