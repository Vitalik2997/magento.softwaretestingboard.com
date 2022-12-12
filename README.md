# magento.softwaretestingboard.com
Diploma project 
test run sequence:
1. pytest -v -m home --reruns 2 --alluredir reports
2. pytest -v -m create --reruns 2 --alluredir reports 
3. pytest -v -m login --alluredir reports
4. pytest -v -m my_acc --reruns 2 --alluredir reports
5. pytest -v -m gear --reruns 2 --alluredir reports
6. pytest -v -m men --reruns 2 --alluredir reports 
7. pytest -v -m sign_out --aluredir reports 
allure serve reports
