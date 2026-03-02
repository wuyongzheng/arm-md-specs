## B4.5.44 RMI\_PSMMU\_ST\_L2\_DESTROY command

Destroy a PSMMU Level 2 Stream Table.

The RMI\_PSMMU\_ST\_L2\_DESTROY command may initiate a Stateful RMI Operation.

The RMI\_PSMMU\_ST\_L2\_DESTROY command may initiate a memory-transferring RMI Operation.

See also:

- A9.7.4 PSMMU Stream Tables

## B4.5.44.1 Interface

## B4.5.44.1.1 Input values

| Name      | Register   | Bits   | Type    | Description                                                  |
|-----------|------------|--------|---------|--------------------------------------------------------------|
| fid       | X0         | 63:0   | UInt64  | FID, value 0xC40001DC                                        |
| psmmu_ptr | X1         | 63:0   | Address | PA of PSMMU                                                  |
| sid       | X2         | 63:0   | Bits64  | Base of StreamID range described by the Level 2 Stream Table |

## B4.5.44.1.2 Context

The RMI\_PSMMU\_ST\_L2\_DESTROY command operates on the following context.

| Name   | Type Value                                    | Before   | Description                       |
|--------|-----------------------------------------------|----------|-----------------------------------|
| rmm    | RmmGlobal Rmm()                               | false    | RMMglobal state                   |
| psmmu  | RmmPsmmu PsmmuAt(psmmu_ptr)                   | false    | PSMMU                             |
| walk   | RmmPsmmuStWalkResult PsmmuStWalk( psmmu, sid) | false    | Result of PSMMU Stream Table walk |


## B4.5.44.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.44.2 Failure conditions

| ID          | Condition                                                                                |
|-------------|------------------------------------------------------------------------------------------|
| feat        | pre: Rmm().static.feat_da != FEATURE_TRUE post: result.status == RMI_ERROR_NOT_SUPPORTED |
| psmmu_valid | pre: !PsmmuAddrIsValid(psmmu_ptr) post: result.status == RMI_ERROR_INPUT                 |
| sid_bound   | pre: UInt(sid) >= 2^psmmu.sid_size post: result.status == RMI_ERROR_INPUT                |

```
ID Condition L2ST.
```

```
sid_align pre: sid identifies the first entry in an post: result.status == RMI_ERROR_INPUT st_entry pre: walk.ste.state == PSMMU_ST_ENTRY_INVALID post: result.status == RMI_ERROR_INPUT l2st_live pre: PsmmuL2StIsLive(psmmu, sid) post: result.status == RMI_ERROR_INPUT
```

## B4.5.44.2.1 Failure condition ordering

The RMI\_PSMMU\_ST\_L2\_DESTROY command does not have any failure condition orderings.

## B4.5.44.3 Success conditions

| ID        | Condition                                      |
|-----------|------------------------------------------------|
| result    | post: result.status == RMI_SUCCESS             |
| state     | post: walk.ste.state == PSMMU_ST_ENTRY_INVALID |
| B4.5.44.4 | Footprint                                      |
| ID        | Value                                          |
| ste_state | walk.ste.state                                 |

