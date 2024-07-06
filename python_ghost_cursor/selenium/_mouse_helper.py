from pathlib import Path

from selenium.webdriver.chrome.webdriver import WebDriver


def install_mouse_helper(page: WebDriver) -> None:
    script_path = Path(__file__).parent.joinpath("../js/mouseHelper.js")
    with open(script_path, 'r') as file:
        script_content = file.read()

    # Inject the script into the page
