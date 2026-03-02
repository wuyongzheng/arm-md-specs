## B4.5.21 RMI\_OP\_CANCEL command

Cancel a stateful RMI operation.

See also:

- B4.3.2 Stateful RMI operations

## B4.5.21.1 Interface

## B4.5.21.1.1 Input values

| Name   | Register   | Bits   | Type   | Description                           |
|--------|------------|--------|--------|---------------------------------------|
| fid    | X0         | 63:0   | UInt64 | FID, value 0xC400020A                 |
| handle | X1         | 63:0   | Bits64 | Handle which identifies the operation |

## B4.5.21.1.2 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.21.2 Failure conditions

| ID         | Condition                                                                                   |
|------------|---------------------------------------------------------------------------------------------|
| complete   | pre: !OperationIncomplete(handle) post: result.status == RMI_ERROR_INPUT                    |
| can_cancel | pre: OperationCanCancel(handle) != RMM_OP_CAN_CANCEL post: result.status == RMI_ERROR_INPUT |

DRAFT !OperationIncomplete(handle)

## B4.5.21.2.1 Failure condition ordering

The RMI\_OP\_CANCEL command does not have any failure condition orderings.

## B4.5.21.3 Success conditions

The RMI\_OP\_CANCEL command does not have any success conditions.

## B4.5.21.4 Footprint

The RMI\_OP\_CANCEL command does not have any footprint.