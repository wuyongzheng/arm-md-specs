## B4.5.24 RMI\_OP\_MEM\_RECLAIM command

Reclaim memory from a stateful RMI operation.

See also:

- B4.3.2 Stateful RMI operations

## B4.5.24.1 Interface

## B4.5.24.1.1 Input values

| Name       | Register   | Bits   | Type    | Description                           |
|------------|------------|--------|---------|---------------------------------------|
| fid        | X0         | 63:0   | UInt64  | FID, value 0xC4000209                 |
| handle     | X1         | 63:0   | Bits64  | Handle which identifies the operation |
| list_addr  | X2         | 63:0   | Address | PA of RMI Address List                |
| list_count | X3         | 63:0   | UInt64  | Number of entries in RMI Address List |

## B4.5.24.1.2 Output values

| Name          | Register   | Bits   | Type      | Description                                   |
|---------------|------------|--------|-----------|-----------------------------------------------|
| result        | X0         | 63:0   | RmiResult | Command result                                |
| reclaim_count | X1         | 63:0   | UInt64    | Number of entries written to RMI Address List |

## B4.5.24.2 Failure conditions

| ID         | Condition                                                                        |
|------------|----------------------------------------------------------------------------------|
| complete   | pre: !OperationIncomplete(handle) post: result.status == RMI_ERROR_INPUT         |
| list_align | pre: !AddrIsAligned(list_addr, 8) post: result.status == RMI_ERROR_INPUT         |
| list_pas   | pre: !NonSecureAccessPermitted(list_addr) post: result.status == RMI_ERROR_INPUT |


## B4.5.24.2.1 Failure condition ordering

The RMI\_OP\_MEM\_RECLAIM command does not have any failure condition orderings.

## B4.5.24.3 Success conditions

| ID         | Condition                                                                                                         |
|------------|-------------------------------------------------------------------------------------------------------------------|
| gran_state | post: State of Granules described by first list_count entries in RMI Address List is the state prior to donation. |

## B4.5.24.4 Footprint

The RMI\_OP\_MEM\_RECLAIM command does not have any footprint.