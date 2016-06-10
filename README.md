FreeIPA-change-password-service
===============================

This is a minimalistic project aiming to expose only password changing capabilities of FreeIPA to
users.


Start Docker container
----------------------

```bash
$ docker run --publish 5000:5000 frolvlad/freeipa-change-password-service
```


Build Docker container
----------------------

```bash
$ docker build --tag freeipa-change-password-service .
$ docker run --publish 5000:5000 freeipa-change-password-service
```


Start FreeIPA Change Password service from sources
--------------------------------------------------

```bash
$ FLASK_APP=freeipa_change_password_service.py flask run --host 0.0.0.0
```
