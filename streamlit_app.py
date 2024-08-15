import streamlit as st
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def crawling():
    @st.cache_resource
    def get_driver():
        return webdriver.Chrome(
            service=Service(
                ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
            ),
            options=options,
        )
    options = Options()
    # options.add_argument("--disable-gpu")
    # options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
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
    try:
        time.sleep(3)
        # Select subsiciaries->campaign
        subsiciaries_dropdown = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "ddlSubsidiary"))
        )
        subsiciaries_dropdown.click()
        # Select Subsidiaries!!! (ex: "SEC")
        option_sec = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//option[@value='SEC']"))
        )
        option_sec.click()
        campaign_dropdown = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "ddlPage"))
        )
        st.write("부서선택")
        campaign_dropdown.click()
        option_enquiry = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//option[text()='{selected_option}']"))
        )
        option_enquiry.click()
        st.write("홈페이지 선택")
        # from
        from_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "txtDateF"))
        )
        from_input.send_keys(tempt_from)
        st.write("from 선택")
        # to
        to_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "txtDateT"))
        )
        to_input.send_keys(tempt_to)
        submit_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "btnSubmit"))
        )
        st.write("to 선택")
        submit_button.click()
        st.write("제출버튼 누름")
        # export_to_excel 버튼 클릭
        export_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "btnExport"))
        )
        export_button.click()
        st.write("Export to Excel 버튼을 클릭했습니다.")
        # 페이지 로딩을 기다림
        WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.ID, "your_result_element_id"))  # 결과가 나타나는 요소의 ID를 사용
        )
        # print(driver.page_source)
    
    except Exception as e:
        print(f"에러발생: {e}")
        time.sleep(5)
    
    # st.code(driver.page_source)
    st.write("일단작동함")
def main():
    crawling()
if __name__ == "__main__":
    main()



