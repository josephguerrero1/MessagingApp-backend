from flask import Flask
import sys
import users
import login
import block
import blocklist
import conversation
import conversations
import friend
import friendlist
import notifications

app = Flask(__name__)


class Data:
    def __init__(self):

        # GET
        self.get_users = users.Users.get_users()
        self.get_conversation = conversation.Conversation.get_conversation()
        self.get_conversations = conversations.Conversations.get_conversations()
        self.get_blocklist = blocklist.Blocklist.get_blocklist()
        self.get_friendlist = friendlist.Friendlist.get_friendlist()
        self.get_notifications = notifications.Notifications.get_notifications()

        # POST
        self.user_signup = users.Users.user_signup()
        self.user_login = login.Login.user_login()
        self.new_message = conversation.Conversation.new_message()
        self.new_conversation = conversations.Conversations.new_conversation()
        self.befriend_user = friend.Friend.befriend_user()
        self.block_user = block.Block.block_user()

        # PATCH
        self.update_user = users.Users.update_user()

        # DELETE
        self.delete_user = users.Users.delete_user()
        self.user_logout = login.Login.user_logout()
        self.delete_message = conversation.Conversation.delete_message()
        self.delete_conversation = conversations.Conversations.delete_conversation()
        self.unblock_user = block.Block.unblock_user()
        self.unfriend_user = friend.Friend.unfriend_user()


# GET endpoints

@app.get("/api/users")
def get_users():
    return Data.get_users


@app.get("/api/conversation")
def get_conversation():
    return Data.get_conversation


@app.get("/api/conversations")
def get_conversations():
    return Data.get_conversations


@app.get("/api/blocklist")
def get_blocklist():
    return Data.get_blocklist


@app.get("/api/friendlist")
def get_friendlist():
    return Data.get_friendlist


@app.get("/api/notifications")
def get_notifications():
    return Data.get_notifications

# POST endpoints


@app.post("/api/users")
def user_signup():
    Data.user_signup


@app.post("/api/login")
def user_login():
    return Data.user_login


@app.post("/api/conversation")
def new_message():
    return Data.new_message


@app.post("/api/conversations")
def new_conversation():
    return Data.new_conversation


@app.post("/api/friend")
def befriend_user():
    return Data.befriend_user


@app.post("/api/block")
def block_user():
    return Data.block_user


# PATCH endpoints

@app.patch("/api/users")
def update_user():
    return Data.update_user

# DELETE endpoints


@app.delete("/api/users")
def delete_user():
    return Data.delete_user


@app.delete("/api/login")
def user_logout():
    return Data.user_logout


@app.delete("/api/conversation")
def delete_message():
    return Data.delete_message


@app.delete("/api/conversations")
def delete_conversation():
    return Data.delete_conversation


@app.delete("/api/friend")
def unfriend_user():
    return Data.unfriend_user


@app.delete("/api/block")
def unblock_user():
    return Data.unblock_user


# Production Code
if(len(sys.argv) > 1):
    mode = sys.argv[1]
else:
    print("No mode argument, please pass a mode argument when invoking the file")
    exit()

if(mode == "production"):
    import bjoern
    print("Bjoern is running.")
    bjoern.run(app, "0.0.0.0", 5020)
elif(mode == "testing"):
    from flask_cors import CORS
    CORS(app)
    print("Running in testing mode!")
    app.run(debug=True)
else:
    print("Invalid mode, please select either 'production' or 'testing'")
    exit()
