## B4.5.10 RMI\_DPT\_L0\_CREATE command

Create a Level 0 DPT.

The RMI\_DPT\_L0\_CREATE command may initiate a Stateful RMI Operation.

The RMI\_DPT\_L0\_CREATE command may initiate a memory-transferring RMI Operation.

See also:

- A9.7.5 Device Permission Table

## B4.5.10.1 Interface

## B4.5.10.1.1 Input values

| Name   | Register   | Bits   | Type   | Description           |
|--------|------------|--------|--------|-----------------------|
| fid    | X0         | 63:0   | UInt64 | FID, value 0xC40001DD |

## B4.5.10.1.2 Context

The RMI\_DPT\_L0\_CREATE command operates on the following context.

| Name   | Type      | Value   | Before   | Description     |
|--------|-----------|---------|----------|-----------------|
| rmm    | RmmGlobal | Rmm()   | false    | RMMglobal state |
| l0dpt  | RmmDptL0  | DptL0() | false    | Level 0 DPT     |

## B4.5.10.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |


## B4.5.10.2 Failure conditions

* feat
  * pre: Rmm().static.feat_ats != FEATURE_TRUE
  * post: result.status == RMI_ERROR_NOT_SUPPORTED
* l0dpt_state
  * pre: l0dpt.state == DPT_L0_VALID
  * post: result.status == RMI_ERROR_INPUT

## B4.5.10.2.1 Failure condition ordering

The RMI\_DPT\_L0\_CREATE command does not have any failure condition orderings.

## B4.5.10.3 Success conditions

* result
  * post: result.status == RMI_SUCCESS
* state
  * post: l0dpt.state == DPT_L0_VALID

## B4.5.10.4 Footprint

| ID          | Value       |
|-------------|-------------|
| l0dpt_state | l0dpt.state |

<!-- image -->