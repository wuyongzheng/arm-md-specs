## B4.5.49 RMI\_REC\_CREATE command

Creates a REC.

The RMI\_REC\_CREATE command may initiate a Stateful RMI Operation.

The RMI\_REC\_CREATE command may initiate a memory-transferring RMI Operation.

## See also:

- A2.4 Realm Execution Context
- A2.4.3 REC index and MPIDR value
- B4.3.4 Object creation and destruction
- B4.5.50 RMI\_REC\_DESTROY command
- D1.2.4 REC creation flow

## B4.5.49.1 Interface

## B4.5.49.1.1 Input values

| Name       | Register   | Bits   | Type    | Description                       |
|------------|------------|--------|---------|-----------------------------------|
| fid        | X0         | 63:0   | UInt64  | FID, value 0xC400015A             |
| rd         | X1         | 63:0   | Address | PA of the RD for the target Realm |
| rec_ptr    | X2         | 63:0   | Address | PA of the target REC              |
| params_ptr | X3         | 63:0   | Address | PA of REC parameters              |

## B4.5.49.1.2 Context

The RMI\_REC\_CREATE command operates on the following context.

| Name      | Type         | Value                      | Before   | Description     |
|-----------|--------------|----------------------------|----------|-----------------|
| rmm       | RmmGlobal    | Rmm()                      | false    | RMMglobal state |
| realm_pre | RmmRealm     | RealmAt(rd)                | true     | Realm           |
| realm     | RmmRealm     | RealmAt(rd)                | false    | Realm           |
| params    | RmiRecParams | RmiRecParamsAt(params_ptr) | false    | REC parameters  |
| rec       | RmmRec       | RecAt(rec_ptr)             | false    | REC             |

DRAFT

## B4.5.49.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.49.2 Failure conditions

## ID

## Condition

```
DRAFT params_align pre: !AddrIsRmiGranuleAligned(params_ptr) post: result.status == RMI_ERROR_INPUT params_pas pre: !NonSecureAccessPermitted(params_ptr) post: result.status == RMI_ERROR_INPUT rec_align pre: !AddrIsRmiGranuleAligned(rec_ptr) post: result.status == RMI_ERROR_INPUT rec_bound pre: !PaIsDelegableConventionalFine(rec_ptr) post: result.status == RMI_ERROR_INPUT rec_state pre: GranuleAt(rec_ptr).state != GRAN_DELEGATED post: result.status == RMI_ERROR_INPUT rd_align pre: !AddrIsRmiGranuleAligned(rd) post: result.status == RMI_ERROR_INPUT rd_bound pre: !PaIsTracked(rd) post: result.status == RMI_ERROR_INPUT rd_state pre: GranuleAt(rd).state != GRAN_RD post: result.status == RMI_ERROR_INPUT realm_state pre: realm_pre.state != REALM_NEW post: result.status == RMI_ERROR_REALM num_recs pre: realm_pre.num_recs == (2 ^ rmm.static.max_recs_order) -1 post: result.status == RMI_ERROR_REALM mpidr_index pre: RecIndex(params.mpidr) != realm_pre.rec_index post: result.status == RMI_ERROR_INPUT B4.5.49.2.1 Failure condition ordering [rd_bound, rd_state] < [realm_state, num_recs]
```

<!-- image -->

## B4.5.49.3 Success conditions

| ID             | Condition                                        |
|----------------|--------------------------------------------------|
| rec_index      | post: realm.rec_index == realm_pre.rec_index + 1 |
| rec_gran_state | post: GranuleAt(rec_ptr).state == GRAN_REC       |
| rec_owner      | post: rec.owner == rd                            |
| rec_attest     | post: rec.attest_state == NO_ATTEST_IN_PROGRESS  |
| rec_mpidr      | post: MpidrEqual(rec.mpidr, params.mpidr)        |
| rec_state      | post: rec.state == REC_READY                     |

## ID

## Condition

```
DRAFT runnable pre: params.flags.runnable == RMI_RUNNABLE post: rec.flags.runnable == RUNNABLE not_runnable pre: params.flags.runnable == RMI_NOT_RUNNABLE post: rec.flags.runnable == NOT_RUNNABLE rec_gprs post: (rec.gprs[[0]] == params.gprs[[0]] && rec.gprs[[1]] == params.gprs[[1]] && rec.gprs[[2]] == params.gprs[[2]] && rec.gprs[[3]] == params.gprs[[3]] && rec.gprs[[4]] == params.gprs[[4]] && rec.gprs[[5]] == params.gprs[[5]] && rec.gprs[[6]] == params.gprs[[6]] && rec.gprs[[7]] == params.gprs[[7]] && rec.gprs[[8]] == Zeros{64}() && rec.gprs[[9]] == Zeros{64}() && rec.gprs[[10]] == Zeros{64}() && rec.gprs[[11]] == Zeros{64}() && rec.gprs[[12]] == Zeros{64}() && rec.gprs[[13]] == Zeros{64}() && rec.gprs[[14]] == Zeros{64}() && rec.gprs[[15]] == Zeros{64}() && rec.gprs[[16]] == Zeros{64}() && rec.gprs[[17]] == Zeros{64}() && rec.gprs[[18]] == Zeros{64}() && rec.gprs[[19]] == Zeros{64}() && rec.gprs[[20]] == Zeros{64}() && rec.gprs[[21]] == Zeros{64}() && rec.gprs[[22]] == Zeros{64}() && rec.gprs[[23]] == Zeros{64}() && rec.gprs[[24]] == Zeros{64}() && rec.gprs[[25]] == Zeros{64}() && rec.gprs[[26]] == Zeros{64}() && rec.gprs[[27]] == Zeros{64}() && rec.gprs[[28]] == Zeros{64}() && rec.gprs[[29]] == Zeros{64}() && rec.gprs[[30]] == Zeros{64}() && rec.gprs[[31]] == Zeros{64}()) rec_pc post: rec.pc == params.pc rim pre: params.flags.runnable == RMI_RUNNABLE post: realm.rim == RimExtendRec(realm_pre, ripas_addr post: rec.ripas_addr == Zeros{ADDRESS_WIDTH}() ripas_top post: rec.ripas_top == Zeros{ADDRESS_WIDTH}() pending post: rec.pending == REC_PENDING_NONE num_recs post: realm.num_recs == realm_pre.num_recs + 1 gic_owner post: rec.gic_owner == 0
```

## B4.5.49.4 RMI\_REC\_CREATE extension of RIM

On successful execution of RMI\_REC\_CREATE, if the new REC is runnable then the new RIM value of the target Realm is calculated by the RMM as follows:

1. Allocate a zero-filled RmiRecParams data structure to hold the measured REC parameters.

```
params)
```

2. Copy the following attributes from the Host-provided RmiRecParams data structure into the measured REC parameters data structure:
- gprs
- pc
- flags
3. Using the RHA of the target Realm, compute the hash of the measured REC parameters data structure.
4. Allocate an RmmMeasurementDescriptorRec data structure.
5. Populate the measurement descriptor:
- Set the desc\_type field to the descriptor type.
- Set the len field to the descriptor length.
- Set the rim field to the current RIM value of the target Realm.
- Set the content field to the hash of the measured REC parameters.
6. Using the RHA of the target Realm, compute the hash of the measurement descriptor. Set the RIM of the target Realm to this value, zero filling upper bytes if the RHA output is smaller than the size of the RIM.

## See also:

- A7.1.1 Realm Initial Measurement
- B3.112 RimExtendRec function
- B4.6.69 RmiRecParams type
- C2.28 RmmMeasurementDescriptorRec type

## B4.5.49.5 Footprint

| ID        | Value                |
|-----------|----------------------|
| rec_index | realm.rec_index      |
| rec_state | GranuleAt(rec).state |
| rim       | realm.rim            |
| num_recs  | realm.num_recs       |

DRAFT