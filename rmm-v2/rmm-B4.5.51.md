## B4.5.51 RMI\_REC\_ENTER command

Enter a REC.

## See also:

- [A2.4 Realm Execution Context](rmm-A2.4.md)
- Chapter A4 Realm exception model
- [D1.3.1 Realm entry and exit flow](rmm-D1.3.md#d131-realm-entry-and-exit-flow)

## B4.5.51.1 Interface

## B4.5.51.1.1 Input values

| Name    | Register   | Bits   | Type    | Description           |
|---------|------------|--------|---------|-----------------------|
| fid     | X0         | 63:0   | UInt64  | FID, value 0xC400015C |
| rec_ptr | X1         | 63:0   | Address | PA of the target REC  |
| run_ptr | X2         | 63:0   | Address | PA of RecRun object   |

## B4.5.51.1.2 Context

The RMI\_REC\_ENTER command operates on the following context.

| Name   | Type      | Value                | Before   | Description   |
|--------|-----------|----------------------|----------|---------------|
| run    | RmiRecRun | RmiRecRunAt(run_ptr) | false    | RecRun object |
| rec    | RmmRec    | RecAt(rec_ptr)       | false    | REC           |
| realm  | RmmRealm  | RealmAt(rec.owner)   | false    | Realm         |

## B4.5.51.1.3 Output values


| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.51.2 Failure conditions

* run_align
  * pre: !AddrIsRmiGranuleAligned(run_ptr)
  * post: result.status == RMI_ERROR_INPUT
* run_pas
  * pre: !NonSecureAccessPermitted(run_ptr)
  * post: result.status == RMI_ERROR_INPUT
* rec_align
  * pre: !AddrIsRmiGranuleAligned(rec_ptr)
  * post: result.status == RMI_ERROR_INPUT
* rec_bound
  * pre: !PaIsTracked(rec_ptr)
  * post: result.status == RMI_ERROR_INPUT
* rec_gran_state
  * pre: GranuleAt(rec_ptr).state != GRAN_REC
  * post: result.status == RMI_ERROR_INPUT
* realm_state
  * pre: realm.state != REALM_ACTIVE
  * post: result.status == RMI_ERROR_REALM
* rec_state
  * pre: rec.state == REC_RUNNING
  * post: result.status == RMI_ERROR_REC
* rec_runnable
  * pre: rec.flags.runnable == NOT_RUNNABLE
  * post: result.status == RMI_ERROR_REC
* rec_mmio
  * pre: (run.enter.flags.emul_mmio == RMI_EMULATED_MMIO && rec.emulatable_abort != EMULATABLE_ABORT)
  * post: result.status == RMI_ERROR_REC
* rec_gicv3
  * pre: !Gicv3ConfigIsValid()
  * post: result.status == RMI_ERROR_REC
* rec_pending
  * pre: rec.pending == REC_PENDING_PSCI
  * post: result.status == RMI_ERROR_REC

## B4.5.51.2.1 Failure condition ordering

[rec\_align, rec\_bound, rec\_gran\_state, run\_pas, run\_align] &lt; [rec\_state, rec\_runnable, rec\_mmio, realm\_state, rec\_pending]

<!-- image -->


## B4.5.51.3 Success conditions

* rec_exit
  * post: run.exit contains Realm exit syndrome information.
* rec_emul_abt
  * post: rec.emulatable_abort is updated.

## B4.5.51.4 Footprint

| ID       | Value                |
|----------|----------------------|
| emul_abt | rec.emulatable_abort |