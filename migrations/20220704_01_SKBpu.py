"""

"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        "CREATE TABLE channels (id SERIAL, channel VARCHAR(15) UNIQUE, PRIMARY KEY (id))",
        "DROP TABLE channels"    
    ),
    step(
        "CREATE TABLE subs (id SERIAL, sub VARCHAR(15) UNIQUE, PRIMARY KEY (id))",
        "DROP TABLE subs"
    )
]
