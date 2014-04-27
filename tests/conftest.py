import pytest
import slash
import logbook.compat
from slash.loader import Loader

@pytest.fixture
def setup_logging(request):
    logbook.compat.LoggingHandler().push_application()

@pytest.fixture
def slash_session():
    return slash.Session()

@pytest.fixture
def test_loader():
    return Loader()


@pytest.fixture
def active_slash_session(request):
    returned = slash.Session()
    returned.__enter__()

    @request.addfinalizer
    def finalize():
        returned.__exit__(None, None, None)

    return returned
