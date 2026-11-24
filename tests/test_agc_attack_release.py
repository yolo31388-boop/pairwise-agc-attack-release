import pytest
import media.agc_attack_release as mod

CASES = [
    ("time_in_seconds", (1,)),
    ("accumulate_across_blocks", (1,)),
    ("target_headroom", (1,)),
    ("gain_per_channel", (1,)),
    ("offline_prewarm", (1,)),
    ("rebuild_on_rate", (1,)),
    ("process", (1,)),
    ("set_target", (1,)),
    ("render", (1,)),
    ("export", (1,)),
    ("validate_agc", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
