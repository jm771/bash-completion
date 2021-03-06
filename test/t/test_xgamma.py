import pytest


class TestXgamma:

    @pytest.mark.complete("xgamma -")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("xgamma -gam")
    def test_2(self, completion):
        assert completion.list == ["-gamma"]
        assert completion.line.endswith(" ")
