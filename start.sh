#!/bin/bash
pytest -s simple_py_tests.py
pytest -s basic_fixtures_tests.py
pytest -s extended_fixtures_tests.py
pytest -s extended_fixture2_tests.py
pytest -s generator_fixture_tests.py
pytest -s levels_fixtures_tests.py
cd session\ scope/
pytest -s -v
cd ..
pytest -v -s request_tests.py
pytest -v -s parametrizing_base_tests.py
pytest -s -v multiple_fixtures_tests.py
pytest -s -v marks_for_tests.py
pytest -s -v exceptions_tests.py