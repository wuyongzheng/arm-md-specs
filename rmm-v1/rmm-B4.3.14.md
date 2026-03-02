## B4.3.14 RMI\_REC\_ENTER command

Enter a REC.

See also:

- A2.3 Realm Execution Context
- Chapter A4 Realm exception model
- D1.3.1 Realm entry and exit flow

## B4.3.14.1 Interface

## B4.3.14.1.1 Input values

| Name    | Register   | Bits   | Type    | Description           |
|---------|------------|--------|---------|-----------------------|
| fid     | X0         | 63:0   | UInt64  | FID, value 0xC400015C |
| rec     | X1         | 63:0   | Address | PA of the target REC  |
| run_ptr | X2         | 63:0   | Address | PA of RecRun object   |

The number of GICv3 List Register values which can be provided by the Host in RmiRecEnter, and which are returned in RmiRecExit, is reported by the RMI\_FEATURES command.

## See also:

- A3.1.9 Number of GICv3 List Registers

## B4.3.14.1.2 Context

The RMI\_REC\_ENTER command operates on the following context.

| Name   | Type      | Value           | Before   | Description   |
|--------|-----------|-----------------|----------|---------------|
| run    | RmiRecRun | RecRun(run_ptr) | false    | RecRun object |

## B4.3.14.1.3 Output values

| Name   | Register   | Bits   | Type                 | Description           |
|--------|------------|--------|----------------------|-----------------------|
| result | X0         | 63:0   | RmiCommandReturnCode | Command return status |

## B4.3.14.2 Failure conditions

| ID        | Condition                                                                                |
|-----------|------------------------------------------------------------------------------------------|
| run_align | pre: !AddrIsGranuleAligned(run_ptr) post: ResultEqual(result, RMI_ERROR_INPUT)           |
| run_bound | pre: !PaIsDelegable(run_ptr) post: ResultEqual(result, RMI_ERROR_INPUT)                  |
| run_pas   | pre: !GranuleAccessPermitted(run_ptr, PAS_NS) post: ResultEqual(result, RMI_ERROR_INPUT) |

ID

## Condition

| rec_align      | pre: post:   | !AddrIsGranuleAligned(rec) ResultEqual(result, RMI_ERROR_INPUT)                                                                      |
|----------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------|
| rec_bound      | pre: post:   | !PaIsDelegable(rec) ResultEqual(result, RMI_ERROR_INPUT)                                                                             |
| rec_gran_state | pre: post:   | Granule(rec).state != REC ResultEqual(result, RMI_ERROR_INPUT)                                                                       |
| realm_new      | pre: post:   | Realm(Rec(rec).owner).state == REALM_NEW ResultEqual(result, RMI_ERROR_REALM, 0)                                                     |
| system_off     | pre: post:   | Realm(Rec(rec).owner).state == REALM_SYSTEM_OFF ResultEqual(result, RMI_ERROR_REALM, 1)                                              |
| rec_state      | pre: post:   | Rec(rec).state == REC_RUNNING ResultEqual(result, RMI_ERROR_REC)                                                                     |
| rec_runnable   | pre: post:   | Rec(rec).flags.runnable == NOT_RUNNABLE ResultEqual(result, RMI_ERROR_REC)                                                           |
| rec_mmio       | pre: post:   | (run.enter.flags.emul_mmio == RMI_EMULATED_MMIO && Rec(rec).emulatable_abort != EMULATABLE_ABORT) ResultEqual(result, RMI_ERROR_REC) |
| rec_gicv3      | pre: post:   | !Gicv3ConfigIsValid( run.enter.gicv3_hcr, run.enter.gicv3_lrs) ResultEqual(result, RMI_ERROR_REC)                                    |
| rec_psci       | pre: post:   | Rec(rec).psci_pending == PSCI_REQUEST_PENDING ResultEqual(result, RMI_ERROR_REC)                                                     |

## B4.3.14.2.1 Failure condition ordering

```
[rec_align, rec_bound, rec_gran_state, run_pas, run_bound, run_align] < [rec_state, ↪ → rec_runnable, rec_mmio, realm_new, system_off, rec_gicv3, rec_psci]
```

<!-- image -->

## B4.3.14.3 Success conditions

| ID           | Condition                                          |
|--------------|----------------------------------------------------|
| rec_exit     | run.exit contains Realm exit syndrome information. |
| rec_emul_abt | rec.emulatable_abort is updated.                   |

## B4.3.14.4 Footprint

| ID       | Value                    |
|----------|--------------------------|
| emul_abt | Rec(rd).emulatable_abort |