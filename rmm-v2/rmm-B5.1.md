## B5.1 RSI version

- RQKLGZ This specification defines version 1.1 of the Realm Services Interface.

See also:

- Chapter B2 Interface versioning
- B5.4.22 RSI\_VERSION command

## B5.2 Programming models for RSI operations

- DMQDGF An RSI operation is an operation which is performed by execution of RSI commands.

See also:

- B5.2 Programming models for RSI operations

## B5.2.1 Properties of RSI operations

- DFFJRY A range RSI operation is an operation which modifies the state of a set of objects, which are identified by a contiguous range of addresses.

DRAFT DGFMHC A non-range RSI operation is an operation which modifies a single object or a set of objects, each of which is identified separately. DTVFKK A long-running RSI operation is an operation which may require multiple RSI calls in order to complete the operation. Specifying that an RSI operation is long-running allows the implementation to guarantee that execution of the command will not cause delivery of interrupts to be delayed by more than an IMPLEMENTATION DEFINED upper bound. DTDQKB A non-long-running RSI operation is an operation which does not require multiple RSI calls in order to complete the operation. IDZTZF A range RSI operation is a long-running RSI operation.

- IQSBZN A non-range RSI operation can be either long-running or non-long-running.

## B5.2.2 Progress of long-running RSI operations

The information returned to the caller regarding the amount of progress which has been made differs between long-running RSI operations. This section describes the patterns which are used for reporting this progress.

## B5.2.2.1 Long-running non-range RSI operation

- IBWRWH This pattern has the following characteristics:
- The operation is a non-range operation.
- The caller initiates the operation by calling an RSI 'init' command. The input values to this command fully describe the requested operation.
- The caller continues the operation by calling an RSI 'continue' command. The input values to this command include a handle which the implementation uses to retrieve a description of the operation.
- While the result of the 'continue' command is RSI\_INCOMPLETE, the caller calls the command again.
- While the operation is incomplete, no changes in state are observable by the caller.

The following pseudocode illustrate the programming model for this pattern.

```
int rsi_long_running_non_range( uint64_t in_value_1, uint64_t in_value_2,
```

INDRGM

```
... uint64_t *out_value_1, uint64_t *out_value_2, ...) { int result; result = RSI_OPERATION_INIT( in_value_1, in_value_2, ..., out_value_1, out_value_2, ...); if (result == RSI_SUCCESS) { do { result = RSI_OPERATION_CONTINUE(in_value_1); } while (result == RSI_INCOMPLETE); } return result; }
```

## See also:

- B5.4.2 RSI\_ATTESTATION\_TOKEN\_CONTINUE command
- B5.4.3 RSI\_ATTESTATION\_TOKEN\_INIT command

## B5.2.2.2 Range RSI operation which returns progress address

This pattern has the following characteristics:

- The operation modifies the state of objects which are contiguous within an address space.
- The caller initiates the operation by calling an RSI command, with the target address range identified by input values base and top .
- If the result of this command is RSI\_SUCCESS then an out\_top output value indicates the top of the target address range for which the requested state change has been completed.
- In order to continue an incomplete operation, the call invokes the same command repeatedly, each time adjusting using the previous out\_top as the new base value. This process is repeated until out\_top == top .
- While the operation is incomplete, changes in state are observable by the caller and are explicitly reported in the out\_top value.

DRAFT

The following pseudocode illustrate the programming model for this pattern.

```
int rsi_range_progress( uint64_t base, // input value 1 uint64_t top, // input value 2 uint64_t in_value_3, ... uint64_t *out_top, // output value 1 uint64_t *out_value_2, ...) { int result; do { result = RSI_DO_OPERATION( base, top, in_value_3, ..., out_top, out_value_2, ...); base = *out_top; // If result == RSI_SUCCESS then the requested state change has been // applied to the range [base, *out_top).
```

IGSLYM

IXZZKG

```
} while (result == RSI_SUCCESS && *out_top != top) // If result == RSI_SUCCESS && *out_top == top then the requested state change // has been applied to the entire range [base, top). return result; }
```

When a range RSI operation returns out\_top , the requested state transition has been applied to all objects in the range [base, out\_top) .

When a range RSI operation returns out\_top , the state of objects in the range [out\_top, top) is unchanged by the operation.

See also:

- B5.4.7 RSI\_IPA\_STATE\_SET command
- B5.4.11 RSI\_MEM\_SET\_PERM\_INDEX command
- B5.4.21 RSI\_VDEV\_VALIDATE\_MAPPING command

## B5.3 RSI command return codes

ICYQDJ

An RSI command return code indicates whether the command

- succeeded, or

- failed, and the reason for the failure.

IDQJSP If an RSI command succeeds then it returns RSI\_SUCCESS.

IYMHKC

Multiple failure conditions in an RSI command may return the same return code.

RMLBDM

If an input to an RSI command uses an invalid encoding then the command fails and returns RSI\_ERROR\_INPUT.

Command inputs include registers and in-memory data structures.

Invalid encodings include:

- using a reserved encoding in an enumeration

## See also:

- B5.5.3 RsiCommandReturnCode type

DRAFT