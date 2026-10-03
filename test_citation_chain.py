import json,pytest
from test_harness import load
@pytest.fixture
def e(): return load('citation_chain.py','CitationChain','citations')
def test_verify_receipt(e):
 _,c,q,b,U=e;c.register_citation('PAPER-1','Consensus Systems',2024,'10.1234/abc.def','https://doi.example/10.1234/abc.def','https://publisher.example/paper'); a='DOI metadata title Consensus Systems year 2024 authors A B'; z='Publisher title Consensus Systems DOI 10.1234/abc.def year 2024'; out='{"status":"VERIFIED","summary":"Both records identify the same work.","title":"Consensus Systems","authors":["A B"],"year":2024,"doi":"10.1234/abc.def","mismatches":[]}'
 b.extend([a,z,a,z]);q.extend([out,out]);c.verify_citation('paper-1');r=json.loads(c.get_citation('0xowner','PAPER-1'));assert r['state']=='VERIFIED' and r['status']=='VERIFIED' and len(r['digests'])==2
def test_guards(e):
 _,c,q,b,U=e
 with pytest.raises(U): c.register_citation('BAD','Title',2024,'not-doi','https://doi.example/x','https://publisher.example/x')
 with pytest.raises(U): c.register_citation('BAD','Title',2024,'10.1234/abc','https://same.example/doi','https://same.example/pub')
 c.register_citation('PAPER-1','Title',2024,'10.1234/abc','https://doi.example/x','https://publisher.example/x')
 with pytest.raises(U): c.register_citation(' paper-1 ','Other',2023,'10.1234/xyz','https://a.example/x','https://b.example/x')
def test_forged_validator_rejected(e):
 _,c,q,b,U=e;c.register_citation('PAPER-2','Consensus Systems',2024,'10.1234/abc.def','https://doi.example/x','https://publisher.example/x');b.extend(['DOI title Consensus Systems year 2024','Publisher title Different Systems year 2024','DOI title Consensus Systems year 2024','Publisher title Different Systems year 2024']);q.extend(['{"status":"VERIFIED","summary":"forged","title":"Consensus Systems","authors":["A B"],"year":2024,"doi":"10.1234/abc.def","mismatches":[]}','{"status":"MISMATCH","summary":"titles differ","title":"Different Systems","authors":["A B"],"year":2024,"doi":"10.1234/abc.def","mismatches":["title"]}'])
 with pytest.raises(U): c.verify_citation('PAPER-2')
