import dropbox  # Dropbox library (must be installed)
import os  # System library of the system
import sys  # Library to take the input parameters
APP_KEY = 't4mqh41tlbcp6d3'  # change with the one generated in your app
APP_SECRET = 'fzm6jfontu9hdzy'  # change with the one generated in your app
actualpath = os.getcwd()


# Transfer Data
# Class with the functions of handling the chat
class TransferData:
    def __init__(self, dbx, access_token):  # initialization function
        self.access_token = access_token

    def exists(self, user):  # Checks if the user exists in the user file
        var = False  # initialization auxiliary
        token = ""
        with open("input.dat", 'r') as input_file:  # open user file
            for line in input_file:

                u, t = line.split(" ")  # Separates username and token
                t = t.strip()
                if u == user:  # If the user exists
                    var = True
                    token = t

        if var == True:
            return token  # If the user exists, return the token
        else:
            return "fail"

    def upload_file(self, dbx, file_from, file_to):  # Upload file

        with open(file_from, 'rb') as f:
            dbx.files_upload(
                f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)

    def download(self, dbx, archive):  # Download the chat file

        dbx.files_download_to_file(
            actualpath + '/chat.txt', '/KasiChat/chat.txt')
        print("\nWelcome to KasiChat !!!")
        f = open('chat.txt', 'r')  # Opening file in reading mode
        message = f.read()  # Show all messages
        print(message)
        f.close()

    def recordmessage(self, dbx, user, message):  # Upload messages to the file
        f = open('chat.txt', 'a')  # Open file
        f.write('\n' + user + ': ' + message)  # Write message to file
        f.close()

    def email(self, dbx):  # Return message with the user's email connected
        try:
            # Show the account attached to the connection
            dbx.users_get_current_account()
            return dbx.users_get_current_account().email
        except dropbox.exceptions.AuthError:
            raise StandardError('error')
            return ""

    def writemessage(self, dbx, user):  # Write message on screen
        message = ''
        print ("\nSend the messages you want, to close type quitchat")
        while (message != 'quitchat'):
            print("message: ")
            message = input()  # line reading

            if message != 'quitchat':

                self.recordmessage(dbx, user, message)
        print('\nAll messages were sent, goodbye !!!')

    def registeruser(self):  # Register new user

        # Create application flow with the key and secret app
        auth_flow = dropbox.DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)
        # Generate a registration url to allow application
        authorize_url = auth_flow.start()
        print("To register a new allowed user, perform the following steps:")
        print ("1. Go to: " + authorize_url)
        print ("2. Click \"Allow\" (you might have to log in first).")
        print ("3. Copy the authorization code.")

        auth_code = input("Enter the authorization code here: ").strip()
        try:
            # The dropbox api generates the token with the auth
            oauth_result = auth_flow.finish(auth_code)
            print("Code entered correctly, the user has the following token\n"
                  "(Copy the token and paste it in input.dat file: ")
            print(oauth_result.access_token)
        except Exception:
            print('Error: The entered code is not correct redo the process')
            sys.exit(1)


def main():
    # Number of parameters minimum 2 and maximum 3 otherwise
    if len(sys.argv) == 1 or len(sys.argv) > 3:
        print("Help KasiChat \nCommand available: \n"
              "To register a new user, use: python chat.py register \n"
              "To see and send messages, use: python chat.py start <user> ")

    elif sys.argv[1] == 'register':
        transferdata = TransferData("", '')
        transferdata.registeruser()  # Call user registration
    elif sys.argv[1] == 'start':
        transferdata = TransferData("", "")
        token = transferdata.exists(sys.argv[2])  # Retrieve file token
        try:

            dbx = dropbox.Dropbox(token)  # Generate dropbox conn with the api
            transferdata = TransferData(dbx, token)  # Transfer class initialization
            print("User associated with the account: ", transferdata.email(dbx))
            file_from = 'chat.txt'  # local file
            file_to = '/KasiChat/chat.txt'  # Destination in the dropbox
            transferdata.download(dbx, file_to)  # Download the chat file
            transferdata.writemessage(
                dbx, sys.argv[2] + " (" + transferdata.email(dbx) + ")")

        # API v2
            transferdata.upload_file(dbx, file_from, file_to)  # Upload the file

        except dropbox.exceptions.BadInputError:

            print('Unregistered user, Please register user by running python chat.py register')
            sys.exit(1)
        except dropbox.exceptions.AuthError:
            print('Unregistered user, Please register user by running python chat.py register')

if __name__ == '__main__':
    main()
