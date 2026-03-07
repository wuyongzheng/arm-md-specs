## B4.5.1 RMI\_ATTEST\_PLAT\_TOKEN\_REFRESH command

Refresh platform attestation token.

See also:

- A9.11.7 Coherent memory device attestation

## B4.5.1.1 Interface

## B4.5.1.1.1 Input values

| Name   | Register   | Bits   | Type   | Description           |
|--------|------------|--------|--------|-----------------------|
| fid    | X0         | 63:0   | UInt64 | FID, value 0xC4000170 |

## B4.5.1.1.2 Context

The RMI\_ATTEST\_PLAT\_TOKEN\_REFRESH command operates on the following context.

| Name   | Type      | Value   | Before   | Description     |
|--------|-----------|---------|----------|-----------------|
| rmm    | RmmGlobal | Rmm()   | false    | RMMglobal state |

## B4.5.1.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.1.2 Failure conditions

* rmm_state
  * pre: rmm.dynamic.state != RMM_STATE_ACTIVE
  * post: result.status == RMI_ERROR_GLOBAL

## B4.5.1.3 Success conditions

* pat_valid
  * post: rmm.dynamic.pat_valid == RMM_TRUE

## B4.5.1.4 Footprint

| ID        | Value                 |
|-----------|-----------------------|
| pat_valid | rmm.dynamic.pat_valid |