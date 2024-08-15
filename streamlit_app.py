import streamlit as st

with st.echo():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.core.os_manager import ChromeType
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    @st.cache_resource
    def get_driver():
        return webdriver.Chrome(
            service=Service(
                ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
            ),
            options=options,
        )

    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")

    driver = get_driver()
    driver.get("https://apps.ucsiuniversity.edu.my/enquiry/resultLogin.aspx")
    time.sleep(5)
    try:
        # Enter ID, PW(!!!!환경변수로?!!!)
        user_id = "dm"
        password = "dm123"
        
        id_input = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "txtUser"))
        )
        id_input.send_keys(user_id)
        pw_input = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "txtPwd"))
        )
        pw_input.send_keys(password)
        login_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.ID, "cmdLogin"))
        )
        login_button.click()
        time.sleep(5)
        st.write("로그인 성공!")
    except Exception as e:
        st.write(f"로그인 실패: {e}")
        time.sleep(5)

    st.code(driver.page_source)
