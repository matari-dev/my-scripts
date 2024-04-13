import pyautogui
import pyperclip
import time

def get_tab_urls():
    # Make sure your browser is positioned in the upper left corner
    # Activate browser window
    pyautogui.click(x=100, y=100)  # Click somewhere to ensure focus on browser window
    
    links = []

    thereIsMore = True

    while thereIsMore:
        # Open a new tab
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(0.1)  # Wait for the next tab
        
        # Navigate to the address bar
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(0.1)  # Wait for the address bar to focus
        
        # Copy the URL
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.1)  # Wait for the URL to be copied
        
        # Get the clipboard content
        links.append(pyperclip.paste())
        
        # Close the tab
        thereIsMore = "stop" != pyperclip.paste()
    return links


def save_urls_to_file(urls, filename='urls.txt'):
    with open(filename, 'w') as f:
        for url in urls:
            f.write(url + '\n')


if __name__ == "__main__":
    urls = get_tab_urls()
    save_urls_to_file(urls)
    print("URLs saved to urls.txt")
