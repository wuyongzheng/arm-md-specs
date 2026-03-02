## B6.3.4 PSCI\_CPU\_SUSPEND command

Suspend execution on the calling VPE.

This command causes a REC exit due to PSCI.

See also:

- A4.3.7 REC exit due to PSCI
- B6.3.2 PSCI\_CPU\_OFF command
- B6.3.3 PSCI\_CPU\_ON command

## B6.3.4.1 Interface

## B6.3.4.1.1 Input values

| Name                | Register   | Bits   | Type    | Description                                                                                                             |
|---------------------|------------|--------|---------|-------------------------------------------------------------------------------------------------------------------------|
| fid                 | X0         | 63:0   | UInt64  | FID, value 0xC4000001                                                                                                   |
| power_state         | X1         | 31:0   | UInt32  | Identifier for a specific local state                                                                                   |
| entry_point_address | X2         | 63:0   | Address | Address at which the core must resume execution                                                                         |
| context_id          | X3         | 63:0   | UInt64  | This parameter is only meaningful to the caller (must be present in X0 upon first entry to Non- Secure exception level) |

The following unused bits of PSCI\_CPU\_SUSPEND input values SBZ: X1[63:32].

The RMM treats all target power states as suspend requests, and therefore the entry\_point\_address and context\_id arguments are ignored.

## B6.3.4.1.2 Output values

The PSCI\_CPU\_SUSPEND command does not have any output values.

Following execution of PSCI\_CPU\_SUSPEND, control does not return to the caller.

## B6.3.4.2 Failure conditions

The PSCI\_CPU\_SUSPEND command does not have any failure conditions.

## B6.3.4.3 Success conditions

The PSCI\_CPU\_SUSPEND command does not have any success conditions.

Following execution of PSCI\_CPU\_SUSPEND, control does not return to the caller.

## B6.3.4.4 Footprint

The PSCI\_CPU\_SUSPEND command does not have any footprint.