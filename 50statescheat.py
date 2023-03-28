from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# set up the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

# navigate to the quiz website
driver.get("https://www.jetpunk.com/quizzes/how-many-states-can-you-name")
time.sleep(2) # Delay so you can start the quiz and it doesn't end the quiz imd.

# find the text box element and enter the state names
text_box = driver.find_element(By.ID, "txt-answer-box")
states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

for state in states:
    text_box.send_keys(state)
    text_box.send_keys(Keys.RETURN)
    time.sleep(1) # Adjust the delay between each awnser sent


