from tkinter.tix import Select


INSERT_INTO_CHANNELS = "INSERT INTO channels (channel) VALUES ('{chat_id}')"
DELETE_FROM_CHANNELS = "DELETE FROM channels WHERE channels.channel='{chat_id}'"

INSERT_INTO_SUBS = "INSERT INTO subs (sub) VALUES ('{sub}')"
DELETE_FROM_SUBS = "DELETE FROM subs WHERE subs.sub='{sub}'"
SELECT_ALL_FROM_SUBS = "SELECT * FROM subs"