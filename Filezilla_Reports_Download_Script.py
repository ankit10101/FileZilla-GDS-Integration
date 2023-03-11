import pysftp

# Enter your sFTP server credentials here
host = 'your_sftp_server_host'
port = 22 # Port number that you want to connect to
username = 'your_user_name'
password = 'your_password'

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

# Establish connection with sFTP server
try:
    conn = pysftp.Connection(
        host=host, port=port, username=username, password=password, cnopts=cnopts)
    print("connection established successfully")
except:
    print('failed to establish connection to targeted server')

# Name of the file to be downloaded
file_name = 'Sales_Report.csv'
# Location on sFTP server / Path for file to be downloaded
sftp_file_path = 'Export/MyReports/Sales/'

# Downloading the csv dataset
with conn.cd(sftp_file_path):
    conn.get(file_name)


