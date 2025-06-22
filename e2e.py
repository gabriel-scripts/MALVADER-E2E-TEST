import time
import platform
import os

def config_selenium():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.firefox.service import Service as FirefoxService

    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager

    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        firefox_options = webdriver.FirefoxOptions()
    except Exception as e: 
        print("error: on configurations of selenium:", e)

    system = platform.system()
    print(system)
    try:
        if system == "Windows":
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        elif system == "Linux":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
        else:
            raise Exception("Error: OS not suported")
    except Exception as e:
        print("Error: ", e)
        print("Please install the required drivers for your OS.")
        return None
    
    return driver

def criar_conta(driver):
    driver.get(f"http://localhost:3000/login")

    REGISTRAR_LINK = '/html/body/div/div[2]/form/div[3]/div/a'

    NOME_CLIENT_INPUT = '/html/body/form/div[1]/input[1]'
    SOBRENOME_CLIENT_INPUT = '/html/body/form/div[1]/input[2]'
    CPF_RESTANTE_INPUT = '/html/body/form/div[1]/input[3]'   
    DATA_NASCIMENTO_INPUT = '/html/body/form/div[1]/input[4]'
    TELEFONE_INPUT = '/html/body/form/div[1]/input[5]'
    EMAIL_INPUT = '/html/body/form/div[1]/input[6]'
    SENHA_INPUT = '/html/body/form/div[1]/input[7]'
    CONFIRMAR_SENHA_INPUT = '/html/body/form/div[1]/input[8]'

    CEP_INPUT = '/html/body/form/div[2]/input[1]'
    LOGRADOURO_INPUT = '/html/body/form/div[2]/input[2]'
    NUMERO_RESIDENCIA_INPUT = '/html/body/form/div[2]/input[3]'
    BAIRRO_INPUT = '/html/body/form/div[2]/input[4]'
    CIDADE_INPUT = '/html/body/form/div[2]/input[5]'
    ESTADO_INPUT = '/html/body/form/div[2]/input[6]'
    COMPLEMENTO_INPUT = '/html/body/form/div[2]/input[7]'

    driver.find_element("xpath", REGISTRAR_LINK).click()
    
    driver.find_element("xpath", NOME_CLIENT_INPUT).send_keys("Teste")
    driver.find_element("xpath", SOBRENOME_CLIENT_INPUT).send_keys("E2E")
    driver.find_element("xpath", CPF_RESTANTE_INPUT).send_keys("09168219008")
    driver.find_element("xpath", DATA_NASCIMENTO_INPUT).send_keys("11/10/2003")
    driver.find_element("xpath", TELEFONE_INPUT).send_keys("61999999999")
    driver.find_element("xpath", EMAIL_INPUT).send_keys("teste@gmail.com")
    driver.find_element("xpath", SENHA_INPUT).send_keys("123!@#senhaTESTE")
    driver.find_element("xpath", CONFIRMAR_SENHA_INPUT).send_keys("123!@#senhaTESTE")

    driver.find_element("xpath", CEP_INPUT).send_keys("69304210")
    driver.find_element("xpath", LOGRADOURO_INPUT).send_keys("")
    driver.find_element("xpath", NUMERO_RESIDENCIA_INPUT).send_keys("100")
    driver.find_element("xpath", BAIRRO_INPUT).send_keys("")
    driver.find_element("xpath", CIDADE_INPUT).send_keys("")
    driver.find_element("xpath", ESTADO_INPUT).send_keys("")
    driver.find_element("xpath", COMPLEMENTO_INPUT).send_keys("Casa")

    time.sleep(3)

def login_cliente(driver):
    driver.get(f"http://localhost:3000/login")
    CLIENTE_BUTTON = '/html/body/div/div[2]/form/div[1]/label[2]'
    EMAIL_INPUT = '/html/body/div/div[2]/form/input[1]'
    SENHA_INPUT = '/html/body/div/div[2]/form/input[2]'


    driver.find_element("xpath", CLIENTE_BUTTON).click()

    driver.find_element("xpath", EMAIL_INPUT).send_keys("Teste")
    driver.find_element("xpath", SENHA_INPUT).send_keys("123!@#senhaTESTE")

    time.sleep(3)

def menu_cliente(driver):
    driver.get(f"http://localhost:3000/client")
    
    TRANFERENCIA_BUTTON = '/html/body/div/div/div[4]/button[1]'
    driver.find_element("xpath", TRANFERENCIA_BUTTON).click()

    time.sleep(3)

def login_funcionario(driver):
    pass

def menu_funcionario(driver):
    pass

def TestForm(driver):
    try:    
        criar_conta(driver)
        login_cliente(driver)
        menu_cliente(driver)
    except Exception as e:
        driver.quit()
        print("error on TestForm:", e)
    finally:
        driver.quit()

def e2e():
    driver = config_selenium()
    TestForm(driver)

e2e()