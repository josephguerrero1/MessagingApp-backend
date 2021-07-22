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
                "SELECT u.username FROM `user` u INNER JOIN block b ON u.id = b.blocked_user_id WHERE b.user_id = ?", [
                    userId]
            )

            empty_blocked_user = []

            for blocked_user in all_blocked_users:
                username = all_blocked_users[0]

                blocked_user = {
                    "username": username
                }

                empty_blocked_user.append(blocked_user)

            if(all_blocked_users == None):
                return Response("Failed to GET all blocked users", mimetype="text/plain", status=500)
            else:
                all_blocked_users_json = json.dumps(
                    all_blocked_users, default=str)
                return Response(all_blocked_users_json, mimetype="application/json", status=200)
