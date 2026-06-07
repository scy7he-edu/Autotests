import pytest
from playwright.sync_api import Page

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    args = browser_type_launch_args.get("args", [])
    if "--disable-blink-features=AutomationControlled" not in args:
        args.append("--disable-blink-features=AutomationControlled")
    return {
        **browser_type_launch_args,
        "args": args,
        "channel": "chrome",
        "ignore_default_args": ["--enable-automation"]
    }

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }

@pytest.fixture()
def page(context):
    page: Page = context.new_page()
    page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    page.set_viewport_size({'height': 720, 'width': 1280})
    yield page
