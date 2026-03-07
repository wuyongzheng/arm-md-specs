## B4.5.97 RMI\_VSMMU\_EVENT\_COMPLETE command

Complete a VSMMU event.

## See also:

- A9.8.6 Page Request Interface events
- B4.5.98 RMI\_VSMMU\_EVENT\_NOTIFY command

## B4.5.97.1 Interface

## B4.5.97.1.1 Input values

| Name      | Register   | Bits   | Type    | Description            |
|-----------|------------|--------|---------|------------------------|
| fid       | X0         | 63:0   | UInt64  | FID, value 0xC40001EE  |
| psmmu_ptr | X1         | 63:0   | Address | PA of the PSMMU        |
| rd        | X2         | 63:0   | Address | PA of the RD           |
| rec_ptr   | X3         | 63:0   | Address | PA of the REC          |
| psid      | X4         | 63:0   | Bits64  | Physical SMMUStream ID |

## B4.5.97.1.2 Context

The RMI\_VSMMU\_EVENT\_COMPLETE command operates on the following context.

| Name   | Type     | Value                    | Before Description   |
|--------|----------|--------------------------|----------------------|
| psmmu  | RmmPsmmu | PsmmuAt(psmmu_ptr) false | PSMMU                |
| realm  | RmmRealm | RealmAt(rd) false        | Realm                |
| rec    | RmmRec   | RecAt(rec_ptr) false     | REC                  |


## B4.5.97.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.97.2 Failure conditions

* feat
  * pre: Rmm().static.feat_vsmmu != FEATURE_TRUE
  * post: result.status == RMI_ERROR_NOT_SUPPORTED
* psmmu_valid
  * pre: !PsmmuAddrIsValid(psmmu_ptr)
  * post: result.status == RMI_ERROR_INPUT
* rd_align
  * pre: !AddrIsRmiGranuleAligned(rd)
  * post: result.status == RMI_ERROR_INPUT
* rd_bound
  * pre: !PaIsTracked(rd)
  * post: result.status == RMI_ERROR_INPUT
* rd_state
  * pre: GranuleAt(rd).state != GRAN_RD
  * post: result.status == RMI_ERROR_INPUT
* realm_state
  * pre: realm.state != REALM_NEW
  * post: result.status == RMI_ERROR_REALM
* rec_align
  * pre: !AddrIsRmiGranuleAligned(rec_ptr)
  * post: result.status == RMI_ERROR_INPUT
* rec_bound
  * pre: !PaIsTracked(rec_ptr)
  * post: result.status == RMI_ERROR_INPUT
* rec_gran_state
  * pre: GranuleAt(rec_ptr).state != GRAN_REC
  * post: result.status == RMI_ERROR_INPUT
* rec_realm
  * pre: rec.owner != rd
  * post: result.status == RMI_ERROR_INPUT
* rec_state
  * pre: rec.state == REC_RUNNING
  * post: result.status == RMI_ERROR_REC
* pending
  * pre: rec.pending != REC_PENDING_VSMMU_COMMAND
  * post: result.status == RMI_ERROR_INPUT
* q_full
  * pre: PsmmuCmdQueueFull(psmmu)
  * post: result.status == RMI_BUSY

## rd\_bound pre: !PaIsTracked(rd) post: result.status == RMI\_ERROR\_INPUT rd\_state pre: GranuleAt(rd).state != GRAN\_RD post: result.status == RMI\_ERROR\_INPUT realm\_state pre: realm.state != REALM\_NEW post: result.status == RMI\_ERROR\_REALM rec\_align pre: !AddrIsRmiGranuleAligned(rec\_ptr) post: result.status == RMI\_ERROR\_INPUT rec\_bound pre: !PaIsTracked(rec\_ptr) post: result.status == RMI\_ERROR\_INPUT rec\_gran\_state pre: GranuleAt(rec\_ptr).state != GRAN\_REC post: result.status == RMI\_ERROR\_INPUT rec\_realm pre: rec.owner != rd post: result.status == RMI\_ERROR\_INPUT rec\_state pre: rec.state == REC\_RUNNING post: result.status == RMI\_ERROR\_REC pending pre: rec.pending != REC\_PENDING\_VSMMU\_COMMAND post: result.status == RMI\_ERROR\_INPUT q\_full pre: PsmmuCmdQueueFull(psmmu) post: result.status == RMI\_BUSY B4.5.97.2.1 Failure condition ordering [rd\_bound, rd\_state] &lt; [realm\_state] feat psmmu\_valid

## B4.5.97.3 Success conditions



post: rec.pending == REC\_PENDING\_VSMMU\_COMPLETE

## B4.5.97.4 Footprint

The RMI\_VSMMU\_EVENT\_COMPLETE command does not have any footprint.

ID

pending