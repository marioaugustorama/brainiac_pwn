# coding=utf-8
import glob
import os.path
import os.path
from os import system as sy





def wordlist():
    import wget
    urlsMetas = [
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/adobe_top100_pass.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/av-update-urls.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/av_hips_executables.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/burnett_top_1024.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/burnett_top_500.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/cms400net_default_userpass.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/common_roots.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/dangerzone_a.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/dangerzone_b.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/db2_default_pass.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/db2_default_user.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/db2_default_userpass.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/default_pass_for_services_unhash.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/default_userpass_for_services_unhash.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/default_users_for_services_unhash.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/dlink_telnet_backdoor_userpass.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/hci_oracle_passwords.csv',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/http_default_pass.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/http_default_userpass.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/http_default_users.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/http_owa_common.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/idrac_default_pass.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/idrac_default_user.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/ipmi_passwords.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/ipmi_users.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/joomla.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/keyboard-patterns.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/malicious_urls.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/mirai_pass.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/mirai_user.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/mirai_user_pass.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/multi_vendor_cctv_dvr_pass.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/multi_vendor_cctv_dvr_users.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/namelist.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/oracle_default_hashes.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/oracle_default_passwords.csv',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/oracle_default_userpass.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/password.lst',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/piata_ssh_userpass.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/postgres_default_pass.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/postgres_default_user.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/postgres_default_userpass.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/root_userpass.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/routers_userpass.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/rpc_names.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/rservices_from_users.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/sap_common.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/sap_default.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/sap_icm_paths.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/scada_default_userpass.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/sensitive_files.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/sensitive_files_win.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/sid.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/snmp_default_pass.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/tftp.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/tomcat_mgr_default_pass.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/tomcat_mgr_default_users.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/tomcat_mgr_default_userpass.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/unix_passwords.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/unix_users.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/vnc_passwords.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/vxworks_collide_20.txt',
        'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/vxworks_common_20.txt',
        ]
    nomes_metasploit = [
        'adobe_top100_pass.txt',
        'av-update-urls.txt',
        'av_hips_executables.txt',
        'burnett_top_1024.txt',
        'burnett_top_500.txt',
        'cms400net_default_userpass.txt',
        'common_roots.txt',
        'dangerzone_a.txt',
        'dangerzone_b.txt',
        'db2_default_pass.txt',
        'db2_default_user.txt',
        'db2_default_userpass.txt',
        'default_pass_for_services_unhash.txt',
        'default_userpass_for_services_unhash.txt',
        'default_users_for_services_unhash.txt',
        'dlink_telnet_backdoor_userpass.txt',
        'hci_oracle_passwords.csv',
        'http_default_pass.txt',
        'http_default_userpass.txt',
        'http_default_users.txt',
        'http_owa_common.txt',
        'idrac_default_pass.txt',
        'idrac_default_user.txt',
        'ipmi_passwords.txt',
        'ipmi_users.txt',
        'joomla.txt',
        'keyboard-patterns.txt',
        'malicious_urls.txt',
        'mirai_pass.txt',
        'mirai_user.txt',
        'mirai_user_pass.txt',
        'multi_vendor_cctv_dvr_pass.txt',
        'multi_vendor_cctv_dvr_users.txt',
        'namelist.txt',
        'oracle_default_hashes.txt',
        'oracle_default_passwords.csv',
        'oracle_default_userpass.txt',
        'password.lst',
        'piata_ssh_userpass.txt',
        'postgres_default_pass.txt',
        'postgres_default_user.txt',
        'postgres_default_userpass.txt',
        'root_userpass.txt',
        'routers_userpass.txt',
        'rpc_names.txt',
        'rservices_from_users.txt',
        'sap_common.txt',
        'sap_default.txt',
        'sap_icm_paths.txt',
        'scada_default_userpass.txt',
        'sensitive_files.txt',
        'sensitive_files_win.txt',
        'sid.txt',
        'snmp_default_pass.txt',
        'tftp.txt',
        'tomcat_mgr_default_pass.txt',
        'tomcat_mgr_default_users.txt',
        'tomcat_mgr_default_userpass.txt',
        'unix_passwords.txt',
        'unix_users.txt',
        'vnc_passwords.txt',
        'vxworks_collide_20.txt',
        'vxworks_common_20.txt',
    ]
    print("instalando wordlist[+]")
    for a in nomes_metasploit:
        pass
    for i in urlsMetas:
        wget.download(i,out="brainiac_suport_file/wordlist/metasploit")
        cont = glob.glob("brainiac_suport_file/wordlist/metasploit/*.*")
    print("")
    print("numero de wordlist [%s]"%len(cont))

def install_web():

    print("[+]iniciando a instalacao =>[web]<=")
    if os.path.exists("brainiac_suport_file") == False:
        os.makedirs("brainiac_suport_file")
    else:
        print("[pass]=[arquivos[ok]]")
    if os.path.exists("brainiac_suport_file/wordlist") ==False:
        print("add=> brainiac_suport_file/wordlist[+]")
        os.makedirs("brainiac_suport_file/wordlist")
    else:
        print("[pass]=[brainiac_suport_file/wordlist[ok]]")
    if os.path.exists("brainiac_suport_file/wordlist/metasploit") == False:
        print("add=> brainiac_suport_file/wordlist/metasploit[+]")
        os.makedirs("brainiac_suport_file/wordlist/metasploit")
    else:
        print("[pass]=[brainiac_suport_file/wordlist/metasploit[ok]]")
    if os.path.exists("brainiac_suport_file/wordlist/sec_wordlist") == False:
        print("add brainiac_suport_file/wordlist/sec_wordlist[+]")
        os.makedirs("brainiac_suport_file/wordlist/sec_wordlist")
    else:
        print("[pass]=[brainiac_suport_file/wordlist/sec_word_list[ok]]")


    print("=> inicinado verificacao de diretorios para  o donwloads dos arquivos....[+]")

    if os.path.isdir("brainiac_suport_file") == True:
        print("check 1-de-4[ok]")
    else:
        print("erro[criacao de diretorios]")
        exit()

    if os.path.isdir("brainiac_suport_file") == True:
        print("check 2-de-5[ok]")
    else:
        print("erro[criacao de diretorios]")
        exit()
    if os.path.isdir("brainiac_suport_file/wordlist") == True:
        print("check 3-de-5[ok]")
    else:
        print("erro[criacao de diretorios]")
        exit()
    if os.path.isdir("brainiac_suport_file/wordlist/metasploit") == True:
        print("check 4-de-5[ok]")
    else:
        print("erro[criacao de diretorios]")
        exit()
    if os.path.isdir("brainiac_suport_file/wordlist/sec_wordlist") == True:
        print("check 5-de-5[ok]")
    else:
        print("erro[criacao de diretorios]")
        exit()
def main():
    install_web()
    wordlist()
main()








