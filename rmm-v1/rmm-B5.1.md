## B5.1 RSI version


This specification defines version 1.0 of the Realm Services Interface.

See also:

- Chapter B2 Interface versioning
- B5.3.10 RSI\_VERSION command

## B5.2 RSI command return codes


- An RSI command return code indicates whether the command

- succeeded, or

- failed, and the reason for the failure.


If an RSI command succeeds then it returns RSI\_SUCCESS.

Multiple failure conditions in an RSI command may return the same return code.

If an input to an RSI command uses an invalid encoding then the command fails and returns RSI\_ERROR\_INPUT.

Command inputs include registers and in-memory data structures.

Invalid encodings include:

- using a reserved encoding in an enumeration

See also:

- B5.4.1 RsiCommandReturnCode type