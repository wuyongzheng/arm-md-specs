## B4.5.11 RMI\_DPT\_L0\_DESTROY command

Destroy a Level 0 DPT.

The RMI\_DPT\_L0\_DESTROY command may initiate a Stateful RMI Operation.

The RMI\_DPT\_L0\_DESTROY command may initiate a memory-transferring RMI Operation.

See also:

- A9.7.5 Device Permission Table

## B4.5.11.1 Interface

## B4.5.11.1.1 Input values

| Name   | Register   | Bits   | Type   | Description           |
|--------|------------|--------|--------|-----------------------|
| fid    | X0         | 63:0   | UInt64 | FID, value 0xC40001DE |

## B4.5.11.1.2 Context

The RMI\_DPT\_L0\_DESTROY command operates on the following context.

| Name   | Type     | Value   | Before   | Description   |
|--------|----------|---------|----------|---------------|
| l0dpt  | RmmDptL0 | DptL0() | false    | Level 0 DPT   |

## B4.5.11.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |


## B4.5.11.2 Failure conditions

* feat
  * pre: Rmm().static.feat_ats != FEATURE_TRUE
  * post: result.status == RMI_ERROR_NOT_SUPPORTED
* l0dpt_state
  * pre: l0dpt.state == DPT_L0_INVALID
  * post: result.status == RMI_ERROR_INPUT

## B4.5.11.2.1 Failure condition ordering

The RMI\_DPT\_L0\_DESTROY command does not have any failure condition orderings.

## B4.5.11.3 Success conditions

* result
  * post: result.status == RMI_SUCCESS
* state
  * post: l0dpt.state == DPT_L0_INVALID

## B4.5.11.4 Footprint

| ID          | Value                                          |
|-------------|------------------------------------------------|
| l0dpt_state | l0dpt.state                                    |
| gran_state  | State of Granules in range [base, base + size) |

<!-- image -->