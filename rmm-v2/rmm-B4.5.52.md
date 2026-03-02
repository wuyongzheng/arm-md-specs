## B4.5.52 RMI\_RMM\_ACTIVATE command

Activate the RMM.

The RMI\_RMM\_ACTIVATE command may initiate a Stateful RMI Operation.

The RMI\_RMM\_ACTIVATE command may initiate a memory-transferring RMI Operation.

See also:

## · A2.1 RMM

## B4.5.52.1 Interface

## B4.5.52.1.1 Input values

| Name   | Register   | Bits   | Type   | Description           |
|--------|------------|--------|--------|-----------------------|
| fid    | X0         | 63:0   | UInt64 | FID, value 0xC4000202 |

## B4.5.52.1.2 Context

The RMI\_RMM\_ACTIVATE command operates on the following context.

| Name   | Type      | Value   | Before   | Description     |
|--------|-----------|---------|----------|-----------------|
| rmm    | RmmGlobal | Rmm()   | false    | RMMglobal state |

## B4.5.52.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

DRAFT

## B4.5.52.2 Failure conditions

| ID    | Condition                                                                        |
|-------|----------------------------------------------------------------------------------|
| state | pre: rmm.dynamic.state != RMM_STATE_INIT post: result.status == RMI_ERROR_GLOBAL |

## B4.5.52.3 Success conditions

| ID     | Condition                                   |
|--------|---------------------------------------------|
| result | post: result.status == RMI_SUCCESS          |
| state  | post: rmm.dynamic.state == RMM_STATE_ACTIVE |

## B4.5.52.4 Footprint

The RMI\_RMM\_ACTIVATE command does not have any footprint.