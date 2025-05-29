import pytest

# skipping ...........................................................................
@pytest.mark.skip
# managing the execution order ...........................................................................
# customized markers  pytest_ordering package
# filename.ini
# [pytest]
# markers=
#     first
#     second
#     third
#     fourth
#     fifth
@pytest.mark.first
@pytest.mark.second
@pytest.mark.third
@pytest.mark.fourth
# default markers
# @pytest.mark.run(order=1)
# @pytest.mark.run(order=2) ...
# dependent test ...........................................................................
@pytest.mark.dependency()    # for the test_openApp
@pytest.mark.dependency(depends=['TestClass::test_openApp'])
# like this nested yvna neg negneesee hamaaraltai
# grouping ...................................................................
# pytest -v -s -m "group name" "file path"
# like sanity, regression,
# need to add these custom marks in recent .ini file
# @pytest.mark.regression
# @pytest.mark.sanity
# mark every finctions like this to group








