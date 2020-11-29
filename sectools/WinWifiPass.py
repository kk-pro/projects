import subprocess, re

command = "nestsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
networks_list = re.findall(r"(?:Profile\s*:\s(.*)", networks)

result = ""
for netwok_neme in networks_list:
    commnad = "nestsh wlan show profile" + networks + "key=clear"
    current_result = subprocess.check_output(command, shell=True)
    result = result + current_result
