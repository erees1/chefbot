# Script to scrape 8 octopus recipe from mobkitchen
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException as noelement
from selenium.common.exceptions import ElementNotInteractableException, StaleElementReferenceException
import pandas as pd
import time
import re
from tqdm import tqdm


def scrape_recipes_from_homepage(driver, url):
    name_class = "GridItem__headingLink"
    meta_class = "RecipeMeta__category"
    url_class = "GridItem__headingLink"
    pic_class = "GridItem__image"

    driver.get(url)

    time.sleep(5)
    start = time.time()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    popup_close(driver)

    # Scroll to the bottom of the window and get all the reciepes
    while time.time() - start < 2:
        try:
            login = driver.find_element_by_class_name("Hits__loadMore").click()
        except noelement:
            break
        except ElementNotInteractableException:
            popup_close(driver)
        except StaleElementReferenceException:
            pass



    item_tags = driver.find_elements_by_class_name("Grid__item")
    names = []
    metas = []
    urls = []
    pics = []
    for item in item_tags:
        try:
            name = item.find_element_by_class_name(name_class).text

            tags = item.find_elements_by_class_name(meta_class)
            meta = [tag.text for tag in tags]

            url = item.find_element_by_class_name(url_class).get_attribute("href")

            pic = (
                item.find_element_by_class_name(pic_class)
                .find_element_by_xpath(".//img[1]")
                .get_attribute("data-src")
            )

            names.append(name)
            metas.append(meta)
            urls.append(url)
            pics.append(pic)

        except noelement:
            print("element not found")

    items = pd.DataFrame({"Dish": names, "Meta": metas, "URL": urls, "Pic": pics})
    return items


def popup_close(driver):

    try:
        popup_close = driver.find_element_by_class_name("Modal__close")
        popup_close.click()
    except noelement:
        pass


def get_heading_with_text(driver, header, text):
    out = driver.find_element_by_xpath(
        f"//{header}[contains("
        "translate(.,"
        '"ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"),'
        f'"{text}")]'
    ).text
    return out


def scrape_info_from_page(driver, url):

    driver.get(url)
    popup_close(driver)
    driver.implicitly_wait(1)

    # Get main content of web page (ignores header etc...)
    blog_main = driver.find_element_by_class_name("BlogItem-main")
    # Ingredients
    try:
        ingredients = blog_main.find_elements_by_xpath("//ul")
        ingredients = [i.text for i in ingredients]
        ingredients = "\n".join(ingredients)
    except noelement:
        ingredients = "na"
        print(f"Failed to scrape ingredients on {url}")
    # Cooking time
    try:
        time = get_heading_with_text(blog_main, "h2", "time")
    except noelement:
        try:
            time = get_heading_with_text(blog_main, "h3", "time")
        except noelement:
            time = "na"
            print(f"Failed to scrape time on {url}")
    # How many people does the reciepe feed?
    try:
        quantity = get_heading_with_text(blog_main, "h2", "feeds:")
    except noelement:
        try:
            quantity = get_heading_with_text(blog_main, "h3", "feeds:")
        except noelement:
            quantity = "na"
            print(f"Failed to scrape quantitiy on {url}")

    return ingredients, time, quantity


def main():
    # Selenium setup
    driver = webdriver.Chrome(executable_path="./chromedriver")

    # Webpage things
    url = "http://www.mobkitchen.co.uk/recipes"

    # Get all of the recipe titles and urls from homepage
    items = scrape_recipes_from_homepage(driver, url)
    # driver.quit()
    # Then visit each url and get ingredients etc...
    ingredients_ = []
    quantities = []
    times = []
    for rec_url in tqdm(items.URL, desc="Scraping individual pages"):
        ingredients, time, quantity = scrape_info_from_page(driver, rec_url)
        ingredients_.append(ingredients)
        times.append(time)
        quantities.append(quantity)

    items["Ingredients"] = ingredients_
    items["Quantities"] = quantities
    items["times"] = times

    # Quit driver and save to csv
    driver.quit()
    items.to_csv("mob_scrape.csv")


if __name__ == "__main__":
    main()
