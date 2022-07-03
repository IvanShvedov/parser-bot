"""

"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        "CREATE TABLE channels (id SERIAL, channel VARCHAR(10), PRIMARY KEY (id))",
        "DROP TABLE channels"    
    )
]
