from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
import time

CONFIGS = {
    'USERNAME': 'YOUR_USERNAME',
    'PASSWORD': 'YOUR_PASSWORD',
    'HASHTAGS': [
        'FIRST_HASHTAG', 'SECOND_HASHTAG'
    ],
    'TOTAL_LIKES_PER_HASHTAG': 300,
    'SYSTEM': 'windows/linux/mac'
}

total_likes = 0

driver = webdriver.Chrome('./chromedriver_{}'.format(CONFIGS['SYSTEM']))

print("Loading Instagram")
driver.get("https://www.instagram.com/")

print("Logging in")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((
    By.NAME, 'username'
)))

usernameInput = driver.find_element(By.NAME, 'username')
usernameInput.send_keys(CONFIGS['USERNAME'])

passwordInput = driver.find_element(By.NAME, 'password')
passwordInput.send_keys(CONFIGS['PASSWORD'])

passwordInput.submit()

# Search
WebDriverWait(driver, 10).until(EC.presence_of_element_located((
    By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input"
)))
print("Logged in!")

print("Navigating through hashtags...")
for current_hashtag in CONFIGS['HASHTAGS']:
    driver.get(
        "https://www.instagram.com/explore/tags/{}/".format(current_hashtag)
    )

    try:
        # Search results
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.TAG_NAME, "h1"
        )))
    except:
        print("Hashtag #{} not loaded, going to next...".format(current_hashtag))
        continue

    print("Loaded #{}".format(current_hashtag))

    print("Checking for results...")
    results = driver.find_elements(By.XPATH, "//a[contains(@href, '/p/')]")

    if not results:
        print("No results for #{}".format(current_hashtag))
        driver.quit()

    print("Opening first post from #{}...".format(current_hashtag))
    results[0].click()

    current_hashtag_likes = 0
    while current_hashtag_likes < CONFIGS['TOTAL_LIKES_PER_HASHTAG']:
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.TAG_NAME, "time"
            )))
        except:
            print("Something is wrong in URL: {}".format(driver.current_url))
            driver.quit()

        time.sleep(1)

        try:
            likeButton = driver.find_element(
                By.XPATH, "/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button"
            )
            likeButton.click()

            print("[#{}/{}/{}] Liked: {}".format(
                current_hashtag,
                current_hashtag_likes,
                CONFIGS['TOTAL_LIKES_PER_HASHTAG'],
                driver.current_url
            ))

            total_likes = total_likes + 1
            current_hashtag_likes = current_hashtag_likes + 1
            time.sleep(10)
        except Exception as e:
            print(e)
            pass

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.CLASS_NAME, 'coreSpriteRightPaginationArrow'
            )))

            nextButton = driver.find_element(
                By.CLASS_NAME, 'coreSpriteRightPaginationArrow'
            )

            nextButton.click()
        except:
            print("Something wrong, going to next hashtag...")
            break

print("Exiting...")
print("=====================")
print("Total posts liked: {}".format(total_likes))
driver.quit()
