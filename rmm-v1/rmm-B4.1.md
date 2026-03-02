## B4.1 RMI version


This specification defines version 1.0 of the Realm Management Interface.

See also:

- Chapter B2 Interface versioning
- B4.3.23 RMI\_VERSION command

## B4.2 RMI command return codes


The return code of an RMI command is a tuple which contains status and index fields.




<!-- image -->


The status field of an RMI command return code indicates whether the command

- succeeded, or
- failed, and the reason for the failure.

If an RMI command succeeds then the status of its return code is RMI\_SUCCESS.

The index field of an RMI command return code can provide additional information about the reason for a command failure. The meaning of the index field depends on the status, and is described by the following table.

| Status          | Description                                                                                                                         | Meaning of index                                            |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| RMI_SUCCESS     | Command completed successfully The value of a command input value caused command to fail An attribute of a Realm does not match the | None: index is zero. None: index is zero.                   |
| RMI_ERROR_INPUT | the                                                                                                                                 |                                                             |
| RMI_ERROR_REALM | expected value                                                                                                                      | Varies between usages. See individual commands for details. |
| RMI_ERROR_REC   | An attribute of a REC does not match the expected value                                                                             | None: index is zero.                                        |
| RMI_ERROR_RTT   | An RTT walk terminated before reaching the target RTT level, or reached an RTTE with an unexpected value                            | RTT level at which the walk terminated.                     |

Multiple failure conditions in an RMI command may return the same error code - that is, the same status and index values.

If an input to an RMI command uses an invalid encoding then the command fails and returns RMI\_ERROR\_INPUT. Command inputs include registers and in-memory data structures. Invalid encodings include:

- using a reserved encoding in an enumeration

## See also:

- B4.4.1 RmiCommandReturnCode type