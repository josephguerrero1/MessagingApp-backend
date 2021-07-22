from flask import request, Response
import dbhelpers
import json
import traceback


class Block:

    # Block User

    def block_user():
        loginToken = request.json['loginToken']
        blocked_userId = request.json['blocked_userId']

        user_id = dbhelpers.run_select_statement(
            "SELECT us.user_id FROM user_session us WHERE us.loginToken = ?", [
                loginToken]
        )

        if(user_id == None):
            return Response("Invalid Login Token", mimetype="text/plain", status=400)
        else:
            userId = user_id[0][0]

            blockId = dbhelpers.run_insert_statement(
                "INSERT INTO block (user_id, blocked_user_id) VALUES (?, ?)", [userId, blocked_userId]
            )

            if(blockId == None):
                return Response("Failed to block user", mimetype="text/plain", status=500)
            else:
                return Response(status=204)

    # Unblock User

    def unblock_user():
        loginToken = request.json['loginToken']
        blocked_userId = request.json['blocked_userId']

        user_id = dbhelpers.run_select_statement(
            "SELECT us.user_id FROM user_session us WHERE us.loginToken = ?", [
                loginToken]
        )

        if(user_id == None):
            return Response("Invalid Login Token", mimetype="text/plain", status=400)
        else:
            userId = user_id[0][0]

            rowcount = dbhelpers.run_delete_statement(
                "DELETE from block b WHERE b.user_id = ? AND b.blocked_user_id = ?", [userId, blocked_userId]
            )

            if(rowcount == 1):
                return Response(status=204)
            elif(rowcount == None):
                return Response("Failed to unblock user", mimetype="text/plain", status=500)
