## B6.3.3 PSCI\_CPU\_ON command

Power up a core.

This command causes a REC exit due to PSCI. In response, the Host should provide the target REC (identified by target\_cpu ) by calling RMI\_PSCI\_COMPLETE.

## See also:

- A2.3.2 REC attributes
- A4.3.7 REC exit due to PSCI
- B4.3.7 RMI\_PSCI\_COMPLETE command
- B6.3.2 PSCI\_CPU\_OFF command
- B6.3.4 PSCI\_CPU\_SUSPEND command
- D1.4.1 PSCI\_CPU\_ON flow

## B6.3.3.1 Interface

## B6.3.3.1.1 Input values

| Name                | Register   | Bits   | Type    | Description                                                                                                                             |
|---------------------|------------|--------|---------|-----------------------------------------------------------------------------------------------------------------------------------------|
| fid                 | X0         | 63:0   | UInt64  | FID, value 0xC4000003                                                                                                                   |
| target_cpu          | X1         | 63:0   | Bits64  | This parameter contains a copy of the affinity fields of the MPIDR register                                                             |
| entry_point_address | X2         | 63:0   | Address | Address at which the core must resume execution                                                                                         |
| context_id          | X3         | 31:0   | UInt32  | This parameter is only meaningful to the caller (must be present in X0 of the target PE upon first entry to Non-Secure exception level) |

The following unused bits of PSCI\_CPU\_ON input values SBZ: X3[63:32].

## B6.3.3.1.2 Context

The PSCI\_CPU\_ON command operates on the following context.

| Name       | Type     | Value                    | Before   | Description   |
|------------|----------|--------------------------|----------|---------------|
| realm      | RmmRealm | CurrentRealm()           | false    | Current Realm |
| target_rec | RmmRec   | RecFromMpidr(target_cpu) | false    | Target REC    |

## B6.3.3.1.3 Output values

| Name   | Register   | Bits   | Type           | Description         |
|--------|------------|--------|----------------|---------------------|
| result | X0         | 63:0   | PsciReturnCode | Command return code |

## B6.3.3.2 Failure conditions

| ID       | Condition                                                                              |
|----------|----------------------------------------------------------------------------------------|
| entry    | pre: !AddrIsProtected(entry_point_address, realm) post: result == PSCI_INVALID_ADDRESS |
| mpidr    | pre: !MpidrIsUsed(target_cpu) post: result == PSCI_INVALID_PARAMETERS                  |
| runnable | pre: target_rec.flags.runnable == RUNNABLE post: result == PSCI_ALREADY_ON             |

## B6.3.3.2.1 Failure condition ordering

The PSCI\_CPU\_ON command does not have any failure condition orderings.

## B6.3.3.3 Success conditions

| ID       | Condition                                            |
|----------|------------------------------------------------------|
| entry    | target_rec.pc == ToBits64(UInt(entry_point_address)) |
| runnable | target_rec.flags.runnable == RUNNABLE                |

## B6.3.3.4 Footprint

| ID       | Value                     |
|----------|---------------------------|
| runnable | target_rec.flags.runnable |