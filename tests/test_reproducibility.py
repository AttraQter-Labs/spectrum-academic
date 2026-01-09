from metrics.fairness import demographic_parity

def test_reproducible():
    o = [1,0,1,1]
    g = ["a","a","b","b"]
    assert demographic_parity(o,g) == demographic_parity(o,g)
