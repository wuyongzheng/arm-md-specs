## B4.3.10 RMI\_REALM\_DESTROY command

Destroys a Realm.

See also:

- A2.1 Realm
- B4.3.9 RMI\_REALM\_CREATE command
- D1.2.5 Realm destruction flow

## B4.3.10.1 Interface

## B4.3.10.1.1 Input values

| Name   | Register   | Bits   | Type    | Description           |
|--------|------------|--------|---------|-----------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC4000159 |
| rd     | X1         | 63:0   | Address | PA of the RD          |

## B4.3.10.1.2 Context

The RMI\_REALM\_DESTROY command operates on the following context.

| Name   | Type     | Value     | Before   | Description   |
|--------|----------|-----------|----------|---------------|
| realm  | RmmRealm | Realm(rd) | true     | Realm         |

## B4.3.10.1.3 Output values

| Name   | Register   | Bits   | Type                 | Description           |
|--------|------------|--------|----------------------|-----------------------|
| result | X0         | 63:0   | RmiCommandReturnCode | Command return status |

## B4.3.10.2 Failure conditions

| ID         | Condition                                                                 |
|------------|---------------------------------------------------------------------------|
| rd_align   | pre: !AddrIsGranuleAligned(rd) post: ResultEqual(result, RMI_ERROR_INPUT) |
| rd_bound   | pre: !PaIsDelegable(rd) post: ResultEqual(result, RMI_ERROR_INPUT)        |
| rd_state   | pre: Granule(rd).state != RD post: ResultEqual(result, RMI_ERROR_INPUT)   |
| realm_live | pre: RealmIsLive(rd) post: ResultEqual(result, RMI_ERROR_REALM)           |

## B4.3.10.2.1 Failure condition ordering

[rd\_bound, rd\_state] &lt; [realm\_live]

<!-- image -->

## B4.3.10.3 Success conditions

| ID        | Condition                                                       |
|-----------|-----------------------------------------------------------------|
| rtt_state | RttsStateEqual( realm.rtt_base, realm.rtt_num_start, DELEGATED) |
| rd_state  | Granule(rd).state == DELEGATED                                  |
| vmid      | VmidIsFree(realm.vmid)                                          |

## B4.3.10.4 Footprint

| ID        | Value                                                  |
|-----------|--------------------------------------------------------|
| rd_state  | Granule(rd).state                                      |
| rtt_state | RttsGranuleState( realm.rtt_base, realm.rtt_num_start) |