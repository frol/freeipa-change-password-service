FreeIPA-change-password-service
===============================

This is a minimalistic project aiming to expose only password changing capabilities of FreeIPA to
users.


Start Docker container
----------------------

```bash
$ docker run --publish 5000:5000 --env FREEIPA_API_SERVER_URL=https://freeipa.example.org frolvlad/freeipa-change-password-service
```


Build Docker container
----------------------

```bash
$ docker build --tag freeipa-change-password-service .
$ docker run --publish 5000:5000 --env FREEIPA_API_SERVER_URL=https://freeipa.example.org freeipa-change-password-service
```


Start FreeIPA Change Password service from sources
--------------------------------------------------

```bash
$ FREEIPA_API_SERVER_URL=https://freeipa.example.org FLASK_APP=freeipa_change_password_service.py flask run --host 0.0.0.0
```


Configuration
-------------

Use environment variables to pass configuration options down to the service:

* `FREEIPA_API_SERVER_URL` (required), e.g. `https://freeipa.example.com`.
* `FREEIPA_CHANGE_PASSWORD_URL_PREFIX` (optional), default is empty string.
