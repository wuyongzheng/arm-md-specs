## B6.3.2 PSCI\_CPU\_OFF command

Power down the calling core.

This command causes a REC exit due to PSCI.

See also:

- A2.3.2 REC attributes
- A4.3.7 REC exit due to PSCI
- B6.3.3 PSCI\_CPU\_ON command
- B6.3.4 PSCI\_CPU\_SUSPEND command

## B6.3.2.1 Interface

## B6.3.2.1.1 Input values

| Name   | Register   | Bits   | Type   | Description           |
|--------|------------|--------|--------|-----------------------|
| fid    | X0         | 63:0   | UInt64 | FID, value 0x84000002 |

## B6.3.2.1.2 Context

The PSCI\_CPU\_OFF command operates on the following context.

| Name   | Type   | Value        | Before   | Description   |
|--------|--------|--------------|----------|---------------|
| rec    | RmmRec | CurrentRec() | false    | Current REC   |

## B6.3.2.1.3 Output values

The PSCI\_CPU\_OFF command does not have any output values.

Following execution of PSCI\_CPU\_OFF, control does not return to the caller.

## B6.3.2.2 Failure conditions

The PSCI\_CPU\_OFF command does not have any failure conditions.

## B6.3.2.3 Success conditions

The PSCI\_CPU\_OFF command does not have any success conditions.

Following execution of PSCI\_CPU\_OFF, control does not return to the caller.

## B6.3.2.4 Footprint

The PSCI\_CPU\_OFF command does not have any footprint.