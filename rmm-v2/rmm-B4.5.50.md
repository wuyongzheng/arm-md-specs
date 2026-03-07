## B4.5.50 RMI\_REC\_DESTROY command

Destroys a REC.

The RMI\_REC\_DESTROY command may initiate a Stateful RMI Operation.

The RMI\_REC\_DESTROY command may initiate a memory-transferring RMI Operation.

## See also:

- A2.4 Realm Execution Context
- B4.3.4 Object creation and destruction
- B4.5.49 RMI\_REC\_CREATE command
- D1.2.5 Realm destruction flow

## B4.5.50.1 Interface

## B4.5.50.1.1 Input values

| Name    | Register   | Bits   | Type    | Description           |
|---------|------------|--------|---------|-----------------------|
| fid     | X0         | 63:0   | UInt64  | FID, value 0xC400015B |
| rec_ptr | X1         | 63:0   | Address | PA of the target REC  |

## B4.5.50.1.2 Context

The RMI\_REC\_DESTROY command operates on the following context.

<!-- image -->


| Name      | Type     | Value                | Before   | Description   |
|-----------|----------|----------------------|----------|---------------|
| rd_pre    | Address  | RecAt(rec_ptr).owner | true     | RD address    |
| realm_pre | RmmRealm | RealmAt(rd_pre)      | true     | Realm         |
| realm     | RmmRealm | RealmAt(rd_pre)      | false    | Realm         |
| rec_pre   | RmmRec   | RecAt(rec_ptr)       | true     | REC           |
| rec       | RmmRec   | RecAt(rec_ptr)       | false    | REC           |

## B4.5.50.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.50.2 Failure conditions

* rec_align
  * pre: !AddrIsRmiGranuleAligned(rec_ptr)
  * post: result.status == RMI_ERROR_INPUT
* rec_tracking
  * pre: !PaIsTrackedFine(rec_ptr)
  * post: result.status == RMI_ERROR_INPUT
* rec_gran_state
  * pre: GranuleAt(rec_ptr).state != GRAN_REC
  * post: result.status == RMI_ERROR_INPUT
* rec_state
  * pre: rec.state == REC_RUNNING
  * post: result.status == RMI_ERROR_REC

## B4.5.50.2.1 Failure condition ordering

[rec\_tracking, rec\_gran\_state] &lt; [rec\_state]

<!-- image -->

## B4.5.50.3 Success conditions

* rec_gran_state
  * post: GranuleAt(rec_ptr).state == GRAN_DELEGATED
* num_recs
  * post: realm.num_recs == realm_pre.num_recs - 1

## B4.5.50.4 Footprint

| ID        | Value                    |
|-----------|--------------------------|
| rec_state | GranuleAt(rec_ptr).state |
| num_recs  | realm.num_recs           |