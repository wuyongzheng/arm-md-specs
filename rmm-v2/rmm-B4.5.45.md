## B4.5.45 RMI\_REALM\_ACTIVATE command

Activates a Realm.

## See also:

- [A2.2 Realm](rmm-A2.2.md)
- [B4.5.48 RMI\_REALM\_TERMINATE command](rmm-B4.5.48.md)

## B4.5.45.1 Interface

## B4.5.45.1.1 Input values

| Name   | Register   | Bits   | Type    | Description           |
|--------|------------|--------|---------|-----------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC4000157 |
| rd     | X1         | 63:0   | Address | PA of the RD          |

## B4.5.45.1.2 Context

The RMI\_REALM\_ACTIVATE command operates on the following context.

| Name   | Type     | Value       | Before   | Description   |
|--------|----------|-------------|----------|---------------|
| realm  | RmmRealm | RealmAt(rd) | false    | Realm         |

## B4.5.45.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |


## B4.5.45.2 Failure conditions

* rd_align
  * pre: !AddrIsRmiGranuleAligned(rd)
* rd_bound
  * pre: !PaIsTracked(rd)
  * post: result.status == RMI_ERROR_INPUT
* rd_state
  * pre: GranuleAt(rd).state != GRAN_RD
  * post: result.status == RMI_ERROR_INPUT
* realm_state
  * pre: realm.state != REALM_NEW
  * post: result.status == RMI_ERROR_REALM

## B4.5.45.2.1 Failure condition ordering

[rd\_bound, rd\_state] &lt; [realm\_state]

<!-- image -->

## B4.5.45.3 Success conditions

* realm_state
  * post: realm.state == REALM_ACTIVE
* realm_state
  * realm.state

