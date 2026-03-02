## B4.5.23 RMI\_OP\_MEM\_DONATE command

Donate memory to a stateful RMI operation.

See also:

- B4.3.2 Stateful RMI operations

## B4.5.23.1 Interface

## B4.5.23.1.1 Input values

| Name       | Register   | Bits   | Type    | Description                           |
|------------|------------|--------|---------|---------------------------------------|
| fid        | X0         | 63:0   | UInt64  | FID, value 0xC4000208                 |
| handle     | X1         | 63:0   | Bits64  | Handle which identifies the operation |
| list_addr  | X2         | 63:0   | Address | PA of RMI Address List                |
| list_count | X3         | 63:0   | UInt64  | Number of entries in RMI Address List |

The contents of the RMI Address List are not modified by execution of RMI\_OP\_MEM\_DONATE.

## B4.5.23.1.2 Output values

| Name          | Register   | Bits   | Type              | Description                                                                                                  |
|---------------|------------|--------|-------------------|--------------------------------------------------------------------------------------------------------------|
| result        | X0         | 63:0   | RmiResult         | Command result                                                                                               |
| donated_count | X1         | 63:0   | UInt64            | Number of Granules consumed from RMI Address List                                                            |
| donate_req    | X2         | 63:0   | RmiOpMemDonateReq | Memory donation requirements RES0 unless result.status == RMI_INCOMPLETE and result.mem == RMI_OP_MEM_DONATE |


## B4.5.23.2 Failure conditions

| ID         | Condition                                                                                                                                        |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| complete   | pre: !OperationIncomplete(handle) post: result.status == RMI_ERROR_INPUT                                                                         |
| list_align | pre: !AddrIsAligned(list_addr, 8) post: result.status == RMI_ERROR_INPUT                                                                         |
| list_pas   | pre: !NonSecureAccessPermitted(list_addr) post: result.status == RMI_ERROR_INPUT                                                                 |
| mem_gt     | pre: Amount of memory described by RMI Address List is greater than amount required by the RMI operation. post: result.status == RMI_ERROR_INPUT |
| mem_contig | pre: Memory described by RMI Address List does not meet contiguity requirement. post: result.status == RMI_ERROR_INPUT                           |


| ID        | Condition                                                                                                                   |
|-----------|-----------------------------------------------------------------------------------------------------------------------------|
| mem_align | pre: Memory described by RMI Address List does not meet alignment requirement. post: result.status == RMI_ERROR_INPUT       |
| mem_state | pre: State of a Granule described by RMI Address List does not match expected state. post: result.status == RMI_ERROR_INPUT |

## B4.5.23.2.1 Failure condition ordering

The RMI\_OP\_MEM\_DONATE command does not have any failure condition orderings.

## B4.5.23.3 Success conditions

| ID         | Condition                                                                                       |
|------------|-------------------------------------------------------------------------------------------------|
| gran_state | post: State of the first donated_count Granules described by RMI Address List is GRAN_INTERNAL. |

## B4.5.23.4 Footprint

The RMI\_OP\_MEM\_DONATE command does not have any footprint.

