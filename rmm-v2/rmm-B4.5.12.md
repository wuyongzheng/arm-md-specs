## B4.5.12 RMI\_DPT\_L1\_CREATE command

Create a Level 1 DPT.

The RMI\_DPT\_L1\_CREATE command may initiate a Stateful RMI Operation.

The RMI\_DPT\_L1\_CREATE command may initiate a memory-transferring RMI Operation.

See also:

- [A9.7.5 Device Permission Table](rmm-A9.7.md#a975-device-permission-table)

## B4.5.12.1 Interface

## B4.5.12.1.1 Input values

| Name   | Register   | Bits   | Type    | Description                                            |
|--------|------------|--------|---------|--------------------------------------------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC40001DF                                  |
| addr   | X1         | 63:0   | Address | Base of physical address region described by the L1DPT |

## B4.5.12.1.2 Context

The RMI\_DPT\_L1\_CREATE command operates on the following context.

| Name        | Type          | Value           | Before   | Description       |
|-------------|---------------|-----------------|----------|-------------------|
| rmm         | RmmGlobal     | Rmm()           | false    | RMMglobal state   |
| l0dpt       | RmmDptL0      | DptL0()         | false    | Level 0 DPT       |
| l0dpt_entry | RmmDptL0Entry | DptL0Walk(addr) | false    | Level 0 DPT entry |

## B4.5.12.1.3 Output values


| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.12.2 Failure conditions

* feat
  * pre: Rmm().static.feat_ats != FEATURE_TRUE
  * post: result.status == RMI_ERROR_NOT_SUPPORTED
* l0dpt_state
  * pre: l0dpt.state != DPT_L0_VALID
  * post: result.status == RMI_ERROR_GLOBAL
* addr_bound
  * pre: UInt(addr) >= rmm.static.dptps
  * post: result.status == RMI_ERROR_INPUT
* addr_align
  * pre: !AddrIsAligned(addr, rmm.static.l0dptsz)
  * post: result.status == RMI_ERROR_INPUT
* entry_state
  * pre: l0dpt_entry.state == DPT_L0_ENTRY_TABLE
  * post: result.status == RMI_ERROR_INPUT

## B4.5.12.2.1 Failure condition ordering

The RMI\_DPT\_L1\_CREATE command does not have any failure condition orderings.

## B4.5.12.3 Success conditions

* result
  * post: result.status == RMI_SUCCESS
* state
  * post: l0dpt_entry.state == DPT_L0_ENTRY_TABLE

## B4.5.12.4 Footprint

| ID                | Value             |
|-------------------|-------------------|
| l0dpt_entry_state | l0dpt_entry.state |

