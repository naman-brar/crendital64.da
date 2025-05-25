import itertools
from tqdm import tqdm
import base64
import time
import sys

def generate_wordlist():
    # NOTE = Don't Touch This part Of the Code
    info = open("crendital64.da",'r')
    sample_string = base64.b64decode(info.read())
    sys.stdout.write(sample_string.decode("ascii"))

    print("")
    com_chr = input("[+] Please Enter Here All Word For Combination: >> ")
    print("")
    Min_length = int(input("[+] Please Enter Minimun length of words: >>"))
    print("")
    Max_length = int(input("[+] Please Enter Maximum length of Words: >>"))
    print(" ")
    File_Name = input("[+] Please Enter The File name (To Save All The Words): >>")

    Max_length = int(Max_length) + 1

    leng_char = len(com_chr)
    temp_list = []
    for i in range(Min_length,Max_length):
        ans = leng_char**i
        temp_list.append(ans)
    total_lines = sum(temp_list)
    print(f"[+] Numbers of Total Lines: {total_lines}")
    input("[+] Are you Ready?[Press Enter]")
    print("")
    print("\n\n=============Please Wait=================")
    time_started = time.asctime()
    start = time.time()

    file_open = open(File_Name+".txt",'a')
    for i in tqdm(range(Min_length,Max_length), desc="Genrating..."):
        file_open.flush()
        for j in itertools.product(com_chr,repeat=i):
            file_open.write("".join(j)+'\n')
    file_open.flush()
    file_open.close()
    sys.stdout.write("\rDone Successfully")
    print("")
    print("\n\n===============================Process report===========================")
    print(f"[+] Process Started                      :{time_started}")
    end = time.time()
    print(f"[+] Process completed                    :{time.asctime()}")
    total_time= end - start
    print(f"[+] Total Time Consumed                  :{'{:.2f}'.format(total_time)} second")
    rate = total_lines/total_time
    print(f"[+] Rate of Words Generating Per Seconds :{'{:.2f}'.format(rate)}")
    print(" ")
    print("""
*************************************************************************************
*                              WordList Successfully Genrated                       *
*************************************************************************************  
""")
    print(" ")
    input("[+]Press Enter To Exit")

x = input('[+] Select an Option : ')
if x == '1': # to generate wordlist
    generate_wordlist()  # Option to Generate wordlist you
if x == '2': print('for zip password cracking, please use this command ("python main3.py -f new.zip -w 4digitlist.txt") and ignore the terminal error') # to crack zip password  

print("in my case the script is main3.py but in your case it may be main.py or wo.py, so please check the file name before running the command")

print("if you want to generate wordlist, please use the option 1, and if you want to crack zip password, please use the option 2")

print("the author of this hibrid script is naman_brar ")

print("thank you so much to use this script, if you have any issue please contact me on github https://github.com/naman-brar/")


from optparse import OptionParser
import pyzipper
from progress.bar import Bar

def get_wordlist(wordlist_file):
    with open(wordlist_file, 'r') as f:
        return f.read().split('\n')


def extract(file_name):

    with pyzipper.AESZipFile(file_name, 'r') as f:
        f.extractall(pwd = bytes(p, 'utf-8'))       

if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                        help="compressed file", metavar="FILE")
    parser.add_option("-w", "--wordlist", dest="wordlist", 
                        help="Select the wordlist", metavar="WORDLIST")

    (options, args) = parser.parse_args()
    print(options.wordlist)
    for p in Bar('Processing').iter(get_wordlist(options.wordlist)):
        try:
            extract(options.filename)
            print(f"\n[+] Password found: {p}")
            break
        except RuntimeError as e:
            pass
        