from flask import request, Response
import dbhelpers
import json
import traceback


class Blocklist:

    # Get All Blocked Users

    def get_blocklist():
        loginToken = request.json['loginToken']

        user_id = dbhelpers.run_select_statement(
            "SELECT us.user_id FROM user_session us WHERE us.loginToken = ?", [
                loginToken]
        )

        if(user_id == None):
            return Response("Invalid Login Token", mimetype="text/plain", status=400)
        else:
            userId = user_id[0][0]

        all_blocked_users = dbhelpers.run_select_statement(
            "SELECT b."
        )
