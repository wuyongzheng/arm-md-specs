## B4.5.13 RMI\_DPT\_L1\_DESTROY command

Destroy a Level 1 DPT.

The RMI\_DPT\_L1\_DESTROY command may initiate a Stateful RMI Operation.

The RMI\_DPT\_L1\_DESTROY command may initiate a memory-transferring RMI Operation.

See also:

- A9.7.5 Device Permission Table

## B4.5.13.1 Interface

## B4.5.13.1.1 Input values

| Name   | Register   | Bits   | Type    | Description                                            |
|--------|------------|--------|---------|--------------------------------------------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC40001E0                                  |
| addr   | X1         | 63:0   | Address | Base of physical address region described by the L1DPT |

## B4.5.13.1.2 Context

The RMI\_DPT\_L1\_DESTROY command operates on the following context.

| Name        | Type                          | Value Before   | Description       |
|-------------|-------------------------------|----------------|-------------------|
| rmm         | RmmGlobal Rmm()               | false          | RMMglobal state   |
| l0dpt_entry | RmmDptL0Entry DptL0Walk(addr) | false          | Level 0 DPT entry |

## B4.5.13.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

DRAFT

## B4.5.13.2 Failure conditions

| ID          | Condition                                                                                 |
|-------------|-------------------------------------------------------------------------------------------|
| feat        | pre: Rmm().static.feat_ats != FEATURE_TRUE post: result.status == RMI_ERROR_NOT_SUPPORTED |
| addr_bound  | pre: UInt(addr) >= rmm.static.dptps post: result.status == RMI_ERROR_INPUT                |
| addr_align  | pre: !AddrIsAligned(addr, rmm.static.l0dptsz) post: result.status == RMI_ERROR_INPUT      |
| entry_state | pre: l0dpt_entry.state == DPT_L0_ENTRY_BLOCK post: result.status == RMI_ERROR_INPUT       |

## B4.5.13.2.1 Failure condition ordering

The RMI\_DPT\_L1\_DESTROY command does not have any failure condition orderings.

## B4.5.13.3 Success conditions

| ID     | Condition                                     |
|--------|-----------------------------------------------|
| result | post: result.status == RMI_SUCCESS            |
| state  | post: l0dpt_entry.state == DPT_L0_ENTRY_BLOCK |

## B4.5.13.4 Footprint

| ID                | Value             |
|-------------------|-------------------|
| l0dpt_entry_state | l0dpt_entry.state |

<!-- image -->