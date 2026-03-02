## B4.5.22 RMI\_OP\_CONTINUE command

Continue a stateful RMI operation.

See also:

- B4.3.2 Stateful RMI operations

## B4.5.22.1 Interface

## B4.5.22.1.1 Input values

| Name   | Register   | Bits   | Type             | Description                           |
|--------|------------|--------|------------------|---------------------------------------|
| fid    | X0         | 63:0   | UInt64           | FID, value 0xC4000203                 |
| handle | X1         | 63:0   | Bits64           | Handle which identifies the operation |
| flags  | X2         | 63:0   | RmiContinueFlags | Flags                                 |

## B4.5.22.1.2 Output values

| Name       | Register   | Bits   | Type              | Description                                                                   |
|------------|------------|--------|-------------------|-------------------------------------------------------------------------------|
| result     | X0         | 63:0   | RmiResult         | Command result                                                                |
| donate_req | X2         | 63:0   | RmiOpMemDonateReq | Memory donation requirements. RES0 unless result.mem == RMI_OP_MEM_REQ_DONATE |

## B4.5.22.2 Failure conditions

| ID       | Condition                                                                                                                |
|----------|--------------------------------------------------------------------------------------------------------------------------|
| complete | pre: !OperationIncomplete(handle) post: result.status == RMI_ERROR_INPUT                                                 |
| fail     | pre: The resumed command fails. post: Output values are populated according to the specification of the resumed command. |


## B4.5.22.2.1 Failure condition ordering

The RMI\_OP\_CONTINUE command does not have any failure condition orderings.

## B4.5.22.3 Success conditions

| ID                | Condition   | Condition                                                                                                             |
|-------------------|-------------|-----------------------------------------------------------------------------------------------------------------------|
| output_complete   | pre: post:  | !OperationIncomplete(handle) All output values are populated according to the specification of the completed command. |
| status_incomplete | pre: post:  | OperationIncomplete(handle) result.status == RMI_INCOMPLETE                                                           |

## ID

## Condition

donate\_req

```
pre: (OperationIncomplete(handle) && result.data.incomplete.mem == RMI_OP_MEM_REQ_DONATE) post: donate_req describes the memory donation requirements of the operation.
```

## B4.5.22.4 Footprint

The RMI\_OP\_CONTINUE command does not have any footprint.

<!-- image -->