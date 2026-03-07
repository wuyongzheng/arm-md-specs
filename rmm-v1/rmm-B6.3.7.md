## B6.3.7 PSCI\_SYSTEM\_RESET command

Shut down the system.

This command causes a REC exit due to PSCI.

See also:

- [A2.3.2 REC attributes](rmm-A2.3.md#a232-rec-attributes)
- [A4.3.7 REC exit due to PSCI](rmm-A4.3.md#a437-rec-exit-due-to-psci)
- [B6.3.6 PSCI\_SYSTEM\_OFF command](rmm-B6.3.6.md)

## B6.3.7.1 Interface

## B6.3.7.1.1 Input values

| Name   | Register   | Bits   | Type   | Description           |
|--------|------------|--------|--------|-----------------------|
| fid    | X0         | 63:0   | UInt64 | FID, value 0x84000009 |

## B6.3.7.1.2 Context

The PSCI\_SYSTEM\_RESET command operates on the following context.

| Name   | Type     | Value          | Before   | Description   |
|--------|----------|----------------|----------|---------------|
| realm  | RmmRealm | CurrentRealm() | false    | Current Realm |

## B6.3.7.1.3 Output values

The PSCI\_SYSTEM\_RESET command does not have any output values.

Following execution of PSCI\_SYSTEM\_RESET, control does not return to the caller.

## B6.3.7.2 Failure conditions

The PSCI\_SYSTEM\_RESET command does not have any failure conditions.

## B6.3.7.3 Success conditions

* state
  * realm.state == REALM_SYSTEM_OFF

## B6.3.7.4 Footprint

The PSCI\_SYSTEM\_RESET command does not have any footprint.