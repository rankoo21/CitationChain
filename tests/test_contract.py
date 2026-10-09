import json,pytest
from harness import load
@pytest.fixture
def e(): return load('build_beacon.py','BuildBeacon','releases')
def test_quorum_receipt(e):
 _,c,q,b,U=e;src=json.dumps([{'url':'https://a.example/r','version_path':['version'],'digest_path':['digest']},{'url':'https://b.example/r','version_path':['version'],'digest_path':['digest']},{'url':'https://c.example/r','version_path':['version'],'digest_path':['digest']}]);c.register_release('REL-1','Demo',src);b.extend(['{"version":"1.0.0","digest":"abc"}','{"version":"1.0.0","digest":"abc"}','{"version":"0.9.0","digest":"old"}']*2);c.attest_release('rel-1');r=json.loads(c.get_release('0xowner','REL-1'));assert r['state']=='ATTESTED' and r['status']=='QUORUM_MATCH' and r['support']==2
def test_guards(e):
 _,c,q,b,U=e
 with pytest.raises(U): c.register_release('REL-1','Demo','[{"url":"https://a.example","version_path":["v"],"digest_path":["d"]},{"url":"https://a.example/x","version_path":["v"],"digest_path":["d"]},{"url":"https://c.example","version_path":["v"],"digest_path":["d"]}]')
def test_forged_validator_rejected(e):
 _,c,q,b,U=e;src='[{"url":"https://a.example","version_path":["version"],"digest_path":["digest"]},{"url":"https://b.example","version_path":["version"],"digest_path":["digest"]},{"url":"https://c.example","version_path":["version"],"digest_path":["digest"]}]';c.register_release('REL-1','Demo',src);b.extend(['{"version":"1.0","digest":"abc"}']*3+['{"version":"1.0","digest":"abc"}','{"version":"1.0","digest":"abc"}','{"version":"9.0","digest":"evil"}'])
 with pytest.raises(U): c.attest_release('REL-1')
