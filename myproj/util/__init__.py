"""Assortment of utilities.
"""

from datetime import datetime
from hashlib import sha256, md5

import random
import re
import string
import unicodedata


epoch = datetime.utcfromtimestamp(0)


def unix_time(dt=None):
    """Returns the UNIX time representation for a given date or current UTC."""
    dt = dt or datetime.utcnow()
    return int((dt - epoch).total_seconds())


def unix_time_millis(dt=None):
    """Returns the UNIX time representation for a given date or current UTC."""
    dt = dt or datetime.utcnow()
    return int((dt - epoch).total_seconds() * 1000)


def from_iso_to_unix(iso_dt):
    """Converts from ISO format (e.g., "1984-06-02T19:05:00.000Z") to UNIX.
    """
    if isinstance(iso_dt, int):
        return iso_dt       # Already UNIX.
    try:
        dt = datetime.strptime(iso_dt, '%Y-%m-%dT%H:%M:%S.%fZ')
    except ValueError:
        dt = datetime.strptime(iso_dt, '%Y-%m-%dT%H:%M:%SZ')
    return unix_time(dt)


def from_unix_to_iso(dt=None):
    """Returns the ISO representation for a given date or current UTC."""
    dt = int(dt) if dt is not None else unix_time()
    return datetime.utcfromtimestamp(dt).strftime('%Y-%m-%dT%H:%M:%SZ')


def datetime_from_unix_time(unix_dt):
    """Returns a datetime object."""
    return datetime.utcfromtimestamp(unix_dt)


def datetime_from_iso(iso_dt):
    """Returns a datetime object."""
    return datetime.strptime(iso_dt, '%Y-%m-%dT%H:%M:%SZ')


def password_hash(password, salt):
    if salt:
        return sha256(password + salt).hexdigest()
    else:
        return md5(password).hexdigest()[::-1]


def random_string(size):
    return ''.join(random.SystemRandom().choice(
        string.ascii_letters + string.digits) for _ in range(size))


def remove_accents(input_str):
    """Replaces accented chars by their ascii equivalents."""
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


def make_url_friendly(input_str):
    """Returns a URL-friedly version of input_str.

    Removes non-word chars, replaces accented ones and makes it lowercase.
    """
    if input_str is None:
        return None
    return re.sub(r'[\W\\/_]+', '-', remove_accents(input_str)).lower()
