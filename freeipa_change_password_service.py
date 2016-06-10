from flask import Flask, request
from freeipa_api_client import IPAPassword
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        error_message = None
        if not request.form.get('username'):
            error_message = "Please, enter username."
        elif not request.form.get('current_password'):
            error_message = "Please, enter current password."
        elif not request.form.get('new_password1'):
            error_message = "Please, enter new password."
        elif request.form.get('new_password1') != request.form.get('new_password2'):
            error_message = "Passwords don't match."
        else:
            ipa_password_api = IPAPassword(requests, 'https://freeipa.sparky.salford-systems.com')
            password_change_status, password_change_response = ipa_password_api.changePassword(
                request.form['username'],
                request.form['current_password'],
                request.form['new_password1']
            )
            if not password_change_status:
                error_message = password_change_response.headers.get('x-ipa-pwchange-policy-error')
                if not error_message:
                    error_message = password_change_response.headers.get('x-ipa-pwchange-result')
                    if not error_message:
                        error_message = "Unexpected error: <pre>%r</pre><br><pre>%r</pre>" % (
                            password_change_response.headers,
                            password_change_response.content,
                        )

        return (
            ('<div>%s</div>' % (error_message if error_message else 'Password is changed successfuly!')) +
            '<a href="/">Back</a>'
        )

    return (
        '<form method="POST">'
            '<label style="display: block">Username: <input type="text" name="username"></label>'
            '<label style="display: block">Current Password: <input type="password" name="current_password"></label>'
            '<label style="display: block">New Password: <input type="password" name="new_password1"></label>'
            '<label style="display: block">New Password (once again): <input type="password" name="new_password2"></label>'
            '<input type="submit" value="Change Password">'
        '</form>'
    )
