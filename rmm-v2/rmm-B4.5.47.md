## B4.5.47 RMI\_REALM\_DESTROY command

Destroys a Realm.

The RMI\_REALM\_DESTROY command may initiate a Stateful RMI Operation.

The RMI\_REALM\_DESTROY command may initiate a memory-transferring RMI Operation.

## See also:

- A2.2 Realm
- B4.3.4 Object creation and destruction
- B4.5.46 RMI\_REALM\_CREATE command
- D1.2.5 Realm destruction flow

## B4.5.47.1 Interface

## B4.5.47.1.1 Input values

| Name   | Register   | Bits   | Type    | Description           |
|--------|------------|--------|---------|-----------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC4000159 |
| rd     | X1         | 63:0   | Address | PA of the RD          |

## B4.5.47.1.2 Context

The RMI\_REALM\_DESTROY command operates on the following context.

<!-- image -->


| Name      | Type      | Value       | Before   | Description     |
|-----------|-----------|-------------|----------|-----------------|
| rmm_pre   | RmmGlobal | Rmm()       | true     | RMMglobal state |
| rmm       | RmmGlobal | Rmm()       | false    | RMMglobal state |
| realm_pre | RmmRealm  | RealmAt(rd) | true     | Realm           |
| realm     | RmmRealm  | RealmAt(rd) | false    | Realm           |

## B4.5.47.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.47.2 Failure conditions

* rd_align
  * pre: !AddrIsRmiGranuleAligned(rd)
  * post: result.status == RMI_ERROR_INPUT
* rd_tracking
  * pre: !PaIsTrackedFine(rd)
  * post: result.status == RMI_ERROR_INPUT
* rd_state
  * pre: GranuleAt(rd).state != GRAN_RD
  * post: result.status == RMI_ERROR_INPUT
* realm_state
  * pre: realm.state != REALM_ZOMBIE
  * post: result.status == RMI_ERROR_REALM
* realm_live
  * pre: RealmIsLive(rd)
  * post: result.status == RMI_ERROR_REALM
* cmem_mec_refresh
  * pre: !CmemMecUpdateComplete(realm)
  * post: result.status == RMI_ERROR_REALM

## B4.5.47.2.1 Failure condition ordering

```
[rd_tracking, rd_state] < [realm_state, realm_live]
```

<!-- image -->

## B4.5.47.3 Success conditions

* result
  * post: result.status == RMI_SUCCESS
* num_realms
  * post: rmm.dynamic.num_realms == rmm_pre.dynamic.num_realms -1
* rtt_state
  * post: RttsStateEqual( realm_pre.rtt_base[[0]], realm_pre.rtt_num_start, GRAN_DELEGATED)
* rd_state
  * post: GranuleAt(rd).state == GRAN_DELEGATED

## B4.5.47.4 Footprint

| ID        | Value                                                               |
|-----------|---------------------------------------------------------------------|
| rd_state  | GranuleAt(rd).state                                                 |
| rtt_state | RttsGranuleState( realm_pre.rtt_base[[0]], realm_pre.rtt_num_start) |