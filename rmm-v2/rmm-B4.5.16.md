## B4.5.16 RMI\_GPT\_L1\_DESTROY command

Destroy a Level 1 GPT.

The RMI\_GPT\_L1\_DESTROY command may initiate a Stateful RMI Operation.

The RMI\_GPT\_L1\_DESTROY command may initiate a memory-transferring RMI Operation.

## See also:

- A2.3.9 Granule Protection Table management
- B4.5.15 RMI\_GPT\_L1\_CREATE command

## B4.5.16.1 Interface

## B4.5.16.1.1 Input values

| Name   | Register   | Bits   | Type    | Description                                            |
|--------|------------|--------|---------|--------------------------------------------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC40001F4                                  |
| addr   | X1         | 63:0   | Address | Base of physical address region described by the L1GPT |

## B4.5.16.1.2 Context

The RMI\_GPT\_L1\_DESTROY command operates on the following context.

| Name        | Type          | Value           | Before   | Description       |
|-------------|---------------|-----------------|----------|-------------------|
| rmm         | RmmGlobal     | Rmm()           | false    | RMMglobal state   |
| l0gpt_entry | RmmGptL0Entry | GptL0Walk(addr) | false    | Level 0 GPT entry |

## B4.5.16.1.3 Output values


| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.16.2 Failure conditions

* addr_bound
  * pre: UInt(addr) >= rmm.static.pasz
  * post: result.status == RMI_ERROR_INPUT
* addr_align
  * pre: !AddrIsAligned(addr, rmm.static.l0gptsz)
  * post: result.status == RMI_ERROR_INPUT
* entry_state
  * pre: l0gpt_entry.state == GPT_L0_ENTRY_BLOCK
  * post: result.status == RMI_ERROR_INPUT
* gpt_l1_homo
  * pre: !GptL1IsHomogeneous(addr)
  * post: result.status == RMI_ERROR_INPUT

## B4.5.16.2.1 Failure condition ordering

The RMI\_GPT\_L1\_DESTROY command does not have any failure condition orderings.

## B4.5.16.3 Success conditions

* result
  * post: result.status == RMI_SUCCESS
* state
  * post: l0gpt_entry.state == GPT_L0_ENTRY_BLOCK

## B4.5.16.4 Footprint

| ID                | Value             |
|-------------------|-------------------|
| l0gpt_entry_state | l0gpt_entry.state |

<!-- image -->