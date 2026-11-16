# Checks for hotspots.py. Run: python test_hotspots.py   (or: python -m pytest)
import contextlib, io, runpy

with contextlib.redirect_stdout(io.StringIO()):
    globals().update({k: v for k, v in runpy.run_path("hotspots.py").items() if not k.startswith("__")})


def test_build():
    assert "reports" in globals(), "Make a variable called reports."
    assert isinstance(reports, list), "reports should be a list, written with square brackets [ ]."
    assert len(reports) == 6, f"reports should hold 6 locations; it holds {len(reports)}."
    assert all(isinstance(r, tuple) and len(r) == 2 for r in reports), "Each report should be a pair like (28.7041, 77.1025)."
    
    assert "cell" in globals() and callable(cell), "Make a function called cell with def."
    assert cell(28.7041, 77.1025) == (28.7, 77.1), f"cell(28.7041, 77.1025) should give (28.7, 77.1); it gave {cell(28.7041, 77.1025)}."
    assert cell(28.7049, 77.1031) == cell(28.7041, 77.1025), "Two reports 90 metres apart should land in the same square."
    
    assert "hotspots" in globals(), "Make a variable called hotspots holding the Counter."
    assert hotspots.most_common(1)[0] == ((28.7, 77.1), 4), f"The worst square should be (28.7, 77.1) with 4 reports; got {hotspots.most_common(1)[0]}."
    assert sum(hotspots.values()) == 6, "Every one of the 6 reports should be counted once."


if __name__ == "__main__":
    test_build()
    print("all checks passed")
