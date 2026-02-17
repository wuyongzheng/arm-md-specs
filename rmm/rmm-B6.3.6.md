## B6.3.6 PSCI\_SYSTEM\_OFF command

Shut down the system.

This command causes a REC exit due to PSCI.

See also:

- A2.3.2 REC attributes
- A4.3.7 REC exit due to PSCI
- B6.3.7 PSCI\_SYSTEM\_RESET command

## B6.3.6.1 Interface

## B6.3.6.1.1 Input values

| Name   | Register   | Bits   | Type   | Description           |
|--------|------------|--------|--------|-----------------------|
| fid    | X0         | 63:0   | UInt64 | FID, value 0x84000008 |

## B6.3.6.1.2 Context

The PSCI\_SYSTEM\_OFF command operates on the following context.

| Name   | Type     | Value          | Before   | Description   |
|--------|----------|----------------|----------|---------------|
| realm  | RmmRealm | CurrentRealm() | false    | Current Realm |

## B6.3.6.1.3 Output values

The PSCI\_SYSTEM\_OFF command does not have any output values.

Following execution of PSCI\_SYSTEM\_OFF, control does not return to the caller.

## B6.3.6.2 Failure conditions

The PSCI\_SYSTEM\_OFF command does not have any failure conditions.

## B6.3.6.3 Success conditions

| ID    | Condition                       |
|-------|---------------------------------|
| state | realm.state == REALM_SYSTEM_OFF |

Following execution of PSCI\_SYSTEM\_OFF, control does not return to the caller.

## B6.3.6.4 Footprint

The PSCI\_SYSTEM\_OFF command does not have any footprint.