from twttr import shorten

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("twitter") == "twttr"
    assert shorten("T.W.I.T.T.E.R.") == "T.W..T.T..R."
    assert shorten("Tw1tt3r") == "Tw1tt3r"
    assert shorten("") == ""
