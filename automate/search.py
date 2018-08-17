import requests
with requests.Session() as c:
    url='https://www.students.psgitech.ac.in'
    user='715516104055'
    pas='24JUN98'
    c.get(url)
    login_data=dict
