## B4.5.15 RMI\_GPT\_L1\_CREATE command

Create a Level 1 GPT.

The RMI\_GPT\_L1\_CREATE command may initiate a Stateful RMI Operation.

The RMI\_GPT\_L1\_CREATE command may initiate a memory-transferring RMI Operation.

## See also:

- A2.3.9 Granule Protection Table management
- B4.5.16 RMI\_GPT\_L1\_DESTROY command

## B4.5.15.1 Interface

## B4.5.15.1.1 Input values

| Name   | Register   | Bits   | Type    | Description                                            |
|--------|------------|--------|---------|--------------------------------------------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC40001F3                                  |
| addr   | X1         | 63:0   | Address | Base of physical address region described by the L1GPT |

## B4.5.15.1.2 Context

The RMI\_GPT\_L1\_CREATE command operates on the following context.

| Name        | Type          | Value           | Before   | Description       |
|-------------|---------------|-----------------|----------|-------------------|
| rmm         | RmmGlobal     | Rmm()           | false    | RMMglobal state   |
| l0gpt_entry | RmmGptL0Entry | GptL0Walk(addr) | false    | Level 0 GPT entry |

## B4.5.15.1.3 Output values


| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.15.2 Failure conditions

* addr_bound
  * pre: UInt(addr) >= rmm.static.pasz
  * post: result.status == RMI_ERROR_INPUT
* addr_align
  * pre: !AddrIsAligned(addr, rmm.static.l0gptsz)
  * post: result.status == RMI_ERROR_INPUT
* entry_state
  * pre: l0gpt_entry.state == GPT_L0_ENTRY_TABLE
  * post: result.status == RMI_ERROR_GPT
* unfold_denied
  * pre: Unfolding of this L0GPT is denied.
  * post: result.status == RMI_ERROR_GLOBAL
* gran
  * pre: The RMM encountered a Granule within the memory donated for the L1GPT whose PAS is not NS or whose category is not DRAM.
  * post: result.status == RMI_ERROR_INPUT

## B4.5.15.2.1 Failure condition ordering

The RMI\_GPT\_L1\_CREATE command does not have any failure condition orderings.

## B4.5.15.3 Success conditions

* result
  * post: result.status == RMI_SUCCESS
* state
  * post: l0gpt_entry.state == GPT_L0_ENTRY_TABLE

## B4.5.15.4 Footprint

| ID                | Value             |
|-------------------|-------------------|
| l0gpt_entry_state | l0gpt_entry.state |
| l0gpt_entry_addr  | l0gpt_entry.addr  |

