# booking

[![Build Status](https://travis-ci.com/DUBooking/booking.svg?branch=main)](https://travis-ci.com/DUBooking/booking)
[![codecov](https://codecov.io/gh/DUBooking/booking/branch/main/graph/badge.svg)](https://codecov.io/gh/DUBooking/booking)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Development

### Requirements

1. Python3.8+
1. PostgreSQL 12+

### Development environment (debian based systems)

#### Install packages

```bash
$ sudo apt install postgresql libpq-dev
$ python3 -m venv .venv
$ . ./.venv/bin/activate
$ pip install wheel
$ pip install -r requirements.txt
```

#### Setup PostgreSQL

```
$ sudo -u postgres psql
postgres=# create database booking;
postgres=# create user booking with encrypted password 'booking';
postgres=# grant all privileges on database booking to booking;
postgres=# alter user booking CREATEDB;
```

##### Test connection example

```bash
$ psql -h 127.0.0.1 -U booking booking
Password for user booking:
psql (12.6 (Ubuntu 12.6-0ubuntu0.20.04.1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
Type "help" for help.

booking=>
```

#### Run migrations

```shell
$ cd booking
$ ./manage.py migrate
```

#### Run dev server

```shell
$ cd booking
$ ./manage.py runserver
```
